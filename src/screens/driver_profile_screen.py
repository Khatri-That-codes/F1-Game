import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class DriverProfileScreen(tk.Frame):
    def __init__(self, root, driver_data, show_screen):
        """
        Initialize the Driver Profile screen.

        Args:
            root (tk.Tk): The root Tkinter window.
            driver_data (dict): Data for the selected driver.
            show_screen (function): Function to switch screens.
        """
        super().__init__(root, bg="black")
        self.driver_data = driver_data
        self.show_screen = show_screen

        # Build the UI sections
        self.build_header()
        self.build_stats()
        self.build_season_stats()
        self.build_recent_form()
        self.build_narrative()
        self.build_navigation()

    def build_header(self):
        """Build the header section with driver portrait, name, and team logo."""
        header_frame = tk.Frame(self, bg="black")
        header_frame.grid(row=0, column=0, columnspan=2, pady=10)

        # Driver portrait
        portrait_path = f"assets/images/drivers/{self.driver_data['portrait']}"
        portrait_image = self.load_image(portrait_path, (100, 100))
        portrait_label = tk.Label(header_frame, image=portrait_image, bg="black")
        portrait_label.image = portrait_image  # Keep a reference
        portrait_label.grid(row=0, column=0, padx=10)

        # Driver name and number
        name_label = tk.Label(
            header_frame,
            text=f"{self.driver_data['name']} ({self.driver_data['number']})",
            fg="white",
            bg="black",
            font=("Courier", 18, "bold"),
        )
        name_label.grid(row=0, column=1, sticky="w")

        # Team logo
        team_logo_path = f"assets/images/teams/{self.driver_data['team_logo']}"
        team_logo_image = self.load_image(team_logo_path, (50, 50))
        team_logo_label = tk.Label(header_frame, image=team_logo_image, bg="black")
        team_logo_label.image = team_logo_image  # Keep a reference
        team_logo_label.grid(row=0, column=2, padx=10)

    def build_stats(self):
        """Build the stats section with progress bars for driver skills."""
        stats_frame = tk.Frame(self, bg="black")
        stats_frame.grid(row=1, column=0, columnspan=2, pady=10)

        for stat, value in self.driver_data['stats'].items():
            stat_label = tk.Label(stats_frame, text=stat, fg="white", bg="black")
            stat_label.pack(anchor="w")

            progress = ttk.Progressbar(stats_frame, length=200, value=value, maximum=100)
            progress.pack(anchor="w", pady=2)

    def build_season_stats(self):
        """Build the season stats section."""
        season_stats_frame = tk.Frame(self, bg="black")
        season_stats_frame.grid(row=2, column=0, columnspan=2, pady=10)

        for stat, value in self.driver_data['season_stats'].items():
            stat_label = tk.Label(
                season_stats_frame, text=f"{stat}: {value}", fg="white", bg="black"
            )
            stat_label.pack(anchor="w")

    def build_recent_form(self):
        """Build the recent form section with last 5 race results."""
        recent_form_frame = tk.Frame(self, bg="black")
        recent_form_frame.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(
            recent_form_frame, text="Recent Form:", fg="white", bg="black", font=("Courier", 14, "bold")
        ).pack(anchor="w")

        for result in self.driver_data['recent_form']:
            color = "green" if result.startswith("P1") else "yellow" if result.startswith("P") else "red"
            result_label = tk.Label(recent_form_frame, text=result, fg=color, bg="black")
            result_label.pack(anchor="w")

    def build_narrative(self):
        """Build the narrative section with bio and media sentiment."""
        narrative_frame = tk.Frame(self, bg="black")
        narrative_frame.grid(row=4, column=0, columnspan=2, pady=10)

        bio_label = tk.Label(
            narrative_frame, text=f"Bio: {self.driver_data['bio']}", fg="white", bg="black", wraplength=400
        )
        bio_label.pack(anchor="w")

        sentiment_label = tk.Label(
            narrative_frame, text=f"Media Sentiment: {self.driver_data['media_sentiment']}", fg="white", bg="black"
        )
        sentiment_label.pack(anchor="w")

    def build_navigation(self):
        """Build the navigation section with a Back button."""
        nav_frame = tk.Frame(self, bg="black")
        nav_frame.grid(row=5, column=0, columnspan=2, pady=10)

        back_button = tk.Button(
            nav_frame,
            text="Back",
            command=lambda: self.show_screen("standings"),
            bg="gray",
            fg="white",
        )
        back_button.pack()

    def load_image(self, path, size):
        """Load an image with a fallback if the file is missing."""
        try:
            image = Image.open(path).resize(size, Image.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Image not found: {path}")
            return ImageTk.PhotoImage(Image.new("RGB", size, "black"))

# Example usage
if __name__ == "__main__":
    def mock_show_screen(name):
        print(f"Switching to screen: {name}")

    mock_driver_data = {
        "name": "Max Verstappen",
        "number": 33,
        "portrait": "verstappen.jpg",
        "team_logo": "red_bull.png",
        "stats": {
            "Pace": 95,
            "Qualifying": 90,
            "Racecraft": 92,
            "Consistency": 88,
            "Aggression": 85,
            "XP Level": 100,
        },
        "season_stats": {
            "Races": 10,
            "Wins": 6,
            "Podiums": 8,
            "Poles": 5,
            "DNFs": 1,
            "Championship Points": 200,
            "Current Position": 1,
        },
        "recent_form": ["P1", "P2", "P3", "DNF", "P5"],
        "bio": "Max Verstappen is a Dutch racing driver and the 2021 Formula One World Champion.",
        "media_sentiment": "Positive",
    }

    root = tk.Tk()
    driver_profile = DriverProfileScreen(root, mock_driver_data, mock_show_screen)
    driver_profile.pack(fill="both", expand=True)
    root.mainloop()