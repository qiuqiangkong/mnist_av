# MNIST-AV Dataset

A synthetic audio-visual dataset with synchronized digit videos, instrument sounds, and text descriptions for multimodal learning research.

<table>
<tr>
<td width="16.6%">
<video controls width="100%">
<source src="./demo1.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo2.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo3.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo4.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo5.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo6.mp4" type="video/mp4">
</video>
</td>
</tr>

<tr>
<td width="16.6%">
<video controls width="100%">
<source src="./demo7.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
<source src="./demo8.mp4" type="video/mp4">
</video>
</td>

<td width="16.6%">
<video controls width="100%">
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