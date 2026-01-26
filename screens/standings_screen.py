import tkinter as tk
from tkinter import ttk

class StandingsScreen:
    def __init__(self, root, standings, on_next_race):
        self.root = root
        self.root.title("Championship Standings")

        # Title Label
        self.title_label = tk.Label(root, text="Championship Standings", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Standings Table
        self.tree = ttk.Treeview(root, columns=("Driver", "Team", "Points"), show="headings")
        self.tree.heading("Driver", text="Driver")
        self.tree.heading("Team", text="Team")
        self.tree.heading("Points", text="Points")
        self.tree.pack(pady=10)
        self.display_standings(standings)

        # Next Race Button
        self.next_race_button = tk.Button(root, text="Next Race", command=on_next_race)
        self.next_race_button.pack(pady=10)

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
    def mock_next_race():
        print("Next Race button clicked!")

    mock_standings = {
        "Driver 1": {"points": 50, "team": "Team A"},
        "Driver 2": {"points": 40, "team": "Team B"},
        "Driver 3": {"points": 30, "team": "Team C"}
    }

    root = tk.Tk()
    app = StandingsScreen(root, mock_standings, mock_next_race)
    root.mainloop()