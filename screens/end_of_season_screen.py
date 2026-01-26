import tkinter as tk
from tkinter import ttk

class EndOfSeasonScreen:
    def __init__(self, root, standings, total_races, champion, on_new_season, on_exit):
        self.root = root
        self.root.title("End of Season")

        # Title Label
        self.title_label = tk.Label(root, text="Season Complete!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Champion Label
        self.champion_label = tk.Label(root, text=f"Champion: {champion['name']} ({champion['team']})", font=("Arial", 14, "bold"))
        self.champion_label.pack(pady=5)

        # Season Summary
        self.summary_label = tk.Label(root, text=f"Total Races: {total_races}\nWinner Points: {champion['points']}", font=("Arial", 12))
        self.summary_label.pack(pady=10)

        # Standings Table
        self.tree = ttk.Treeview(root, columns=("Driver", "Team", "Points"), show="headings")
        self.tree.heading("Driver", text="Driver")
        self.tree.heading("Team", text="Team")
        self.tree.heading("Points", text="Points")
        self.tree.pack(pady=10)
        self.display_standings(standings)

        # Buttons
        self.new_season_button = tk.Button(root, text="Start New Season", command=on_new_season)
        self.new_season_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit Game", command=on_exit)
        self.exit_button.pack(pady=5)

    def display_standings(self, standings):
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert sorted standings
        sorted_standings = sorted(standings.items(), key=lambda x: x[1]["points"], reverse=True)
        for driver_name, data in sorted_standings:
            team = data["team"]
            points = data["points"]
            self.tree.insert("", tk.END, values=(driver_name, team, points))

if __name__ == "__main__":
    def mock_new_season():
        print("Starting a new season!")

    def mock_exit():
        print("Exiting game!")
        root.destroy()

    mock_standings = {
        "Driver 1": {"points": 100, "team": "Team A"},
        "Driver 2": {"points": 90, "team": "Team B"},
        "Driver 3": {"points": 80, "team": "Team C"}
    }
    mock_champion = {"name": "Driver 1", "team": "Team A", "points": 100}

    root = tk.Tk()
    app = EndOfSeasonScreen(root, mock_standings, total_races=10, champion=mock_champion, on_new_season=mock_new_season, on_exit=mock_exit)
    root.mainloop()