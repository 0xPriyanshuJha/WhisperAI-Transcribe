import streamlit as st
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Streamlit app
st.title("Whisper Audio Transcription")

# File uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    # Save the uploaded file temporarily
    with open("uploaded_audio.mp3", "wb") as f:
        f.write(audio_file.getbuffer())

    st.write("Transcribing...")

    # Transcribe the audio file using Whisper
    result = model.transcribe("uploaded_audio.mp3")

    # Display the transcription
    st.write("Transcription:")
    st.text_area("", result["text"], height=200)

    # Option to download the transcription as a .txt file
    st.download_button(
        label="Download Transcription",
        data=result["text"],
        file_name="transcription.txt",
        mime="text/plain"
    )
