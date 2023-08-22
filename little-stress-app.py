import tkinter as tk
from tkinter import ttk, tix

import subprocess

def run_command(cmd_template, duration_var):
    cmd = cmd_template.format(duration_var.get())
    subprocess.Popen(cmd, shell=True)

def main():
    root = tix.Tk()
    root.title("Stress-ng Tester")

    balloon = tix.Balloon(root)

    # Duration input
    ttk.Label(root, text="Duration (seconds):").pack(pady=5)
    duration_var = tk.IntVar(value=60)  # default value
    ttk.Entry(root, textvariable=duration_var).pack(pady=5)

    # Define commands
    commands = {
        # ... (Same commands as before) ...
    }

    explanations = {
        "CPU Load": "Stresses the CPU cores.",
        "Memory Load": "Stresses the RAM.",
        # ... Add explanations for all other commands ...
    }

    # Create and place buttons
    for label, cmd_template in commands.items():
        btn = ttk.Button(root, text="▶ " + label, command=lambda cmd_template=cmd_template: run_command(cmd_template, duration_var))
        btn.pack(pady=10)
        balloon.bind_widget(btn, msg="Command: " + cmd_template.format("[duration]") + "\nExplanation: " + explanations[label])

    root.mainloop()

if __name__ == "__main__":
    main()
