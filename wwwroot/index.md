# A FastVLM webserver
[fastvlm](https://github.com/apple/ml-fastvlm) is apple released a open source
multiple modal llm, it can input image, promt and generate text

## Usage
```
curl https://{domain}/v1/generate \
    -F "prompt=描述这张图片" \
    -F "image_path=@path_to_image"
```

