'''
Module for handling commentary speech synthesis.
'''
import pyttsx3
import threading
import queue

class CommentarySpeaker:
    def __init__(self):
        self.engine = pyttsx3.init()  # Single engine instance
        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self._process_queue, daemon=True)
        self.thread.start()

    def _process_queue(self):
        while True:
            text = self.queue.get()  # Get text from the queue
            if text is None:  # Exit signal
                break
            print(f"Processing: {text}")  # Debugging log
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                print(f"Error speaking text: {e}")
            finally:
                self.queue.task_done()  # Ensure the queue continues processing
            print(f"Processed: {text}")  # Debugging log

    def speak(self, text: str):
        print(f"Queued: {text}")  # Debugging log
        self.queue.put(text)  # Add text to the queue

    def stop(self):
        self.queue.put(None)  # Send exit signal
        self.thread.join()
        self.engine.stop()  # Stop the engine when done