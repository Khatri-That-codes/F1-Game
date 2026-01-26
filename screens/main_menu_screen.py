import tkinter as tk
from tkinter import font
import theme
from theme.colour_palette import themed_header, themed_button

class MainMenuScreen(tk.Frame):
    def __init__(self, root, app_state, show_screen):
        """
        Initialize the Main Menu screen.

        Args:
            root (tk.Tk): The root Tkinter window.
            app_state (dict): Shared application state.
            show_screen (function): Function to switch screens.
        """
        super().__init__(root, bg="black")
        self.app_state = app_state
        self.show_screen = show_screen

        # Create a monospaced font
        header_font = font.Font(family="Courier", size=24, weight="bold")
        button_font = font.Font(family="Courier", size=14, weight="bold")

        # Title
        title_label = tk.Label(
            self,
            text="F1 Racing Simulator",
            fg="white",
            bg="black",
            font=header_font,
        )
        title_label.pack(pady=20)

        # New Season button
        new_season_button = tk.Button(
            self,
            text="New Season",
            command=self.start_new_season,
            bg="gray",
            fg="white",
            font=button_font,
        )
        new_season_button.pack(pady=10)

        # Load Season button
        load_season_button = tk.Button(
            self,
            text="Load Season",
            command=self.load_season,
            bg="gray",
            fg="white",
            font=button_font,
        )
        load_season_button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(
            self,
            text="Exit",
            command=root.destroy,
            bg="gray",
            fg="white",
            font=button_font,
        )
        exit_button.pack(pady=10)

    def start_new_season(self):
        """Initialize a new season and go to the Race Intro screen."""
        # Initialize season data
        self.app_state["season"] = None  # Replace with actual Season initialization logic
        self.app_state["current_track_index"] = 0
        self.app_state["drivers"] = []  # Replace with actual driver initialization
        self.app_state["standings"] = {}

        # Go to the Race Intro screen
        self.show_screen("race_intro")

    def load_season(self):
        """Load a saved season and resume the flow."""
        # Replace with actual load logic
        print("Load season logic goes here")
        self.show_screen("race_intro")

# Example usage
if __name__ == "__main__":
    def mock_show_screen(name):
        print(f"Switching to screen: {name}")

    root = tk.Tk()
    app_state = {}
    main_menu = MainMenuScreen(root, app_state, mock_show_screen)
    main_menu.pack(fill="both", expand=True)
    root.mainloop()