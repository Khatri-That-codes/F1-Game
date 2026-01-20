import re

def _slug(self, name: str) -> str:
    s = re.sub(r"[\(\)\-]", " ", name.lower())
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s

def _ascii_tracks(self) -> dict[str, str]:
    return {
        "monza": (
            "          ╭──────────────╮        \n"
            "        ╭─╯              ╰─╮      \n"
            "      ╭─╯   Variante      ╰─╮     \n"
            "      │     del Rettifilo   │     \n"
            "      │                      │     \n"
            "      │                      │     \n"
            "      │   Lesmo     Ascari   │     \n"
            "      ╰─╮                ╭───╯     \n"
            "        ╰───────────────╯          "
        ),
        "monaco": (
            "   ╭───────╮  ╭────╮              \n"
            "   │Start/ │──╯    │  Casino      \n"
            "   │Finish │       ╰──╮           \n"
            "   ╰──╮  ╭─╯           │          \n"
            "      │  │  Tunnel     │          \n"
            "  Port│  ╰──╮     ╭────╯          \n"
            "       ╰────╯─────╯  Chicane      "
        ),
        "silverstone": (
            "  ╭────── Hangar Straight ───────╮\n"
            "  │                               │\n"
            "  │   Maggots/Becketts            │\n"
            "  ╰─╮                         ╭───╯\n"
            "    ╰───── Club ─────── Stowe ╯    "
        ),
        "suzuka": (
            "     ╭────┐                      \n"
            "  ╭──╯    ╰──╮                   \n"
            "  │  Esses   │                   \n"
            "  ╰─╮     ╭──╯  Spoon            \n"
            "    ╰──╮ ╭╯      130R ───╮       \n"
            "       ╰─╯               ╰──╮    "
        ),
        "spa_francorchamps": (
            " Start           Kemmel Straight  \n"
            "  │  ╭─ Eau Rouge / Raidillon ─╮  \n"
            "  ╰──╯                         │  \n"
            "   Pouhon                 Stavelot \n"
            "      ╭───────╮         ╭──────╮  \n"
            "      ╰────────╯─────────╯──────╯  "
        ),
        "singapore": (
            " ╭──────── Marina Bay ────────╮   \n"
            " │   Street Circuit           │   \n"
            " ╰─╮   ╭────╮      ╭────╮  ╭─╯   \n"
            "   │   ╰────╯      ╰────╯  │     \n"
            "   ╰────────────────────────╯     "
        ),
        "bahrain": (
            "     ╭───────────╮                \n"
            "   ╭─╯           ╰─╮              \n"
            "  ╭╯   Hairpin     ╰╮             \n"
            "  │                 │             \n"
            "  ╰──╮         ╭───╯             \n"
            "     ╰─────────╯                  "
        ),
        "australia": (
            "   ╭──────── Albert Park ───────╮ \n"
            "   │                            │ \n"
            "   │  Lakeside   Chicane        │ \n"
            "   ╰─╮                      ╭───╯ \n"
            "     ╰──────────────────────╯     "
        ),
        "circuit_of_the_americas": (
            "    ╭── Uphill T1 ──╮             \n"
            "  ╭─╯               ╰─╮           \n"
            "  │   Esses            │          \n"
            "  ╰─╮             ╭───╯           \n"
            "    ╰───── Stadium ╯              "
        ),
    }

def _ascii_generic_track(self, name: str) -> str:
    return (
        f"   {name}\n"
        "   ╭────────────────────────╮\n"
        "   │    . . . chicane . .   │\n"
        "   │                        │\n"
        "   ╰─────────╮  ╭──────────╯\n"
        "             ╰──╯            "
    )