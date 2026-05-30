import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wavio

# Define function to recognize speech
def takeCommand():
    r = sr.Recognizer()
    fs = 44100  # Sampling rate
    duration = 5  # seconds to listen — you can adjust this
    print("Listening...")
    # text_widget.configure(state="normal")
    # text_widget.insert("end", "JARVIS: Listening...\n")
    # text_widget.configure(state="disabled")

    # Record from the default microphone using sounddevice
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save the recording temporarily
    wavio.write("temp.wav", audio_data, fs, sampwidth=2)

    print("Recognizing...")
    # text_widget.configure(state="normal")
    # text_widget.insert("end", "JARVIS: Recognizing...\n")
    # text_widget.configure(state="disabled")

    try:
        with sr.AudioFile("temp.wav") as source:
            audio = r.record(source)
        query = r.recognize_google(audio, language='en-in')
        # text_widget.configure(state="normal")
        # text_widget.insert("end", f"YOU: {query}\n")
        # text_widget.configure(state="disabled")
        print(f"You said: {query}\n")
        return query.lower()

    except Exception as e:
        print(e)
        # text_widget.configure(state="normal")
        # text_widget.insert("end", f"JARVIS: {e}\n")
        # text_widget.configure(state="disabled")
        return "None"

if __name__ == "__main__":
    print("Testing microphone input...")
    result = takeCommand()
    print("Result:", result)
