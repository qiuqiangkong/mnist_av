# MNIST-AV Dataset

MNIST-AV [[download]](https://huggingface.co/datasets/qiuqiangkong/mnist_av/blob/main/mnist_av.zip) is a synthetic audio-visual dataset with synchronized digit videos, instrument sounds, and text descriptions for multimodal learning research. The dataset contains 60,000 training samples and 10,000 test samples, each consisting of a 2-second video clip paired with corresponding audio and natural language descriptions. The total dataset size is approximately 2 GB.

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
  src="https://github.com/user-attachments/assets/9867fe73-8d0d-48ab-8437-f25ab3c6105c"
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
{"video_fps": 24, "audio_sr": 16000, "digit": 2, "speed": -116.73286592787174, "instrument": "piano"}
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

### 2.1 Set Up the Environment

```bash
git clone https://github.com/qiuqiangkong/mnist_av
cd mnist_av

uv sync
source .venv/bin/activate
```

### 2.2 Download the SoundFont

Download the `FluidR3_GM.sf2` SoundFont from: https://musical-artifacts.com/artifacts/738/FluidR3_GM.sf2

### 2.3 Run

```python
python create_dataset.py
```

## License

This project is licensed under the MIT License.
