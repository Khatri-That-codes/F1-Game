import tkinter as tk
from tkinter import font
import theme
from theme import styled_text, team_colours, F1_RED

class TrackAsciiAnimator:
    def __init__(self, root, track_ascii, drivers, speed=500):
        """
        Initialize the TrackAsciiAnimator.

        Args:
            root (tk.Tk): The root Tkinter window.
            track_ascii (str): ASCII representation of the track.
            drivers (list): List of drivers with their teams and positions.
            speed (int): Animation speed in milliseconds.
        """
        self.root = root
        self.track_ascii = track_ascii.split("\n")
        self.drivers = drivers
        self.speed = speed

        # Create a frame for the track animation
        self.track_frame = tk.Frame(root, bg="black")
        self.track_frame.pack(fill="both", expand=True)

        # Create a monospaced font
        self.mono_font = font.Font(family="Courier", size=12, weight="bold")

        # Create a label to display the track
        self.track_label = tk.Label(
            self.track_frame,
            text="",
            bg="black",
            fg="white",
            font=self.mono_font,
            justify="left",
        )
        self.track_label.pack(pady=10)

    def draw_track(self, driver_positions):
        """
        Draw the track with driver markers.

        Args:
            driver_positions (dict): Dictionary mapping driver names to positions (row, col).
        """
        track_copy = self.track_ascii.copy()

        # Place driver markers on the track
        for driver, (row, col) in driver_positions.items():
            team = next(d["team"] for d in self.drivers if d["name"] == driver)
            marker = styled_text("🏎", team_colours().get(team, "white"))
            track_copy[row] = track_copy[row][:col] + marker + track_copy[row][col + 1:]

        # Update the track label
        self.track_label.config(text="\n".join(track_copy))

    def animate(self, driver_positions_callback):
        """
        Animate the track with driver positions.

        Args:
            driver_positions_callback (function): Function that returns updated driver positions.
        """
        driver_positions = driver_positions_callback()
        self.draw_track(driver_positions)
        self.root.after(self.speed, self.animate, driver_positions_callback)

# Example usage
if __name__ == "__main__":
    def mock_driver_positions():
        """Mock function to simulate driver positions."""
        from random import randint
        return {
            "Verstappen": (3, randint(10, 30)),
            "Hamilton": (4, randint(10, 30)),
            "Leclerc": (5, randint(10, 30)),
        }

    mock_track = (
        "          ╭──────────────╮        \n"
        "        ╭─╯              ╰─╮      \n"
        "      ╭─╯   Variante      ╰─╮     \n"
        "      │     del Rettifilo   │     \n"
        "      │                      │     \n"
        "      │                      │     \n"
        "      │   Lesmo     Ascari   │     \n"
        "      ╰─╮                ╭───╯     \n"
        "        ╰───────────────╯          "
    )

    mock_drivers = [
        {"name": "Verstappen", "team": "Red Bull"},
        {"name": "Hamilton", "team": "Mercedes"},
        {"name": "Leclerc", "team": "Ferrari"},
    ]

    root = tk.Tk()
    animator = TrackAsciiAnimator(root, mock_track, mock_drivers, speed=1000)
    animator.animate(mock_driver_positions)
    root.mainloop()