import tkinter as tk
from tkinter import ttk


class F1App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("F1 Game — MAX ATTACK Edition")
        self.geometry("720x480")
        self.minsize(640, 420)

        # Apply theme
        self._apply_theme()

        # Header bar (Max Verstappen reference)
        header = ttk.Frame(self, style="F1.TFrame")
        header.pack(fill="x")
        ttk.Label(
            header,
            text="F1 World Championship — Max Attack 🏁",
            style="F1Header.TLabel",
            anchor="w"
        ).pack(side="left", padx=10, pady=8)

        self.dm = DataManager()

        nb = ttk.Notebook(self, style="F1.TNotebook")
        nb.pack(fill="both", expand=True)

        self.players_tab = ttk.Frame(nb, style="F1.TFrame")
        self.teams_tab = ttk.Frame(nb, style="F1.TFrame")
        self.race_tab = ttk.Frame(nb, style="F1.TFrame")

        nb.add(self.players_tab, text="Players")
        nb.add(self.teams_tab, text="Teams")
        nb.add(self.race_tab, text="Race")

        self._build_players_tab()
        self._build_teams_tab()
        self._build_race_tab()

        self.refresh_players()
        self.refresh_teams()

    def clear_output(self):
        """Clear the race output panel."""
        self.race_output.delete("1.0", tk.END)

    def _build_race_tab(self):
        frm = self.race_tab

        # Top row split: controls (left) + preview (right)
        top = ttk.Frame(frm, style="F1.TFrame")
        top.pack(fill="x", padx=8, pady=8)

        controls = ttk.Frame(top, style="F1.TFrame")
        controls.pack(side="left", fill="x", expand=True)

        ttk.Label(controls, text="Select location:", style="F1.TLabel").pack(anchor="w", pady=(0, 4))
        self.location_var = tk.StringVar()
        loc_names = [loc.name for loc in self.dm.locations]
        self.location_combo = ttk.Combobox(controls, textvariable=self.location_var, values=loc_names, state="readonly")
        if loc_names:
            self.location_combo.current(0)
        self.location_combo.pack(fill="x")
        # Fire on any change (selection or programmatic)
        self.location_var.trace_add("write", lambda *a: self.update_track_preview_by_name(self.location_var.get()))
        # (optional) still bind selection
        self.location_combo.bind("<<ComboboxSelected>>",
                                 lambda e: self.update_track_preview_by_name(self.location_var.get()))

        btn_row = ttk.Frame(controls, style="F1.TFrame")
        btn_row.pack(anchor="w", pady=6)
        ttk.Button(btn_row, text="Run Race", style="F1.TButton",
                   command=self.run_race).pack(side="left", padx=(0, 6))
        ttk.Button(btn_row, text="Clear Output", style="F1.TButton",
                   command=self.clear_output).pack(side="left")

        # Right: small Track Preview box
        preview = ttk.Frame(top, style="F1.TFrame")
        preview.pack(side="right", padx=(12, 0))
        ttk.Label(preview, text="Track Preview", style="F1.TLabel").pack(anchor="w")
        self.track_preview = tk.Text(preview,
                                     height=10, width=36,  # small box
                                     font=("Consolas", 10),
                                     bg=F1_MID, fg=F1_TEXT,
                                     insertbackground=F1_TEXT,
                                     highlightthickness=0, relief="solid", borderwidth=1)
        self.track_preview.pack()

        # Progress bar (used by animations; shown only when running)
        self.race_progress = ttk.Progressbar(frm, mode="determinate", maximum=100, style="F1.Horizontal.TProgressbar")
        # (packed only during animation)

        # Main race output below
        self.race_output = tk.Text(frm, height=18, font=("Consolas", 10),
                                   bg=F1_MID, fg=F1_TEXT,
                                   insertbackground=F1_TEXT,
                                   highlightthickness=0, relief="flat")
        self.race_output.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        if loc_names:
            self.after(0, lambda: self.update_track_preview_by_name(self.location_var.get()))
