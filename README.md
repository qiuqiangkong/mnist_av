# MNIST-AV Dataset

A synthetic audio-visual dataset with synchronized digit videos, instrument sounds, and text descriptions for multimodal learning research.

<table>
<tr>
<td width="16.6%">
Video with audio
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="https://github.com/user-attachments/assets/58144316-d816-4da2-903a-55d987a7dc21" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
  

https://github.com/user-attachments/assets/c6ad7544-716e-4675-b741-1bcf1736d81f


<source src="./demo9.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo10.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo11.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo12.mp4" type="video/mp4">
</video>
</td>
</tr>

<tr>
<td width="16.6%">
Metadata
</video>
</td>

<td width="16.6%">
{"video_fps": 24, "audio_sr": 16000, "digit": 0, "speed": -79.3532652822735, "instrument": "harp"}
</video>
</td>

<td width="16.6%">
{"video_fps": 24, "audio_sr": 16000, "digit": 1, "speed": 50.48710167061431, "instrument": "oboe"}
</video>
</td>

<td width="16.6%">
{"video_fps": 24, "audio_sr": 16000, "digit": 3, "speed": 80.23661416370088, "instrument": "viola"}
</video>
</td>

<td width="16.6%">
{"video_fps": 24, "audio_sr": 16000, "digit": 2, "speed": -116.73286592787174, "instrument": "piano"}
</video>
</td>

<td width="16.6%">
{"video_fps": 24, "audio_sr": 16000, "digit": 8, "speed": -33.987388002672645, "instrument": "oboe"}
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
