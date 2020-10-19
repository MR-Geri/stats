from random import choice

import pyttsx3
from threading import Thread

tts = pyttsx3.init()
tts.setProperty('voice', "ru")
run = Thread(target=lambda: tts.runAndWait())


def take_a_break():
    phrases = ['Пора пройтись.', 'Сделайте попить.', 'Время сделать чай.', 'Сделайте зарядку.',
               'Смените положение.', 'Необходим перерыв.', 'Нужен отдых']
    tts.say(choice(phrases))
    run.start()
