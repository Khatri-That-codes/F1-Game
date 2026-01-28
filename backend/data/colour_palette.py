'''
This file defines a colour palette for F1 theme
'''
# F1 palette
"""
F1-inspired colour palette
"""

# Core
F1_RED        = "#E10600"   # Official F1 red
F1_BLACK      = "#0B0B0B"   # Near-black (easier on eyes)
F1_DARK_GRAY  = "#141414"
F1_MID_GRAY   = "#1F1F1F"

# Text
F1_TEXT_MAIN  = "#F5F5F5"
F1_TEXT_MUTED = "#B0B0B0"
F1_TEXT_DIM   = "#7A7A7A"

# Accents
F1_GREEN     = "#00C853"   # Positive (gains, P1)
F1_YELLOW    = "#FFD600"   # Warnings / flags
F1_BLUE      = "#2979FF"   # Info / buttons


TEAM_COLORS = {
    "red_bull": "#0600ef",
    "ferrari": "#dc0000",
    "mercedes": "#00d2be",
    "mclaren": "#ff8700",
    "aston_martin": "#006f62",
    "alpine": "#0090ff",
    "williams": "#005aff",
    "rb": "#2b4562",
    "sauber": "#00ff41",
    "haas": "#ffffff",
}


#Podium colours
F1_GOLD   = "#d4af37"   # podium / winner
F1_SILVER = "#c0c0c0"
F1_BRONZE = "#cd7f32"

from colorama import Fore, Style

# Central colour palette
F1_RED = Fore.RED
F1_DARK_BG = Style.DIM + Fore.BLACK
F1_MUTED_TEXT = Style.DIM + Fore.WHITE
F1_GOLD = Fore.YELLOW
F1_SILVER = Fore.LIGHTWHITE_EX
F1_BRONZE = Fore.LIGHTRED_EX

# Team colour mapping
def team_colours():
    return {
        "Red Bull": Fore.BLUE,
        "Mercedes": Fore.CYAN,
        "Ferrari": Fore.RED,
        "McLaren": Fore.LIGHTYELLOW_EX,
        "Alpine": Fore.LIGHTBLUE_EX,
        "Aston Martin": Fore.GREEN,
        "AlphaTauri": Fore.LIGHTBLACK_EX,
        "Alfa Romeo": Fore.MAGENTA,
        "Williams": Fore.LIGHTWHITE_EX,
        "Haas": Fore.WHITE,
    }

# Styled text output helpers
def styled_text(text, colour, bold=False):
    """Return styled text with the given colour and optional bold formatting."""
    style = colour
    if bold:
        style += Style.BRIGHT
    return f"{style}{text}{Style.RESET_ALL}"

def winner_text(text):
    """Return text styled for winners (gold)."""
    return styled_text(text, F1_GOLD, bold=True)

def muted_text(text):
    """Return text styled as muted."""
    return styled_text(text, F1_MUTED_TEXT)

# Widget theming helpers
def themed_header(text):
    """Return a styled header with F1 red."""
    return styled_text(text, F1_RED, bold=True)

def themed_button(text):
    """Return a styled button with a muted background."""
    return styled_text(f"[ {text} ]", F1_MUTED_TEXT, bold=True)

def themed_table_row(cells, team=None):
    """Return a styled table row, optionally using team colours."""
    row = " | ".join(cells)
    if team:
        return styled_text(row, team_colours().get(team, F1_MUTED_TEXT))
    return styled_text(row, F1_MUTED_TEXT)

# Example usage
if __name__ == "__main__":
    print(winner_text("Congratulations to the winner!"))
    print(styled_text("Team Mercedes", team_colours()["Mercedes"]))
    print(muted_text("This is muted text."))
    print(themed_header("Race Results"))
    print(themed_button("Start Race"))
    print(themed_table_row(["P1", "Verstappen", "Red Bull"], team="Red Bull"))
    print(themed_table_row(["P2", "Hamilton", "Mercedes"], team="Mercedes"))