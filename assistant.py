import datetime
import os
import sqlite3
import sys

import plyer
from vosk import Model, KaldiRecognizer
import pyaudio
import pymorphy2
from config import *
from gtts import gTTS
import playsound
import random
import wikipedia
import translators as ts

f = {'первый': 1, 'второй': 2, 'третий': 3, 'четвёртый': 4, 'пятый': 5, 'шестой': 6, 'седьмой': 7, 'восьмой': 8,
     'девятый': 9}
o = {'двадцать': 20, 'тридцать': 30}
s = {'десятый': 10, 'одиннадцатый': 11, 'двенадцатый': 12, 'тринадцатый': 13, 'четырнадцатый': 14, 'пятнадцатый': 15,
     'шестнадцатый': 16,
     'семнадцатый': 17, 'восемнадцатый': 18, 'девятнадцатый': 19}

MONTHS = {'январь': 1,
          'февраль': 2,
          'март': 3,
          'апрель': 4,
          'май': 5,
          'июнь': 6,
          'июль': 7,
          'август': 8,
          'сентябрь': 9,
          'октябрь': 10,
          'ноябрь': 11,
          'декабрь': 12, }
morph = pymorphy2.MorphAnalyzer()


def word_to_number(txt):
    n = 0
    for i in s.keys():
        if i in txt:
            n += s[i]
    if not n:
        for i in o.keys():
            if i in txt:
                n += o[i]
        for i in f.keys():
            if i in txt:
                n += f[i]
    return n


class VoiceAssistant:
    def __init__(self):
        self.commands = [[['сказать'], self.test],
                         [['какой план', 'что запланировать', 'что будет'], self.events_check],
                         [['завершить работа'], self.turn_off],
                         [['что такой', 'что значит'], self.explain]]
        self.active = False
        self.last_notify = None
        self.name = name
        self.changename_flg = False
        self.request = None

    def events_check(self, text):
        num = word_to_number(text)
        for i in MONTHS.keys():
            if i in text:
                month = MONTHS[i]
        con = sqlite3.connect('Assets/Databases/main.sqlite3')
        cur = con.cursor()
        events = cur.execute(
            f"SELECT * FROM EVENTS").fetchall()
        self.speak('Перечисляю.')
        for i in events:
            if i[4] == month and i[5] == num:
                self.speak(i[1])

    def events_notify(self):
        con = sqlite3.connect('Assets/Databases/main.sqlite3')
        cur = con.cursor()
        events = cur.execute(
            f"SELECT * FROM EVENTS").fetchall()
        events.sort(key=lambda x: x[0])
        con.close()
        event_times = [datetime.datetime(i[3], i[4], i[5], i[6], i[7]) for i in events]
        now = datetime.datetime.now()
        timeleft = [(event_times[i].timestamp() - now.timestamp(), i) for i in range(len(event_times))]
        timeleft.sort()
        timeleft = list(filter(lambda i: i[0] >= 0, timeleft))
        for i in timeleft:
            if int(i[0]) == 3600 and self.last_notify != events[i[1]][1]:
                plyer.notification.notify(message=f'До {events[i[1]][1]} остался час.',
                                          title='Уведомление')
                self.last_notify = events[i[1]][1]

    def test(self, text):
        print('test!')
        self.speak('test!', 'ru')

    def turn_off(self, text):
        self.speak('WHERE IS YOUR MOTIVATION?', 'en')
        sys.exit(0)

    def start(self):
        model = Model('Assets/Models/rumodel')
        recognizer = KaldiRecognizer(model, 16000)
        cap = pyaudio.PyAudio()
        stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        print('started')
        while 1:
            self.events_notify()
            data = stream.read(4096, exception_on_overflow=False)
            # if len(data) == 0:
            #    break
            if recognizer.AcceptWaveform(data):
                self.analyze(recognizer.Result())

    def wikisearch(self, request):
        en_request = ts.google(request)
        title = wikipedia.search(en_request)
        try:
            page = wikipedia.page(title[0], auto_suggest=False).content.split('.')
        except wikipedia.DisambiguationError as e:
            s = e.options[0]
            page = wikipedia.page(s, auto_suggest=False).content.split('.')
        n = 3
        while len('.'.join(page[:n])) >= 300:
            n -= 1
        page = '.'.join(page[:n])
        return ts.google(page, to_language='ru')

    def speak(self, text, lang='ru'):
        tts = gTTS(text=text, lang=lang)
        b = 'Assets/Audio/speech.mp3'
        tts.save(b)
        playsound.playsound(b)
        os.remove(b)

    def explain(self, text):
        term = text
        phrases = ['Подождите секунду.', 'Момент.', 'Уже ищу.']
        self.speak(random.choice(phrases))
        self.speak(self.wikisearch(term))

    def analyze(self, data):
        print(self.active)
        text = eval(data)['text']
        if text:
            text_inf = [morph.parse(i)[0].normal_form for i in text.split()]
            print(text_inf)
            text_inf = ' '.join(text_inf)
            first_word = text_inf.split()[0]
            if self.request:
                self.request(text_inf)
                self.request = None
            elif self.active:
                self.react(text_inf)

            elif text_inf == self.name:
                self.active = True
                self.name_react()
            elif 'сменить' in text_inf.split() and 'имя' in text_inf.split():
                phrases = ['Выберите новое имя.']
                self.speak(random.choice(phrases))
                self.request = self.change_name
            elif text_inf.startswith(self.name):
                self.react(text_inf.replace(self.name, '', 1))
            else:
                self.active = False

    def change_name(self, text):
        first_word = text.split()[0]
        with open('config.py', 'r', encoding='utf-8') as file:
            old = file.read()
        new = old.replace(self.name, first_word)
        with open('config.py', 'w', encoding='utf-8') as file:
            file.write(new)
        self.name = first_word
        self.speak('Теперь мое имя' + self.name)
        self.changename_flg = False

    def name_react(self):
        phrases = ['Чем могу помочь?', 'Чем могу быть полезна?', 'Да?', 'Слушаю вас.']
        self.speak(random.choice(phrases))

    def react(self, txt):
        txt = txt.strip()
        for i in self.commands:
            for j in i[0]:
                if j in txt:
                    i[1](txt.replace(j, ''))
                    self.active = False


if __name__ == '__main__':
    v = VoiceAssistant()
    v.start()
