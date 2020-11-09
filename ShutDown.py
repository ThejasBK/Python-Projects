import os
import pyttsx3
import speech_recognition as sr

class listener:
    def takeCommands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Litening')
            r.phase_threshold = 0.7
            audio = r.listen(source)
            try:
                print('Recognizing')
                query = r.recognize_google(audio, language = 'en-in')
                print(audio)
            except Exception as e:
                print(e)
                print('Say it again')
                return 'None'
        return query

    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1],id)
        engine.say(audio)
        engine.runAndWait()

    def quitSelf(self):
        self.Speak('Do you wish off the computer sir')
        take = self.takeCommands()
        choice = take
        if 'yes' in choice:
            print('Shutting down the system')
            self.Speak('Shutting down the system')
            os.system('shutdown /s /t 30')
        if 'no' in choice:
            print('Thank you sir')
            self.Speak('Thank you sir')

if __name__ == '__main__':
    maam = listener()
    maam.quitSelf()
