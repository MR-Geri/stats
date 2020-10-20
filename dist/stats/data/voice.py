from random import choice

import pyttsx3

tts = pyttsx3.init()
tts.setProperty('voice', "ru")


def take_a_break():
    phrases = ['Пора пройтись.', 'Сделайте попить.', 'Время сделать чай.', 'Сделайте зарядку.',
               'Смените положение.', 'Необходим перерыв.', 'Нужен отдых']
    tts.say(choice(phrases))
    tts.runAndWait()
