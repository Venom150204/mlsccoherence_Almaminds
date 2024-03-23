import speech_recognition as sr
import joblib
from gtts import gTTS
import pygame
import io
import pyttsx3

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
        continue

def main():
    # Load the trained model
    model_path = 'trained_model.joblib'
    model = load_model(model_path)
    if model is None:
        return

    # Provide a simple command-line interface
    print("Welcome to the Product Delivery System Chatbot!")
    while True:
        instruction = speech_to_text()
        if instruction is None:
            continue
        if instruction.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(model, instruction)
        if response:
            print("Bot:", response)
            text_to_speech(response)
        else:
            print("Bot: Sorry, I couldn't process your request.")

if __name__ == "__main__":
    main()
