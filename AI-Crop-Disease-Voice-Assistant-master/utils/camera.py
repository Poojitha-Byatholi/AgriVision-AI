import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from PIL import Image
from utils.language import t
import threading

class LeafCapture(VideoTransformerBase):
    def __init__(self):
        self.frame = None
        self.lock = threading.Lock()

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        with self.lock:
            self.frame = img
        return img


def capture_leaf_image(language):
    ctx = webrtc_webrtc = webrtc_streamer(
        key="leaf-camera",
        video_transformer_factory=LeafCapture,
        media_stream_constraints={"video": True, "audio": False},
        async_transform=True,
    )

    captured_image = None

    if ctx.video_transformer:
        if st.button("📸 " + t(language, "capture_image")):
            with ctx.video_transformer.lock:
                frame = ctx.video_transformer.frame

            if frame is not None:
                captured_image = Image.fromarray(
                    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                )
                st.success(t(language, "image_captured_success"))

    return captured_image
