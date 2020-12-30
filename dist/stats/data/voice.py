from random import choice
import pyttsx3

tts = pyttsx3.init()
tts.setProperty('voice', "ru")


def take_random(phrases=None):
    phrases = ['Проверка'] if phrases is None else phrases
    tts.say(choice(phrases))
    tts.runAndWait()
