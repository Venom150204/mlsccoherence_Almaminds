from flask import Flask, render_template, request
import speech_recognition as sr
import joblib
from gtts import gTTS
import pygame
import io

app = Flask(__name__)

# Global variable to keep track of speech output status
speech_playing = False

def load_model(model_path):
    """
    Load the trained model from the provided file path.
    """
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print("Error loading the model:", e)
        return None

def get_response(model, instruction):
    """
    Get the response from the trained model for the given instruction.
    """
    try:
        response = model.predict([instruction])
        return response[0]
    except Exception as e:
        print("Error predicting response:", e)
        return None

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=1)

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return None

def text_to_speech(response):
    # Convert text to speech using Google Text-to-Speech
    tts = gTTS(text=response, lang='en')
    speech_stream = io.BytesIO()
    tts.write_to_fp(speech_stream)
    speech_stream.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(speech_stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if not speech_playing:
            pygame.mixer.music.stop()
            break
        continue

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    global speech_playing
    speech_playing = True
    model_path = 'trained_model.joblib'
    model = load_model(model_path)
    if model is None:
        return "Error: Model not loaded"

    instruction = speech_to_text()
    if instruction is None:
        return "Error: Could not understand audio"

    response = get_response(model, instruction)
    if response:
        text_to_speech(response)
        speech_playing = False
        return response
    else:
        speech_playing = False
        return "Error: No response generated"

@app.route('/stop_audio', methods=['POST'])
def stop_audio():
    global speech_playing
    speech_playing = False
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
