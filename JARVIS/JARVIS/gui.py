from tkinter import Tk, Canvas, Text, Button, PhotoImage, Scrollbar, INSERT, END, Y
from pathlib import Path
import threading
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import speech_recognition as sr
import smtplib
import song
import requests
import json
import re
import pywhatkit
from bs4 import BeautifulSoup
import os
import psutil
import pyautogui
import time
import hashlib
#update 1
import sounddevice as sd
import numpy as np
import wavio
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\yadav\Desktop\JARVIS\JARVIS\assets\frame0")
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\AKSHAY KUMAR\Desktop\JARVIS\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Set up text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Patterns & Responses for chating with jarvis
patterns = [        ["hi", "hello", "hey", "hi there"],
        ["how are you", "how are things"],
        ["what is your name", "what's your name", "can i know your name", "who are you"],
        ["how old are you", "what is your age"],
        ["what do you do", "what is your job", "what do you do for a living"],
        ["tell me a joke", "say something funny"],
        ["bye", "goodbye", "see you later", "have a nice day"]
    ]
responses = [        ["Hello!", "Hi there!", "Hi!", "Hey!"],
        ["I'm doing great, thank you!", "Everything is going well!", "Things are good!"],
        ["My name is Jarvis.", "I'm Jarvis, your personal assistant.", "I'm Jarvis.", "I'm your personal assistant Jarvis."],
        ["I'm an AI language model, so I don't age!", "I'm ageless!", "I don't have an age, I'm a machine!"],
        ["I'm your personal assistant, I can help you with your tasks and answer your questions!", "I'm here to assist you!", "I can help you with your tasks and answer your questions!"],
        ["Why did the tomato turn red? Because it saw the salad dressing!", "Why couldn't the bicycle stand up by itself? Because it was two-tired!", "Why don't scientists trust atoms? Because they make up everything!"],
        ["Goodbye!", "See you later!", "Have a nice day!"]
    ]

# Define function to speak text
def speak(text, text_widget):
    print(f":{text}")  # added for test
    text_widget.configure(state="normal")
    text_widget.insert("end", f"JARVIS: {text}\n")
    text_widget.configure(state="disabled")
    text_widget.see(END)   #For scrolling text widget automatically
    engine.say(text) # speak the audio
    engine.runAndWait() # wait for speech to complete


# Define function to recognize speech
def takeCommand():
    r = sr.Recognizer()
    fs = 44100  # Sampling rate
    duration = 5  # seconds to listen — you can adjust this
    print("Listening...")
    text_widget.configure(state="normal")
    text_widget.insert("end", "JARVIS: Listening...\n")
    text_widget.configure(state="disabled")

    # Record from the default microphone using sounddevice
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save the recording temporarily
    wavio.write("temp.wav", audio_data, fs, sampwidth=2)

    print("Recognizing...")
    text_widget.configure(state="normal")
    text_widget.insert("end", "JARVIS: Recognizing...\n")
    text_widget.configure(state="disabled")

    try:
        with sr.AudioFile("temp.wav") as source:
            audio = r.record(source)
        query = r.recognize_google(audio, language='en-in')
        text_widget.configure(state="normal")
        text_widget.insert("end", f"YOU: {query}\n")
        text_widget.configure(state="disabled")
        print(f"You said: {query}\n")
        return query.lower()

    except Exception as e:
        print(e)
        text_widget.configure(state="normal")
        text_widget.insert("end", f"JARVIS: {e}\n")
        text_widget.configure(state="disabled")
        return "None"

#OLD TAKE COMMAND 
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         text_widget.configure(state="normal")
#         text_widget.insert("end", f"JARVIS: Listening\n")
#         text_widget.configure(state="disabled")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         text_widget.configure(state="normal")
#         text_widget.insert("end", f"JARVIS: Recognizing\n")
#         text_widget.configure(state="disabled")
#         query = r.recognize_google(audio, language='en-in')
#         text_widget.configure(state="normal")
#         text_widget.insert("end", f"YOU: {query}\n")
#         text_widget.configure(state="disabled")
#         print(f"You said: {query}\n")

#     except Exception as e:
#         print(e)
#         text_widget.configure(state="normal")
#         text_widget.insert("end", f"JARVIS: {e}\n")
#         text_widget.configure(state="disabled")
#         return "None"
#     return query.lower()

#for logging the unhandled queries for making it better 
def log_unhandled_query(query):
    with open('unhandled_queries.txt', 'a') as f:
        f.write(query+'\n')

# for logging and maintaing a History
def log_query(query):
    with open("query_history.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {query}\n")

window = Tk()

window.geometry("800x500")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    250.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    161.0,
    64.0,
    image=image_image_2
)

# Text widget with scrollbar
text_widget = Text(
    window,
    wrap="word",
    font=("Helvetica", 12),
    bg="#D9D9D9",
    relief="flat",
    state='disabled'
)
text_widget.place(x=50, y=366.5, width=699, height=114)

scrollbar = Scrollbar(window)
scrollbar.place(x=749, y=366.5, height=114)

text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

####################################################################################################
#Features
####################################################################################################
# Function to play a song
def play_song():
    # Ask the user for the name of the song to play
    speak("Sure, what song would you like to play?", text_widget)
    song_name = takeCommand().lower()

    # Check if the user provided a song name
    if song_name:
        # Call the play_song() function from the song.py file
        try:
            song.search_and_play_song(song_name)
        except:
            speak("Sorry, there was an error playing that song.", text_widget)
    else:
        speak("Sorry, I didn't catch the name of the song.", text_widget)

#Fuction For Weather
def get_weather(city):
    # API key and base URL
    api_key = "8c75364cc8b3384015803855cda9daa0"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q="
    
    # format the city name
    city = re.sub('[^A-Za-z]+', '', city)
    
    # make the API call
    try:
        url = base_url + city
        response = requests.get(url)
        data = json.loads(response.text)
    except:
        return "Sorry, I could not get the weather for that city."
    
    # parse the API response
    if data["cod"] == "404":
        return "Sorry, I could not find the weather for that city."
    else:
        weather_description = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 1)
        feels_like = round(data["main"]["feels_like"] - 273.15, 1)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        # construct the response
        response = f"The weather in {city} is {weather_description}, with a temperature of {temperature} degrees Celsius. It feels like {feels_like} degrees Celsius, with a humidity of {humidity}% and a wind speed of {wind_speed} meters per second."
        return response

def run_get_weather():
    speak("Sure, which city would you like the weather for?", text_widget)
    city = takeCommand().lower()
    weather = get_weather(city)
    speak(weather, text_widget) 


# Getting Recipies Via Spooncacular API 
def how_to_make(dish_name):
    api_key = 'd39c89949b4c4fad8d27fb82918fc2f5'
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query={dish_name}&number=1'
    response = requests.get(url)
    data = response.json()

    if data['totalResults'] == 0:
        print("Sorry, I couldn't find any results for that dish.")
        speak("Sorry, I couldn't find instructions for that dish.", text_widget)
        return
    else:
        recipe_id = data['results'][0]['id']
        url = f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey={api_key}'
        response = requests.get(url)
        data = response.json()

        if not data:
            print("Sorry, I couldn't find instructions for that dish.")
            speak("Sorry, I couldn't find instructions for that dish.", text_widget)
            return
        else:
            instructions = data[0]['steps']
            for i, step in enumerate(instructions[:3]):
                print(f"Step {i+1}: {step['step']}")
                speak(f"Step {i+1}:{step['step']}", text_widget)
            return


#Youtube Search
def YouTubeSearch(term):
    query = term.lower().replace("jarvis", "").replace("search youTube for", "").replace("on youtube", "").replace("youtube search","")
    
    with open('C:\\Users\\yadav\\Downloads\\JARVIS\\JARVIS\\Data.txt', 'a') as file:
        file.write(query + '\n')

    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(url)

    speak("This is what I found for your search.", text_widget)
    pywhatkit.playonyt(query)
    speak("This may also help you, sir.", text_widget)

#Whatsapp Automations

# Define the contacts
contacts = {
    "mom": "+919773614966",
    "dad": "+919968892071",
    "shivam": "+919910349134",
    "anikesh": "+918757858082"
}

# Define the function to send messages
def send_whatsapp_message():
    # Ask for the contact name and message to send
    speak("Who do you want to send a message to?", text_widget)
    print("Who do you want to send a message to?")
    contact_name = takeCommand().lower()
    
    speak("What message do you want to send?", text_widget) 
    print("What message do you want to send?") 
    message = takeCommand().lower()

    # Confirm the message
    speak(f"You want to send the following message to {contact_name}:", text_widget)
    print(f"You want to send the following message to {contact_name}:", text_widget)
    speak(message, text_widget)
    print(message)
    speak("Are you sure you want to send this message?", text_widget)
    print("Are you sure you want to send this message?")
    confirmation = takeCommand().lower()

    # Send the message if confirmed
    if confirmation.lower() == "yes" or confirmation.lower() == "yeah":
        phone_number = contacts.get(contact_name)
        if phone_number:
            pywhatkit.sendwhatmsg_instantly(phone_number, message)
            speak(f"Message sent to {contact_name}", text_widget)
            print(f"Message sent to {contact_name}")
        else:
            speak(f"Sorry, I couldn't find the contact {contact_name}", text_widget)
            print(f"Sorry, I couldn't find the contact {contact_name}")
    else:
        speak("Message not sent", text_widget)
        print("Message not sent")

# Window automation: shut down
def shut_down():
    """
    Prompts the user for confirmation before shutting down the system.
    """
    message = "Are you sure you want to shut down your system?"
    speak(message, text_widget)
    
    confirmation = takeCommand()
    if confirmation.lower() in ["yes", "yeah"]:
        os.system("shutdown /s /t 5")
    else:
        funny_messages = [
            "Ok sir, let's keep working. Did you know that the shortest war in history lasted only 38 minutes?",
            "Alright, let's keep going. Did you know that laughter is contagious and can improve your immune system?",
            "No problem, let's continue. Did you know that the first computer mouse was made of wood?",
            "Sure thing, let's get back to work. Did you know that the world's largest snowflake on record measured 15 inches wide and 8 inches thick?",
            "Got it, let's keep going. Did you know that a group of flamingos is called a flamboyance?"
        ]
        funny_message = random.choice(funny_messages)
        speak(funny_message, text_widget)

# Window automation: restart
def restart():
    """
    Prompts the user for confirmation before restarting the system.
    """
    message = "Are you sure you want to restart your system?"
    speak(message, text_widget)
    
    confirmation = takeCommand()
    if confirmation.lower() in ["yes", "yeah"]:
        funny_messages = [
            "Alright, see you on the other side. Did you know that the first computer virus was created in 1983?",
            "Got it, restarting now. Did you know that the first webcam was created to monitor a coffee pot at the University of Cambridge?",
            "Ok sir, meet you on the flip side. Did you know that the first smartphone was invented in 1992 by IBM?",
            "No problem, restarting now. Did you know that the first computer programmer was a woman named Ada Lovelace?",
            "Sure thing, see you soon. Did you know that the first domain name ever registered was symbolics.com in 1985?"
        ]
        funny_message = random.choice(funny_messages)
        speak(funny_message, text_widget)
        print(funny_message)
        os.system("shutdown /r /t 5")
    else:
        funny_messages = [
            "No worries, let's keep working. Did you know that a group of penguins in the water is called a raft?",
            "Alright, back to work. Did you know that the world's oldest piece of chewing gum is over 9,000 years old?",
            "Got it, let's continue. Did you know that a group of hedgehogs is called a prickle?",
            "Sure thing, let's keep going. Did you know that the longest wedding veil on record was over 20 feet long?",
            "Ok sir, let's keep working. Did you know that the world's largest snow maze is over 91,000 square feet?"
        ]
        funny_message = random.choice(funny_messages)
        speak(funny_message, text_widget)
        print(funny_message)

# Window automation: Open basic applications
# NotePad
def open_notepad():
    """
    Opens Notepad application.
    """
    speak("Opening Notepad.", text_widget)
    os.system("start notepad.exe")
#Word
def open_word():
    """
    Opens Microsoft Word application.
    """
    speak("Opening Word.", text_widget)
    os.system("start winword.exe")
#Excel
def open_excel():
    """
    Opens Microsoft Excel application.
    """
    speak("Opening Excel.", text_widget)
    os.system("start excel.exe")
#PowerPoint
def open_powerpoint():
    """
    Opens Microsoft PowerPoint application.
    """
    speak("Opening PowerPoint.", text_widget)
    os.system("start powerpnt.exe")
#Paint
def open_paint():
    """
    Opens Microsoft Paint application.
    """
    speak("Opening Paint.", text_widget)
    os.system("start mspaint.exe")
#Calculator
def open_calc():
    """
    Opens Calculator application.
    """
    speak("Opening Calculator.", text_widget)
    os.system("start calc.exe")
#Cmd
def open_cmd():
    """
    Opens Command Prompt application.
    """
    speak("Opening Command Prompt.", text_widget)
    os.system("start cmd.exe")
#Photos
def open_photos():
    """
    Opens Photos application.
    """
    speak("Opening Photos.", text_widget)
    os.system("start ms-photos://")


#Windows Automation: Check Battery Level
def check_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if plugged:
        message = "Your battery is currently charging, and the battery level is at " + str(percent) + "%."
    else:
        message = "Your battery is currently not charging, and the battery level is at " + str(percent) + "%."

    # Random funny comment
    funny_comments = ["Don't forget to feed your battery with electricity!",
                      "I hope your battery isn't running on fumes.",
                      "Your battery level is over 9000!",
                      "Your battery is doing great, keep it up!"]
    message += " " + random.choice(funny_comments)
    print(message)
    speak(message, text_widget)

#Windows Automation: Taking ScreenShot
def take_screenshot():
    """
    Takes a screenshot and saves it to the Windows default screenshot folder.
    """
    speak("What would you like to name the screenshot?", text_widget)
    name = takeCommand().lower()
    img = pyautogui.screenshot()
    screenshot_folder = os.path.join(os.environ["USERPROFILE"], "Pictures", "Screenshots")
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
    screenshot_path = os.path.join(screenshot_folder, f"{name}.png")
    img.save(screenshot_path)
    speak(f"Screenshot saved as {name}", text_widget)
    
    # Open the screenshot
    os.startfile(screenshot_path)

#email
 # Define function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('urbanmonkeygiveaway@gmail.com', 'akshay4ever')
    server.sendmail('urbanmonkeygiveaway@gmail.com', to, content)
    server.close()

def send_email():
    try:
        # Get the recipient's email address
        speak("To whom would you like to send the email?", text_widget)
        to = takeCommand()

        # Confirm the recipient's email address
        speak(f"Is this the correct email address, {to}?", text_widget)
        confirm = takeCommand()
        if 'yes' not in confirm.lower():
            speak("Please provide the correct email address.", text_widget)
            to = takeCommand()

        # Get the email content
        speak("What should I say?")
        content = takeCommand()

        # Confirm the email content
        speak(f"Is this the email content you would like to send: {content}?", text_widget)
        confirm = takeCommand()
        if 'yes' not in confirm.lower():
            speak("Please provide the email content.", text_widget)
            content = takeCommand()

        # Send the email
        sendEmail(to, content)
        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry. I am not able to send this email.", text_widget)


#Calculator
def calculator(query):
    arithmetic = query.lower().replace("jarvis", "").replace("calculate", "")
    if "plus" in arithmetic or "add" in arithmetic or "+" in arithmetic:
        operands = re.findall(r'\d+', arithmetic)
        if len(operands) != 2:
            speak("Sorry, I did not understand that arithmetic expression.", text_widget)
            return
        result = int(operands[0]) + int(operands[1])
        speak(f"The sum of {operands[0]} and {operands[1]} is {result}", text_widget)
    elif "minus" in arithmetic or "subtract" in arithmetic or "-" in arithmetic:
        operands = re.findall(r'\d+', arithmetic)
        if len(operands) != 2:
            speak("Sorry, I did not understand that arithmetic expression.", text_widget)
            return
        result = int(operands[0]) - int(operands[1])
        speak(f"The difference of {operands[0]} and {operands[1]} is {result}", text_widget)
    elif "multiply" in arithmetic or "product" in arithmetic or "*" in arithmetic or "into" in arithmetic:
        operands = re.findall(r'\d+', arithmetic)
        if len(operands) != 2:
            speak("Sorry, I did not understand that arithmetic expression.", text_widget)
            return
        result = int(operands[0]) * int(operands[1])
        speak(f"The product of {operands[0]} and {operands[1]} is {result}", text_widget)
    elif "divide" in arithmetic or "/" in arithmetic:
        operands = re.findall(r'\d+', arithmetic)
        if len(operands) != 2:
            speak("Sorry, I did not understand that arithmetic expression.", text_widget)
            return
        result = int(operands[0]) / int(operands[1])
        speak(f"The division of {operands[0]} and {operands[1]} is {result}", text_widget)
    elif "percentage" in arithmetic or "percent" in arithmetic:
        operands = re.findall(r'\d+', arithmetic)
        if len(operands) != 2:
            speak("Sorry, I did not understand that arithmetic expression.", text_widget)
            return
        result = (int(operands[0]) * int(operands[1])) / 100
        speak(f"The {operands[0]} percent of {operands[1]} is {result}", text_widget)
    else:
        speak("Sorry, I did not understand that arithmetic expression.", text_widget)

#Google Search
def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("google search","")
    query = query.replace("how to","")
    query = query.replace("what do you mean by","")

    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    response = requests.get(search_url)

    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    results_text = ""

    for result in search_results:
        results_text += result.text

    summary = results_text.split('.')[0] + '.' + results_text.split('.')[1] + '.'
    speak(f"According to your search: {summary}", text_widget)

def typing_mode():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    fs = 16000   # sampling rate
    duration = 5 # seconds per recording

    newline = True
    engine.say("Typing mode enabled")
    engine.runAndWait()

    while True:
        print("🎙️ Listening for typing input...")
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        wavio.write("temp_type.wav", audio_data, fs, sampwidth=2)

        try:
            with sr.AudioFile("temp_type.wav") as source:
                audio = r.record(source)
            query = r.recognize_google(audio, language='en-US')
            print(f"You said: {query}")

            # punctuation & commands
            if 'pause' in query.lower():
                engine.say("Alright, I am done typing for you. That was fun! Bye bye!")
                engine.runAndWait()
                break
            elif 'full stop' in query.lower() or 'period' in query.lower():
                pyautogui.typewrite('.')
            elif 'comma' in query.lower():
                pyautogui.typewrite(',')
            elif 'at the rate' in query.lower():
                pyautogui.typewrite('@')
            elif 'new line' in query.lower() and len(query.split()) == 2:
                newline = True
            else:
                if newline:
                    pyautogui.typewrite(query.capitalize())
                    newline = False
                else:
                    pyautogui.typewrite(" " + query)

        except sr.UnknownValueError:
            print("❌ Could not understand speech.")
        except Exception as e:
            print(f"⚠️ Error in typing_mode: {e}")

def record_audio(filename="temp.wav", duration=5, fs=16000):
    """Record audio from microphone using sounddevice and save to file."""
    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    return filename

def open_camera():
    """
    Opens Camera application and allows voice-controlled actions:
    - 'click photo' to take a screenshot
    - 'close camera' or 'exit camera' to close the app
    """
    speak("Opening Camera.")
    os.system("start explorer shell:appsfolder\\Microsoft.WindowsCamera_8wekyb3d8bbwe!App")

    r = sr.Recognizer()
    time.sleep(5)  # wait for camera to open

    speak("Camera is ready. Say 'click photo' to take a picture or 'close camera' to exit.")

    while True:
        try:
            # Record audio using sounddevice
            filename = record_audio(duration=4)  # 4-second listen chunks

            # Recognize using speech_recognition
            with sr.AudioFile(filename) as source:
                audio = r.record(source)
            query = r.recognize_google(audio, language='en-US')
            print(f"You said: {query}")

            # Process commands
            cmd = query.lower()
            if 'click photo' in cmd:
                speak("Taking photo in 3 seconds.")
                time.sleep(3)
                pyautogui.press('space')  # simulates camera click
                speak("Photo clicked!")

            elif 'close camera' in cmd or 'exit camera' in cmd:
                speak("Closing Camera.")
                pyautogui.hotkey('alt', 'f4')
                break

            else:
                speak("Sorry, I didn't understand. Say 'click photo' or 'close camera'.")

        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("I didn't catch that, please repeat.")

        except Exception as e:
            print(f"Error: {e}")
            speak(f"An error occurred: {str(e)}")
            break 

#JokeApi
def ai_joke():
    """
    Tells a joke about AI ruling the world using JokeAPI.
    """
    # Make API request
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "type": "twopart",
        "blacklistFlags": "religious,political,racist,sexist"
    }
    response = requests.get(url, params=params)
    
    # Parse API response
    data = response.json()
    setup = data['setup']
    punchline = data['delivery']
    
    speak(f"Here's a joke for you, sir. {setup} {punchline}.")
    engine.runAndWait()



# import openai
# import openai_secret_manager
# def chat_gpt_mode():
#     """
#     Activates Chat GPT mode for virtual assistant.
#     """
#     try:
#         secrets = openai_secret_manager.get_secret("openai")

#         api_key = secrets["YOUR_OPENAI_API_KEY"]
#         model_engine = secrets["model_engine"]

#         speak("Activating Chat GPT mode.")
#         while True:
#             # Listening
#             query = takeCommand()

#             # Recognizing
#             if "pause" in query.lower():
#                 speak("Disabling Chat GPT mode.")
#                 break
#             else:
#                 try:
#                     openai.api_key = api_key
#                     response = openai.Completion.create(
#                         engine=model_engine,
#                         prompt=query,
#                         max_tokens=60,
#                         n=1,
#                         stop=None,
#                         temperature=0.7,
#                     )
#                     message = response.choices[0].text.strip()
#                     speak(message)
#                 except openai.error.RateLimitError:
#                     speak("Sorry, your quota is ending. Disabling Chat GPT mode.")
#                     break
#                 except Exception as e:
#                     speak(f"Sorry, I am not able to understand. {str(e)}")
#                     continue
#     except Exception as e:
#         speak(f"Sorry, some error occurred. {str(e)}")

#copy Function
def copy_things():
    pyautogui.hotkey('ctrl', 'c')
    speak("copied.")

#paste Function
def paste_things():
    pyautogui.hotkey('ctrl', 'v')
    speak("Pasted.")

#Cut_things function 
def cut_things():
    pyautogui.hotkey('ctrl', 'x')
    speak("done")

#Tossing a Coin
def toss_coin():
    """
    Simulates a coin toss.
    Returns 'Heads' or 'Tails'.
    """
    result = random.choice(['Heads', 'Tails'])
    speak(result, text_widget)

#password authentication function
def authenticate_user():
    speak("This particular file is password protected.", text_widget)
    speak("Please enter your password to continue.", text_widget)
    password = "activate"
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    while True:
        pass_input = takeCommand()
        hashed_input = hashlib.sha256(pass_input.encode('utf-8')).hexdigest()
        if hashed_input == hashed_password:
            speak("Access granted.", text_widget)
            return True
        else:
            print(f"Listened password: {pass_input}") # print the password that was listened to
            speak("Access denied. Please try again.", text_widget)

#Medidation exercise function
def meditation_guide():
    # Set the duration of the meditation in seconds
    duration = 300  # 5 minutes
    
    # Define the meditation instructions
    instructions = [
        "Take a comfortable seated position with your spine straight and your feet on the floor.",
        "Close your eyes and take a deep breath in through your nose, filling your lungs with air.",
        "Hold the breath for a few seconds, and then exhale slowly through your mouth, releasing all the air from your lungs.",
        "Repeat this deep breathing pattern, inhaling through your nose and exhaling through your mouth.",
        "As you continue to breathe deeply, focus your attention on your breath.",
        "If your mind wanders, gently bring it back to your breath without judgment.",
        "Continue breathing and focusing on your breath for the next few minutes."
    ]
    
    # Start the meditation guide
    speak("Let's begin the meditation exercise.", text_widget)
    time.sleep(1)
    
    for instruction in instructions:
        speak(instruction, text_widget)
        time.sleep(5)  # Pause for 5 seconds between instructions
    
    # Start the meditation timer
    speak("Now, let's meditate for the next 5 minutes.", text_widget)
    start_time = time.time()
    end_time = start_time + duration
    
    while time.time() < end_time:
        time_remaining = end_time - time.time()
        minutes, seconds = divmod(time_remaining, 60)
        timer_message = f"Time remaining: {int(minutes)} minutes {int(seconds)} seconds."
        speak(timer_message, text_widget)
        time.sleep(30)  # Update the timer every 30 seconds
    
    # End the meditation
    speak("The meditation exercise is now over. Take a moment to notice how you feel.", text_widget)

#Quitting function
def exit_jarvis():
    cool_messages = [
        "See you later, alligator!",
        "Hasta la vista, baby!",
        "Catch you on the flip side!",
        "Adios, amigo!",
        "Until next time, my friend!",
    ]
    message = random.choice(cool_messages)
    speak(message)
    exit()


####################################################################################################################
# Features End Here 
####################################################################################################################

def run_jarvis():
    # Password authentication
    if authenticate_user():
        # Call the speak function from JARVIS
        speak("Activating........", text_widget)
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            speak("Good morning!", text_widget)
        elif hour >= 12 and hour < 18:
            speak("Good afternoon!", text_widget)
        else:
            speak("Good evening!", text_widget)

        speak("I am Jarvis. How may I assist you?", text_widget)

        while True:
            query = takeCommand().lower()
            log_query(query)

            # Search Wikipedia
            if 'wikipedia' in query:
                speak('Searching Wikipedia...', text_widget)
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:", text_widget)
                speak(results, text_widget)

            # Open website
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("Opening YouTube...", text_widget)

            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("Opening Google...", text_widget)

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
                speak("Opening Stack Overflow...", text_widget)
            
            #googleSearch
            elif 'google search' in query:
                GoogleSearch(query)

            # Play a song
            elif 'play' in query:
                play_song()


            # Get the time
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}", text_widget)

            # Send email
            elif 'send email' in query:
                send_email()
            
            #Know weather
            elif 'weather' in query:
                run_get_weather()
            
            #Recipies
            elif 'how to cook' in query:
                dish = query.lower().replace("jarvis","").replace("how to cook ","")
                how_to_make(dish)

            #Youtube Search
            elif 'youtube search' in query:
                YouTubeSearch(query)
        
            #Whatsapp Message
            elif 'whatsapp message' in query:
                send_whatsapp_message()
            

            #Window Automation: Shut Down
            elif 'shutdown the system' in query:
                shut_down()
            
            #Window Automation : Restart
            elif "restart the system" in query:
                restart()
            
            #Window Automation : Checking Battery Level
            elif "check battery level" in query:
                check_battery()
            
            #Window Automation: ScreenShot
            elif "take screenshot" in query:
                take_screenshot()

            # Window automation: Open basic applications
            # NotePad
            elif "open notepad" in query:
                open_notepad()
            # Word
            elif "open word" in query:
                open_word()
            #Excel
            elif "open excel" in query:
                open_excel()
            #PowerPoint
            elif "open powerpoint" in query:
                open_powerpoint()
            #Paint
            elif "open paint" in query:
                open_paint()
            #Calculator
            elif "open calculator" in query:
                open_calc()
            #cmd
            elif "open cmd" in query:
                open_cmd()
            #Photos
            elif "open photos" in query:
                open_photos()
            elif "open camera" in query:
                open_camera()
            
            #Window Automation: Closing Applications like chrome, brave, notepad, word, excel, powerpoint, paint, calculator and cmd
            elif "close" in query:
                pyautogui.hotkey('alt', 'f4')
            
            # elif"chat gpt mode" in query:
            #     chat_gpt_mode()
            elif "copy" in query:
                copy_things()
            elif"cut" in query:
                cut_things()
            elif"paste"in query:
                paste_things()
            elif"type mode" in query:
                typing_mode()
            elif"toss coin" in query:
                toss_coin()
            #Calculator
            elif"calculate" in query:
                calculator(query)
            # Meditation Guide
            elif 'meditation guide' in query:
                meditation_guide(text_widget)
            #exiting from jarvis
            elif any(word in query.lower() for word in ["close", "exit", "bye"]):
                exit_jarvis()
            

            # Chat with Jarvis & logging Unhandled queries for future
            elif True:
                handled = False
                for i in range(len(patterns)):
                    for j in range(len(patterns[i])):
                        if patterns[i][j] in query:
                            response = random.choice(responses[i])
                            speak(response, text_widget)
                            handled = True
                            break
                    if handled:
                        break
                if not handled:
                    log_unhandled_query(query)
                    speak("Sorry, I am not programmed to handle that yet. I have logged your query and will work on adding the functionality in the future.", text_widget)
        

    


# Button to start Jarvis
button = Button(
    window,
    text="Start JARVIS",
    bg="#4CAF50",
    fg="#FFFFFF",
    command=lambda: threading.Thread(target=run_jarvis).start()
)
button.place(x=50.0, y=320.0, width=120.0, height=35.0)

# # Text entry for user input
# entry_widget = Text(
# window,
# wrap="word",
# font=("Helvetica", 12),
# bg="#D9D9D9",
# relief="flat",
# state='normal'
# )
# entry_widget.place(x=190, y=320, width=500, height=35)

# def get_input():
#     # Get the user input from the entry widget
#     user_input = entry_widget.get("1.0", "end-1c")
#     # Clear the entry widget
#     entry_widget.delete("1.0", END)
#     # Return the user input
#     return user_input

# submit_button = Button(
#     window,
#     text="Submit",
#     bg="#4CAF50",
#     fg="#FFFFFF",
#     command=get_input
#     )
# submit_button.place(x=700, y=320, width=80, height=35)

window.mainloop()







