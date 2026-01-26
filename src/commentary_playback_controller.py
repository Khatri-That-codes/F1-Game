'''
This file controls the playback of commentary during the race
'''

import time
import threading
from commentary_speaker import CommentarySpeaker
class CommentaryPlaybackController:
    def __init__(self, delay: float = 5.0):
        self.delay = delay
        self.speaker = CommentarySpeaker()

    def play_commentary(self, commentary_list):
        def _play():
            for commentary in commentary_list:
                print(f"Speaking: {commentary}")  # Debugging log
                self.speaker.speak(commentary)
                self.speaker.queue.join()  # Wait for the current commentary to finish
                print(f"Finished: {commentary}")  # Debugging log
                time.sleep(self.delay)

        thread = threading.Thread(target=_play)
        thread.start()