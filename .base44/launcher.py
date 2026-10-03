"""Development desktop launcher; runs the repository's original Turtle demos."""
import subprocess
import tkinter as tk
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
window = tk.Tk()
window.title("Python Turtle demos")
window.geometry("520x290+40+40")
window.configure(bg="#f5f7fb")

tk.Label(window, text="Python Turtle demos", font=("sans", 22, "bold"), bg="#f5f7fb").pack(pady=(24, 12))
tk.Label(window, text="Choose a demo to run from the cloned source.", bg="#f5f7fb").pack(pady=8)


def launch(filename, terminal=False):
    command = ["/usr/bin/python3", str(ROOT / filename)]
    if terminal:
        command = ["xterm", "-T", "Enter movement steps", "-geometry", "80x12+40+420", "-e", *command]
    subprocess.Popen(command, cwd=ROOT)


tk.Button(window, text="Screen color — click to change background", command=lambda: launch("screencolor.py"), padx=15, pady=8).pack(pady=8)
tk.Button(window, text="Key events — enter steps in the terminal", command=lambda: launch("key events", terminal=True), padx=15, pady=8).pack(pady=8)
tk.Label(window, text="Close a demo window before launching it again.\nChanges take effect when you reopen a demo.", bg="#f5f7fb", fg="#526075").pack(pady=8)
window.mainloop()
