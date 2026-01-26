import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import tkinter as tk

from tkinter import ttk
from src.season import Season
from src.models import Driver, Track

from screens.results_screen import ResultsScreen

class RaceScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("F1 Race Simulator")

        # Title Label
        self.title_label = tk.Label(root, text="Race in Progress", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Commentary Label
        self.commentary_label = tk.Label(root, text="Click 'Start Race' to begin", wraplength=400, justify="center")
        self.commentary_label.pack(pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # Start Race Button
        self.start_button = tk.Button(root, text="Start Race", command=self.start_race)
        self.start_button.pack(pady=10)

    def start_race(self):
        # Disable the Start Race button and update its text
        self.start_button.config(text="Race in Progress", state="disabled")
        self.progress["value"] = 0  # Reset progress bar

        # Example teams
        teams = ["Team A", "Team B", "Team C"]

        # Initialize drivers with teams
        drivers = [
            Driver("Driver 1", teams[0]),
            Driver("Driver 2", teams[1]),
            Driver("Driver 3", teams[2])
        ]
        # Initialize tracks with required arguments
        tracks = [
            Track("Track 1", 5, 0.2),  # Added difficulty and weather_bias
            Track("Track 2", 7, 0.3)   # Added difficulty and weather_bias
        ]
        season = Season(drivers, tracks)

        # Run the next race
        results, commentary_log, incidents = season.run_next_race()

        # Update commentary and progress bar dynamically
        self.update_progress(commentary_log, results, incidents)

    def update_progress(self, commentary_log, results, incidents, index=0):
        if index < len(commentary_log):
            # Update commentary label
            self.commentary_label.config(text=commentary_log[index])

            # Update progress bar
            progress_value = (index + 1) / len(commentary_log) * 100
            self.progress["value"] = progress_value

            # Schedule the next update
            self.root.after(2000, self.update_progress, commentary_log, results, incidents, index + 1)
        else:
            # Race complete, switch to Results Screen
            from screens.results_screen import ResultsScreen
            for widget in self.root.winfo_children():
                widget.destroy()  # Clear the current screen
            ResultsScreen(self.root, results, incidents, 25, lambda: self.show_standings())

    def show_standings(self):
        from screens.standings_screen import StandingsScreen
        mock_standings = {
            "Driver 1": {"points": 50, "team": "Team A"},
            "Driver 2": {"points": 40, "team": "Team B"},
            "Driver 3": {"points": 30, "team": "Team C"}
        }
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear the current screen
        StandingsScreen(self.root, mock_standings, lambda: print("Next Race clicked!"))

if __name__ == "__main__":
    root = tk.Tk()
    app = RaceScreen(root)
    root.mainloop()