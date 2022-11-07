import sys
from vosk import Model, KaldiRecognizer
import pyaudio
import pymorphy2
from gtts import gTTS
import playsound

morph = pymorphy2.MorphAnalyzer()


class VoiceAssistant:
    def __init__(self):
        self.commands = {'тест': self.test, 'завершить работа': self.turn_off}

    def test(self, text):
        print('test!')
        self.speak('test!', 'ru')

    def turn_off(self, text):
        self.speak('WHERE IS YOUR MOTIVATION?', 'en')
        sys.exit(0)

    def start(self):
        model = Model('rumodel')
        recognizer = KaldiRecognizer(model, 16000)
        cap = pyaudio.PyAudio()
        stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        print('started')
        while 1:
            data = stream.read(4096)
            # if len(data) == 0:
            #    break
            if recognizer.AcceptWaveform(data):
                self.analyze(recognizer.Result())

    def speak(self, text, lang):
        tts = gTTS(text=text, lang=lang)
        b = 'speech.mp3'
        tts.save(b)
        playsound.playsound(b)

    def analyze(self, data):
        text = eval(data)['text']
        text = [morph.parse(i)[0].normal_form for i in text.split()]
        print(text)
        text = ' '.join(text)
        for i in self.commands.keys():
            if text.startswith(i):
                self.commands[i](text)


if __name__ == '__main__':
    v = VoiceAssistant()
    v.start()
