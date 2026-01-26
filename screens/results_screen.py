import tkinter as tk
from tkinter import ttk

class ResultsScreen:
    def __init__(self, root, results, incidents, points, on_continue):
        self.root = root
        self.root.title("Race Results")

        # Title Label
        self.title_label = tk.Label(root, text="Race Results", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Results Section
        self.results_label = tk.Label(root, text="Final Classification:", font=("Arial", 12, "bold"))
        self.results_label.pack(pady=5)
        self.results_list = tk.Text(root, height=10, width=50)
        self.results_list.pack(pady=5)
        self.display_results(results)

        # Penalties Section
        self.penalties_label = tk.Label(root, text="Penalties:", font=("Arial", 12, "bold"))
        self.penalties_label.pack(pady=5)
        self.penalties_list = tk.Text(root, height=5, width=50)
        self.penalties_list.pack(pady=5)
        self.display_penalties(incidents)

        # Points Section
        self.points_label = tk.Label(root, text=f"Points Awarded: {points}", font=("Arial", 12))
        self.points_label.pack(pady=10)

        # Continue Button
        self.continue_button = tk.Button(root, text="Continue", command=on_continue)
        self.continue_button.pack(pady=10)

    def display_results(self, results):
        for i, driver in enumerate(results, start=1):
            self.results_list.insert(tk.END, f"P{i}: {driver.name} ({driver.team})\n")
        self.results_list.config(state=tk.DISABLED)

    def display_penalties(self, incidents):
        if not incidents:
            self.penalties_list.insert(tk.END, "No penalties applied.\n")
        else:
            for incident in incidents:
                self.penalties_list.insert(tk.END, f"{incident.description} - Penalty: {incident.penalty}\n")
        self.penalties_list.config(state=tk.DISABLED)

if __name__ == "__main__":
    def mock_continue():
        # Example logic to switch to Standings Screen
        from screens.standings_screen import StandingsScreen
        mock_standings = {
            "Driver 1": {"points": 50, "team": "Team A"},
            "Driver 2": {"points": 40, "team": "Team B"},
            "Driver 3": {"points": 30, "team": "Team C"}
        }
        for widget in root.winfo_children():
            widget.destroy()  # Clear the current screen
        StandingsScreen(root, mock_standings, lambda: print("Next Race clicked!"))

    mock_results = [
        type("Driver", (), {"name": "Driver 1", "team": "Team A"}),
        type("Driver", (), {"name": "Driver 2", "team": "Team B"}),
        type("Driver", (), {"name": "Driver 3", "team": "Team C"})
    ]
    mock_incidents = [
        type("Incident", (), {"description": "Collision at Turn 3", "penalty": "5 seconds"}),
        type("Incident", (), {"description": "Track limits violation", "penalty": "Warning"})
    ]
    mock_points = 25

    root = tk.Tk()
    app = ResultsScreen(root, mock_results, mock_incidents, mock_points, mock_continue)
    root.mainloop()