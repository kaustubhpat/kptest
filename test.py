import cv2
import numpy as np
import streamlit as st

# Function to capture video stream from camera
def capture_video_stream(ip_address):
    try:
        video_capture = cv2.VideoCapture(ip_address)
        while True:
            _, frame = video_capture.read()
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            yield frame_rgb
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

# Streamlit web interface
def main():
    st.title("Live Camera Stream with OpenCV and Streamlit")
    ip_address = st.text_input("Enter IP Address of the Camera")

    if ip_address:
        video_stream = capture_video_stream(ip_address)
        video_player = st.empty()
        
        for frame in video_stream:
            video_player.image(frame, channels="RGB")

# Run the Streamlit app
if __name__ == "__main__":
    main()
