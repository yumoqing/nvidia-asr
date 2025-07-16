#!/usr/bin/bash

rundir=/share/ymq/run/nvidia-asr
cd $rundir
CUDA_VISIBLE_DEVICES=6 $rundir/nvidia-asr.env/bin/python app/asr.py -p 9992 &
CUDA_VISIBLE_DEVICES=6 $rundir/nvidia-asr.env/bin/python app/asr.py -p 9992 &

