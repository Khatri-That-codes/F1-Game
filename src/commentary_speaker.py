'''
Module for handling commentary speech synthesis.
'''

import pyttsx3
import threading

class CommentarySpeaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.lock = threading.Lock()

    def speak(self, text: str):
        def _speak():
            with self.lock:
                self.engine.say(text)
                self.engine.runAndWait()

        thread = threading.Thread(target=_speak)
        thread.start()