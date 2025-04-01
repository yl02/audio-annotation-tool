import streamlit as st
import os
import librosa
import numpy as np
import json
from utils.audio_processing import load_audio, plot_waveform
from utils.annotation_utils import save_annotations, load_annotations

# 设置 Streamlit 页面
st.set_page_config(page_title="音乐音频标注工具", layout="wide")
st.title("🎵 音乐音频标注工具")

# 上传音频文件
uploaded_file = st.file_uploader("上传音频文件", type=["mp3", "wav"])
if uploaded_file is not None:
    file_path = f"assets/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(file_path, format="audio/mp3")

    # 加载音频并绘制波形
    y, sr = load_audio(file_path)
    waveform_plot = plot_waveform(y, sr)
    st.image(waveform_plot, caption="音频波形")

    # 加载标注
    annotations = load_annotations()

    # 显示现有标注信息
    title = st.text_input("曲目名称", annotations.get("title", ""))
    artist = st.text_input("艺术家", annotations.get("artist", ""))
    emotion = st.selectbox("情感标签", ["Happy", "Sad", "Angry"], index=0)

    # 关键时间点标注
    segments = st.text_area("标注关键段落（格式：时间,标签）", "30,副歌\n60,乐器独奏")
    segment_list = [{"time": int(line.split(",")[0]), "label": line.split(",")[1]} for line in segments.split("\n")]

    # 保存标注
    if st.button("保存标注"):
        annotation_data = {
            "title": title,
            "artist": artist,
            "segments": segment_list,
            "emotion": emotion
        }
        save_annotations(annotation_data)
        st.success("标注数据已保存！")