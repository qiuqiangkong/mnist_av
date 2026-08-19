# MNIST-AV

A Synthetic Audio-Visual Dataset for Multimodal Learning

## Overview

MNIST-AV is a synthetic audio-visual dataset. Each sample is generated with including digit identity, motion speed, and audio instrument.

The dataset can be downloaded at xxx

Users can also reproduce the dataset by running: 

1. Download SoundFont 2 to produce audio from https://musical-artifacts.com/artifacts/738/FluidR3_GM.sf2

```bash
$ git clone https://github.com/qiuqiangkong/mnist_av
$ cd mnist_av
$ uv sync
$ source .venv/bin/activate
```

```python
python create_dataset.py
```

## LICENSE

MIT