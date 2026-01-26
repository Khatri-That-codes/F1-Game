import time
import tkinter as tk
from tkinter import font
from colorama import Fore, Style

import theme
from theme.colour_palette import styled_text, F1_GOLD, F1_SILVER, F1_BRONZE, team_colours
from src.sound_manager import SoundManager

def display_podium(p1, p2, p3):
    """
    Display the podium with P1, P2, and P3 highlighted.

    Args:
        p1 (str): Name of the first-place driver.
        p2 (str): Name of the second-place driver.
        p3 (str): Name of the third-place driver.
    """
    podium = [
        f"{Fore.LIGHTWHITE_EX}        {Fore.LIGHTYELLOW_EX}🥇 {p1} {Style.RESET_ALL}",
        f"{Fore.LIGHTWHITE_EX}   {Fore.LIGHTWHITE_EX}🥈 {p2} {Style.RESET_ALL}",
        f"{Fore.LIGHTWHITE_EX}      🥉 {p3} {Style.RESET_ALL}",
    ]

    podium_blocks = [
        "        ████████",
        "   ████████",
        "      ████████",
    ]

    for i in range(3):
        print("\n" * 10)  # Clear the screen
        for j in range(3):
            if j == i:
                print(podium[j])
            print(podium_blocks[j])
        time.sleep(0.5)

    print("\n" * 2)
    print(f"{Fore.LIGHTYELLOW_EX}🏆 Congratulations to {p1}! {Style.RESET_ALL}")

def show_podium_screen(root, race_results, on_continue):
    """
    Display a podium ceremony after a race.

    Args:
        root (tk.Tk): The root Tkinter window.
        race_results (list): List of race results sorted by finishing position.
        on_continue (function): Callback for the "Continue" button.
    """
    # Create a new frame for the podium screen
    podium_frame = tk.Frame(root, bg="black")
    podium_frame.pack(fill="both", expand=True)

    # Extract P1, P2, P3
    p1, p2, p3 = race_results[:3]

    # Define podium layout
    podium_layout = [
        (p2, F1_SILVER, 2),
        (p1, F1_GOLD, 1),
        (p3, F1_BRONZE, 3),
    ]

    # Create a monospaced font
    mono_font = font.Font(family="Courier", size=14, weight="bold")

    # Create labels for the podium
    labels = []
    for driver, colour, position in podium_layout:
        label = tk.Label(
            podium_frame,
            text=f"🥈🥇🥉\n{driver['name']}\n{driver['team']}",
            fg=colour,
            bg="black",
            font=mono_font,
        )
        label.pack()
        labels.append(label)

    # Animate the podium appearing line by line
    def animate_podium(index=0):
        if index < len(labels):
            labels[index].pack()
            root.after(500, animate_podium, index + 1)
        else:
            # Play crowd cheer sound
            sound_manager = SoundManager()
            sound_manager.play_effect("cheer")

    animate_podium()

    # Add a "Continue" button
    continue_button = tk.Button(
        podium_frame,
        text="Continue",
        command=lambda: [podium_frame.destroy(), on_continue()],
        bg="gray",
        fg="white",
        font=mono_font,
    )
    continue_button.pack(pady=20)

# Example usage
if __name__ == "__main__":
    def mock_continue():
        print("Continuing to the next screen...")

    mock_results = [
        {"name": "Verstappen", "team": "Red Bull"},
        {"name": "Hamilton", "team": "Mercedes"},
        {"name": "Leclerc", "team": "Ferrari"},
    ]

    root = tk.Tk()
    show_podium_screen(root, mock_results, mock_continue)
    root.mainloop()

    display_podium("Verstappen", "Hamilton", "Leclerc")