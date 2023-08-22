import tkinter as tk
from tkinter import ttk
import subprocess

def run_command(cmd):
    subprocess.Popen(cmd, shell=True)

def main():
    root = tk.Tk()
    root.title("Stress-ng Tester")

    # Define commands
    commands = {
        "CPU Load": "stress-ng --cpu 4 --timeout 60s",
        "Memory Load": "stress-ng --vm 2 --vm-bytes 256M --timeout 60s",
        "I/O Load": "stress-ng --io 4 --timeout 60s",
        "Fork/Process Load": "stress-ng --fork 4 --timeout 60s",
        # ... Add all other commands similarly ...
    }

    # Create and place buttons
    for label, cmd in commands.items():
        btn = ttk.Button(root, text=label, command=lambda cmd=cmd: run_command(cmd))
        btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
