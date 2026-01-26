import time
from colorama import Fore, Style

def animate_track(track_ascii, waypoints):
    """
    Animate a car marker moving along the track.

    Args:
        track_ascii (str): ASCII representation of the track.
        waypoints (list of tuple): List of (row, col) positions for the car marker.
    """
    track_lines = track_ascii.split("\n")

    for row, col in waypoints:
        animated_track = track_lines.copy()
        animated_track[row] = (
            animated_track[row][:col] + Fore.RED + "🚗" + Style.RESET_ALL + animated_track[row][col + 1:]
        )

        print("\n" * 10)  # Clear the screen
        print("\n".join(animated_track))
        time.sleep(0.5)

# Example usage
if __name__ == "__main__":
    monza_ascii = (
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

    waypoints = [
        (3, 10), (3, 15), (4, 20), (5, 25), (6, 30), (7, 35), (8, 40)
    ]

    animate_track(monza_ascii, waypoints)