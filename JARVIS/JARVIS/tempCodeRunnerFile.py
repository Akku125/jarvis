# from tkinter import Tk, Canvas, Text, Button, PhotoImage, Scrollbar, INSERT, END, Y
# from pathlib import Path
# import threading
# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import random
# import speech_recognition as sr
# import smtplib
# import song
# import requests
# import json
# import re
# import pywhatkit
# from bs4 import BeautifulSoup
# import os
# import psutil
# import pyautogui
# import time
# import hashlib
# #update 1
# import sounddevice as sd
# import numpy as np
# import wavio


# # Set up text-to-speech engine
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


# # Define function to speak text
# def speak(text, text_widget):
#     print(f":{text}")  # added for test
#     text_widget.configure(state="normal")
#     text_widget.insert("end", f"JARVIS: {text}\n")
#     text_widget.configure(state="disabled")
#     text_widget.see(END)   #For scrolling text widget automatically
#     engine.say(text) # speak the audio
#     engine.runAndWait() # wait for speech to complete


# # Define function to recognize speech
# def takeCommand():
#     r = sr.Recognizer()
#     fs = 44100  # Sampling rate
#     duration = 5  # seconds to listen — you can adjust this
#     print("Listening...")
#     # text_widget.configure(state="normal")
#     # text_widget.insert("end", "JARVIS: Listening...\n")
#     # text_widget.configure(state="disabled")

#     # Record from the default microphone using sounddevice
#     audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()  # Wait until recording is finished

#     # Save the recording temporarily
#     wavio.write("temp.wav", audio_data, fs, sampwidth=2)

#     print("Recognizing...")
#     # text_widget.configure(state="normal")
#     # text_widget.insert("end", "JARVIS: Recognizing...\n")
#     # text_widget.configure(state="disabled")

#     try:
#         with sr.AudioFile("temp.wav") as source:
#             audio = r.record(source)
#         query = r.recognize_google(audio, language='en-in')
#         # text_widget.configure(state="normal")
#         # text_widget.insert("end", f"YOU: {query}\n")
#         # text_widget.configure(state="disabled")
#         print(f"You said: {query}\n")
#         return query.lower()

#     except Exception as e:
#         print(e)
#         # text_widget.configure(state="normal")
#         # text_widget.insert("end", f"JARVIS: {e}\n")
#         # text_widget.configure(state="disabled")
#         return "None"


# def run_jarvis():
#     while True:
#         query = takeCommand().lower()
#         print(f"[DEBUG] Recognized Command: {query}")  # 👈 console feedback
#         speak(f"You said {query}", text_widget)         # 👈 audio + GUI feedback
#         log_query(query)



#     # # Password authentication
#     # if authenticate_user():
#     #     # Call the speak function from JARVIS
#     #     speak("Activating........", text_widget)
#     #     hour = datetime.datetime.now().hour
#     #     if hour >= 0 and hour < 12:
#     #         speak("Good morning!", text_widget)
#     #     elif hour >= 12 and hour < 18:
#     #         speak("Good afternoon!", text_widget)
#     #     else:
#     #         speak("Good evening!", text_widget)

#     #     speak("I am Jarvis. How may I assist you?", text_widget)

#     #     while True:
#     #         query = takeCommand().lower()
#     #         log_query(query)

#     #         # Search Wikipedia
#     #         if 'wikipedia' in query:
#     #             speak('Searching Wikipedia...', text_widget)
#     #             query = query.replace("wikipedia", "")
#     #             results = wikipedia.summary(query, sentences=2)
#     #             speak("According to Wikipedia:", text_widget)
#     #             speak(results, text_widget)

#     #         # Open website
#     #         elif 'open youtube' in query:
#     #             webbrowser.open("youtube.com")
#     #             speak("Opening YouTube...", text_widget)

#     #         elif 'open google' in query:
#     #             webbrowser.open("google.com")
#     #             speak("Opening Google...", text_widget)

#     #         elif 'open stack overflow' in query:
#     #             webbrowser.open("stackoverflow.com")
#     #             speak("Opening Stack Overflow...", text_widget)
            
#     #         #googleSearch
#     #         elif 'google search' in query:
#     #             GoogleSearch(query)

#     #         # Play a song
#     #         elif 'play' in query:
#     #             play_song()


#     #         # Get the time
#     #         elif 'the time' in query:
#     #             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#     #             speak(f"The time is {strTime}", text_widget)

#     #         # Send email
#     #         elif 'send email' in query:
#     #             send_email()
            
#     #         #Know weather
#     #         elif 'weather' in query:
#     #             run_get_weather()
            
#     #         #Recipies
#     #         elif 'how to cook' in query:
#     #             dish = query.lower().replace("jarvis","").replace("how to cook ","")
#     #             how_to_make(dish)

#     #         #Youtube Search
#     #         elif 'youtube search' in query:
#     #             YouTubeSearch(query)
        
#     #         #Whatsapp Message
#     #         elif 'whatsapp message' in query:
#     #             send_whatsapp_message()
            

#     #         #Window Automation: Shut Down
#     #         elif 'shutdown the system' in query:
#     #             shut_down()
            
#     #         #Window Automation : Restart
#     #         elif "restart the system" in query:
#     #             restart()
            
#     #         #Window Automation : Checking Battery Level
#     #         elif "check battery level" in query:
#     #             check_battery()
            
#     #         #Window Automation: ScreenShot
#     #         elif "take screenshot" in query:
#     #             take_screenshot()

#     #         # Window automation: Open basic applications
#     #         # NotePad
#     #         elif "open notepad" in query:
#     #             open_notepad()
#     #         # Word
#     #         elif "open word" in query:
#     #             open_word()
#     #         #Excel
#     #         elif "open excel" in query:
#     #             open_excel()
#     #         #PowerPoint
#     #         elif "open powerpoint" in query:
#     #             open_powerpoint()
#     #         #Paint
#     #         elif "open paint" in query:
#     #             open_paint()
#     #         #Calculator
#     #         elif "open calculator" in query:
#     #             open_calc()
#     #         #cmd
#     #         elif "open cmd" in query:
#     #             open_cmd()
#     #         #Photos
#     #         elif "open photos" in query:
#     #             open_photos()
#     #         elif "open camera" in query:
#     #             open_camera()
            
#     #         #Window Automation: Closing Applications like chrome, brave, notepad, word, excel, powerpoint, paint, calculator and cmd
#     #         elif "close" in query:
#     #             pyautogui.hotkey('alt', 'f4')
            
#     #         # elif"chat gpt mode" in query:
#     #         #     chat_gpt_mode()
#     #         elif "copy" in query:
#     #             copy_things()
#     #         elif"cut" in query:
#     #             cut_things()
#     #         elif"paste"in query:
#     #             paste_things()
#     #         elif"type mode" in query:
#     #             typing_mode()
#     #         elif"toss coin" in query:
#     #             toss_coin()
#     #         #Calculator
#     #         elif"calculate" in query:
#     #             calculator(query)
#     #         # Meditation Guide
#     #         elif 'meditation guide' in query:
#     #             meditation_guide(text_widget)
#     #         #exiting from jarvis
#     #         elif any(word in query.lower() for word in ["close", "exit", "bye"]):
#     #             exit_jarvis()
            

#     #         # Chat with Jarvis & logging Unhandled queries for future
#     #         elif True:
#     #             handled = False
#     #             for i in range(len(patterns)):
#     #                 for j in range(len(patterns[i])):
#     #                     if patterns[i][j] in query:
#     #                         response = random.choice(responses[i])
#     #                         speak(response, text_widget)
#     #                         handled = True
#     #                         break
#     #                 if handled:
#     #                     break
#     #             if not handled:
#     #                 log_unhandled_query(query)
#     #                 speak("Sorry, I am not programmed to handle that yet. I have logged your query and will work on adding the functionality in the future.", text_widget)
        


if __name__ == "__main__":
    print("Testing microphone input...")
    result = takeCommand()
    print("Result:", result)
