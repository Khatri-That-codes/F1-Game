import tkinter as tk
import theme
from tkinter import font
from theme.colour_palette import styled_text, team_colours, F1_RED, F1_MUTED_TEXT
from src.sound_manager import SoundManager

def show_race_intro_screen(root, track, race_number, total_races, drivers, on_start_race):
    """
    Display the Race Intro Broadcast Screen.

    Args:
        root (tk.Tk): The root Tkinter window.
        track (dict): Track information including name and ASCII map.
        race_number (int): Current race number.
        total_races (int): Total number of races in the season.
        drivers (list): List of drivers with their teams.
        on_start_race (function): Callback for the "Start Race" button.
    """
    # Create a new frame for the race intro screen
    intro_frame = tk.Frame(root, bg="black")
    intro_frame.pack(fill="both", expand=True)

    # Create a monospaced font
    mono_font = font.Font(family="Courier", size=12, weight="bold")
    large_font = font.Font(family="Courier", size=18, weight="bold")

    # Display track name
    track_label = tk.Label(
        intro_frame,
        text=styled_text(track['name'], F1_RED, bold=True),
        bg="black",
        fg="white",
        font=large_font,
    )
    track_label.pack(pady=10)

    # Display ASCII map
    track_map_label = tk.Label(
        intro_frame,
        text=track['ascii_map'],
        bg="black",
        fg="white",
        font=mono_font,
        justify="left",
    )
    track_map_label.pack(pady=10)

    # Display race number
    race_number_label = tk.Label(
        intro_frame,
        text=f"Race {race_number} of {total_races}",
        bg="black",
        fg="white",
        font=mono_font,
    )
    race_number_label.pack(pady=5)

    # Display driver list
    driver_list_frame = tk.Frame(intro_frame, bg="black")
    driver_list_frame.pack(pady=10)
    for driver in drivers:
        driver_label = tk.Label(
            driver_list_frame,
            text=f"{driver['name']} ({driver['team']})",
            fg=team_colours().get(driver['team'], F1_MUTED_TEXT),
            bg="black",
            font=mono_font,
        )
        driver_label.pack(anchor="w")

    # Countdown animation
    countdown_label = tk.Label(
        intro_frame,
        text="",
        bg="black",
        fg="white",
        font=large_font,
    )
    countdown_label.pack(pady=20)

    sound_manager = SoundManager()
    sound_manager.play_engine_loop()

    def countdown(step):
        if step > 0:
            countdown_label.config(text=str(step))
            sound_manager.play_effect("beep")
            root.after(1000, countdown, step - 1)
        else:
            countdown_label.config(text="Lights Out!")
            sound_manager.stop_engine_loop()
            sound_manager.play_effect("cheer")

    countdown(3)

    # Start Race button
    start_button = tk.Button(
        intro_frame,
        text="Start Race",
        command=lambda: [intro_frame.destroy(), on_start_race()],
        bg="gray",
        fg="white",
        font=mono_font,
    )
    start_button.pack(pady=20)

# Example usage
if __name__ == "__main__":
    def mock_start_race():
        print("Starting the race...")

    mock_track = {
        "name": "Monza",
        "ascii_map": (
            "          ╭──────────────╮        \n"
            "        ╭─╯              ╰─╮      \n"
            "      ╭─╯   Variante      ╰─╮     \n"
            "      │     del Rettifilo   │     \n"
            "      │                      │     \n"
            "      │                      │     \n"
            "      │   Lesmo     Ascari   │     \n"
            "      ╰─╮                ╭───╯     \n"
            "        ╰───────────────╯          "
        ),
    }

    mock_drivers = [
        {"name": "Verstappen", "team": "Red Bull"},
        {"name": "Hamilton", "team": "Mercedes"},
        {"name": "Leclerc", "team": "Ferrari"},
    ]

    root = tk.Tk()
    show_race_intro_screen(root, mock_track, 3, 23, mock_drivers, mock_start_race)
    root.mainloop()