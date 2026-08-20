# MNIST-AV Dataset

MNIST-AV [download](https://huggingface.co/datasets/qiuqiangkong/mnist_av/blob/main/mnist_av.zip) is a synthetic audio-visual dataset with synchronized digit videos, instrument sounds, and text descriptions for multimodal learning research. The dataset contains 60,000 training samples and 10,000 test samples, each consisting of a 2-second video clip paired with corresponding audio and natural language descriptions. The total dataset size is approximately 2 GB.

<table>
<tr>
<td width="20%">
Video with audio
</video>
</td>

<td width="20%">
<video 
  src="https://github.com/user-attachments/assets/35e93ac9-baea-45f7-a37f-f9e887800dd3"
  controls
  width="100%">
</video>
</td>

<td width="20%">
<video 
  src="https://github.com/user-attachments/assets/62b3e8ec-069d-40da-8f3c-28434759a67a"
  controls
  width="100%">
</video>
</td>

<td width="20%">
<video 
  src="https://github.com/user-attachments/assets/31b81777-ee97-4cff-b4a6-12cf3189426e"
  controls
  width="100%">
</video>
</td>

<tr>
<td width="20%">
Metadata
</video>
</td>

<td width="20%">
{"video_fps": 24, "audio_sr": 16000, "digit": 0, "speed": -79.3532652822735, "instrument": "harp"}
</video>
</td>

<td width="20%">
{"video_fps": 24, "audio_sr": 16000, "digit": 1, "speed": 50.48710167061431, "instrument": "oboe"}
</video>
</td>

<td width="20%">
{"video_fps": 24, "audio_sr": 16000, "digit": 3, "speed": 80.23661416370088, "instrument": "viola"}
</video>
</td>

</tr>

</table>

## 1. Download

```bash
wget -O "mnist_av.zip" "https://huggingface.co/datasets/qiuqiangkong/mnist_av/resolve/main/mnist_av.zip?download=true"
```

## 2. Reproduce Dataset (Optional)

The dataset can also be reproduced from scratch using the following steps.

### 2.1 Download the SoundFont

Download the `FluidR3_GM.sf2` SoundFont from: https://musical-artifacts.com/artifacts/738/FluidR3_GM.sf2

Place the downloaded file in the project directory.

### 2.2 Set Up the Environment

```bash
git clone https://github.com/qiuqiangkong/mnist_av
cd mnist_av
uv sync
source .venv/bin/activate
```

```python
source .venv/bin/activate
python create_dataset.py
```

## License

This project is licensed under the MIT License.
