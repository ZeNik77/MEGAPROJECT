import os
import sys
from vosk import Model, KaldiRecognizer
import pyaudio
import pymorphy2
from config import *
from gtts import gTTS
import playsound
import random
import wikipedia
import translators as ts

morph = pymorphy2.MorphAnalyzer()


class VoiceAssistant:
    def __init__(self):
        self.commands = [[['тест'], self.test], [['завершить работа'], self.turn_off],
                         [['что такой', 'что значит'], self.explain]]
        self.active = False
        self.name = name
        self.changename_flg = False

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
        print(term)
        self.speak('Момент.')
        self.speak(self.wikisearch(term))

    def analyze(self, data):
        text = eval(data)['text']
        if text:
            text_inf = [morph.parse(i)[0].normal_form for i in text.split()]
            print(text_inf)
            text_inf = ' '.join(text_inf)
            first_word = text_inf.split()[0]
            if self.active:
                for i in self.commands:
                    for j in i[0]:
                        if text_inf.startswith(j):
                            i[1](text_inf.replace(j, ''))
            if self.changename_flg:
                with open('config.py', 'r', encoding='utf-8') as file:
                    old = file.read()
                new = old.replace(self.name, first_word)
                with open('config.py', 'w', encoding='utf-8') as file:
                    file.write(new)
                self.name = first_word
                self.speak('Теперь мое имя' + self.name)
                self.changename_flg = False
            elif text_inf == self.name:
                self.active = True
                self.name_react()
            elif 'сменить' in text_inf.split() and 'имя' in text_inf.split():
                phrases = ['Выберите новое имя.']
                self.speak(random.choice(phrases))
                self.changename_flg = True
            elif text_inf.startswith(self.name):
                self.react(text_inf.replace(self.name, ''))
            else:
                self.active = False

    def name_react(self):
        phrases = ['Чем могу помочь?', 'Чем могу быть полезна?', 'Да?', 'Слушаю вас.']
        self.speak(random.choice(phrases))

    def react(self, text):
        self.speak(text)


if __name__ == '__main__':
    v = VoiceAssistant()
    v.start()
