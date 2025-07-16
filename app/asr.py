from ahserver.webapp import webapp
from ahserver.serverenv import ServerEnv
from ahserver.filestorage import FileStorage
from appPublic.log import debug,exception, error
from appPublic.worker import awaitify
from appPublic.jsonConfig import getConfig
import torch
import nemo.collections.asr as nemo_asr

class NVidiaASR:
	def __init__(self):
		config = getConfig()
		self.models = {}
		device = torch.device(config.device)
		for lang, model_path in config.asr_models.items():
			debug(f'{lang=}, {model_path=}')
			model = None
			if lang == 'en':
				model = nemo_asr.models.EncDecCTCModelBPE.restore_from(model_path)
			elif lang == 'cn':
				model = nemo_asr.models.EncDecCTCModel.restore_from(model_path)
			model.to(device)
			self.models[lang] = model
	
	def _generate(self, audio_file, lang):
		model = self.models.get(lang)
		output = model.transcribe([audio_file])
		return output
	
	async def generate(self, audio_file, lang='en'):
		f = awaitify(self._generate)
		t1 = time.time()
		content = await f(audio_file, lang)
		t2 = time.time()
		return {
			'content':content,
			'timecost':t2 - t1
		}

def init():
	g = ServerEnv()
	g.asr_engine = NVidiaASR()
	g.generate = g.asr_engine.generate

if __name__ == '__main__':
	webapp(init)

