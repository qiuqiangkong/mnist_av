import json
import os
from pathlib import Path

import cv2
import numpy as np
import pretty_midi
import soundfile as sf
from datasets import load_dataset
from PIL import Image

INSTS_MAP = {
    "piano":  "Acoustic Grand Piano",
    "violin": "Violin",
    "viola": "Viola",
    "cello": "Cello",
    "flute": "Flute",
    "clarinet": "Clarinet",
    "oboe": "Oboe",
    "trumpet": "Trumpet",
    "guitar": "Acoustic Guitar (nylon)",
    "harp": "Orchestral Harp"
}


def create_dataset(split: str) -> None:

    duration = 2.
    video_fps = 12
    audio_sr = 16000
    max_deg_per_sec = 180
    rs = np.random.RandomState(1234)

    dataset = load_dataset("mnist")
    imgs = dataset[split]["image"]
    tgts = dataset[split]["label"]
    n_data = len(imgs)
    
    tmp_dir = Path("./_tmp")
    root = Path("./dataset")

    for n in range(n_data):
        # Video
        print(f"{n}/{n_data}")
        x = imgs[n].resize((32, 32), Image.BILINEAR)
        speed = rs.uniform(-max_deg_per_sec, max_deg_per_sec)
        xs = rotate_mnist(x, duration, speed, video_fps)

        video_path = tmp_dir / split / "video_only" / f"{n:05d}.mp4"
        video_path.parent.mkdir(parents=True, exist_ok=True)
        pil_to_video(xs, path=video_path, fps=video_fps)
        print(f"Write to {video_path}")

        # Audio
        inst_name = rs.choice(list(INSTS_MAP.keys()))
        audio = create_audio(INSTS_MAP[inst_name], duration, speed, audio_sr)

        audio_path = tmp_dir / split / "audio_only" / f"{n:05d}.wav"
        audio_path.parent.mkdir(parents=True, exist_ok=True)
        sf.write(file=audio_path, data=audio, samplerate=audio_sr)
        print(f"Write to {audio_path}")
        
        # Audio & Video
        out_path = root / split / "audio_video" / f"{n:05d}.mp4"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        os.system(f'ffmpeg -y -loglevel error -i {video_path} -i {audio_path} -c:v copy -c:a aac {out_path}')
        print(f"Write to {out_path}")

        # Metadata
        meta = {
            "digit": tgts[n],
            "speed": speed,
            "instrument": inst_name
        }

        meta_path = root / split / "metadata" / f"{n:05d}.json"
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        write_jsonl(meta, meta_path)
        print(f"Write to {meta_path}")

        # if n == 100:
        #     break
        

def rotate_mnist(
    image: Image,
    duration: float,
    speed: float,
    fps: float,
    start_angle=0
):
    """Rotate image.

    Args:
        image: (Image)
        speed: (float): rotate speed per second
        fps: (float)

    Returns:
        frames: (list[Image])
    """

    n_frames = int(duration * fps)
    frames = []

    for t in range(n_frames):
        angle = start_angle + (speed / fps) * t
        frame = image.rotate(angle, resample=Image.BILINEAR)
        frames.append(frame)

    return frames


def pil_to_video(images: list[Image], path: str, fps: int) -> None:
    r"""Write images to video.
    """
    frames = [np.array(img.convert("RGB")) for img in images]
    h, w, _ = frames[0].shape

    # VideoWriter
    writer = cv2.VideoWriter(
        path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (w, h)
    )

    for frame in frames:
        # RGB -> BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        writer.write(frame)

    writer.release()


def create_audio(instrument_name: str, duration: float, speed: float, sr: float) -> np.ndarray:
    r"""Create audio.
    """
    midi = pretty_midi.PrettyMIDI()

    instrument = pretty_midi.Instrument(
        program=pretty_midi.instrument_name_to_program(instrument_name)
    )

    onsets = np.arange(0, duration, 30 / np.abs(speed))
    offsets = np.concatenate([onsets[1:], [duration]], axis=0)
    n_notes = len(onsets)
    
    if speed >= 0:
        intervals = np.array([0, 2, 4, 5, 7, 9, 11])
        intervals = np.concatenate([intervals, intervals + 12, intervals + 24], axis=0)
    else:
        intervals = np.array([0, -1, -3, -5, -7, -8, -10])
        intervals = np.concatenate([intervals, intervals - 12, intervals - 24], axis=0)

    intervals = intervals[0 : n_notes]

    for i in range(n_notes):
        note = pretty_midi.Note(
            velocity=100,
            pitch=60 + intervals[i],
            start=onsets[i],
            end=offsets[i]
        )
        instrument.notes.append(note)
    
    midi.instruments.append(instrument)
    audio = midi.fluidsynth(sf2_path="FluidR3_GM.sf2", fs=sr)
    audio = audio[0 : int(duration * sr)]
    return audio
        

def write_jsonl(meta: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False))


if __name__ == '__main__':
    create_dataset(split="train")
    create_dataset(split="test")