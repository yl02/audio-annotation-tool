import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def load_audio(file_path):
    """加载音频文件"""
    y, sr = librosa.load(file_path, sr=None)
    return y, sr

def plot_waveform(y, sr):
    """绘制音频波形"""
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Audio Waveform")
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf
    