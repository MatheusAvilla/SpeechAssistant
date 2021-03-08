import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import requests
import json
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="pt-BR")
        except sr.UnknownValueError:
            alexis_speak("Desculpe, não entendi.")
        except sr.RequestError:
            alexis_speak("Desculpe, meu serviço de fala não funcionou.")
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang="pt-BR")
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def is_weather_search_action(voice_data):
    text = voice_data.lower()
    return "Qual é a temperatura em" in text

def extract_city_name_for_weather_action(voice_data):
    text = voice_data.lower()
    return text.replace("Qual é a temperatura em","").strip()

def respond(voice_data):
    if 'me diga seu nome' in voice_data:
        alexis_speak('Meu nome é Alexis')
    if 'tempo' in voice_data:
        alexis_speak(ctime())
    if 'pesquisar' in voice_data:
        search = record_audio('O que voce deseja pesquisar?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Aqui está o que eu encontrei sobre ' + search)
    if 'encontrar local' in voice_data:
        location = record_audio('Qual é a localização?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Aqui está a localização de ' + location)
    if 'assistir' in voice_data:
        video = record_audio('Quais vídeos?')
        url = 'https://youtube.com/results?search_query=' + video 
        webbrowser.get().open(url)
        alexis_speak('Aqui está seus vídeos sobre ' + video)
    if "obrigado" in voice_data:
        alexis_speak('Disponha.')
    if 'sair' in voice_data:
        alexis_speak('Fico feliz em poder ajudar.')
        exit()

time.sleep(1)
alexis_speak('Como posso te ajudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)