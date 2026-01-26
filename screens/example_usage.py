from commentary_playback_controller import CommentaryPlaybackController

if __name__ == "__main__":
    commentary = [
        "The race is about to begin!",
        "And they're off! What a fantastic start!",
        "Oh no, there's been a crash at turn 3!",
        "The stewards are investigating the incident.",
        "What an incredible overtake on the final lap!",
        "And the race is over! What a thrilling finish!"
    ]

    playback_controller = CommentaryPlaybackController(delay=2.0)
    playback_controller.play_commentary(commentary)