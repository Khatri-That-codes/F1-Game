import os
import pygame.mixer

class SoundManager:
    def __init__(self, sound_folder="assets/sounds"):
        """Initialize the SoundManager and pygame.mixer."""
        self.sound_folder = sound_folder
        self.engine_channel = None
        self.sounds = {}

        # Initialize pygame.mixer safely
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Preload sound effects
        self._load_sounds()

    def _load_sounds(self):
        """Load all sound files from the sound folder."""
        for file_name in os.listdir(self.sound_folder):
            if file_name.endswith(".wav") or file_name.endswith(".mp3"):
                sound_name = os.path.splitext(file_name)[0]
                self.sounds[sound_name] = pygame.mixer.Sound(os.path.join(self.sound_folder, file_name))

    def play_engine_loop(self):
        """Play the engine loop sound."""
        if "engine" in self.sounds:
            if self.engine_channel is None or not self.engine_channel.get_busy():
                self.engine_channel = self.sounds["engine"].play(loops=-1)

    def stop_engine_loop(self):
        """Stop the engine loop sound."""
        if self.engine_channel is not None:
            self.engine_channel.stop()
            self.engine_channel = None

    def play_effect(self, name):
        """Play a one-shot sound effect."""
        if name in self.sounds:
            self.sounds[name].play()

# Example usage
if __name__ == "__main__":
    sound_manager = SoundManager()

    # Play engine loop
    sound_manager.play_engine_loop()

    # Play a one-shot effect
    sound_manager.play_effect("collision")

    # Stop engine loop
    sound_manager.stop_engine_loop()