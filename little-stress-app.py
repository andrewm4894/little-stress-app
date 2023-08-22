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

    # Define commands with their emojis
    commands = {
        "🔥 CPU Load": "stress-ng --cpu 4 --timeout {}s",
        "🧠 Memory Load": "stress-ng --vm 2 --vm-bytes 256M --timeout {}s",
        "💽 I/O Load": "stress-ng --io 4 --timeout {}s",
        "🍴 Fork/Process Load": "stress-ng --fork 4 --timeout {}s",
        "🌐 Network Load": "stress-ng --netdev 2 --timeout {}s",
        "🔢 Matrix Load": "stress-ng --matrix 2 --timeout {}s",
        "💾 Disk Load": "stress-ng --hdd 2 --timeout {}s",
        "🔄 Context Switching Load": "stress-ng --context 2 --timeout {}s",
        "💰 Cache Thrashing": "stress-ng --cache 2 --cache-ops 1000000 --timeout {}s",
        "🔋 Thermal and Power": "stress-ng --power 2 --timeout {}s",
        "🔒 Semaphore Stress": "stress-ng --sem 4 --timeout {}s",
        "🧟 Zombie Processes": "stress-ng --zombie 1000 --timeout {}s",
        "🔌 Socket Load": "stress-ng --sock 2 --timeout {}s",
        "✉️ Msg Stress": "stress-ng --msg 2 --timeout {}s",
        "🌪 Combination Load": "stress-ng --cpu 2 --io 2 --vm 2 --vm-bytes 128M --timeout {}s"
    }

    explanations = {
        "🔥 CPU Load": "Stresses the CPU cores.",
        "🧠 Memory Load": "Stresses the RAM.",
        "💽 I/O Load": "Stresses the I/O operations.",
        "🍴 Fork/Process Load": "Stresses the system by constantly forking processes.",
        "🌐 Network Load": "Stresses the network interfaces.",
        "🔢 Matrix Load": "Performs matrix multiplications to stress the CPU.",
        "💾 Disk Load": "Stresses disk writes.",
        "🔄 Context Switching Load": "Stresses the context switching mechanism.",
        "💰 Cache Thrashing": "Stresses the cache.",
        "🔋 Thermal and Power": "Stress power management and thermal code.",
        "🔒 Semaphore Stress": "Stresses system semaphores.",
        "🧟 Zombie Processes": "Creates a large number of zombie processes.",
        "🔌 Socket Load": "Stresses socket operations.",
        "✉️ Msg Stress": "Stresses System V message passing.",
        "🌪 Combination Load": "Combines multiple scenarios together for a composite load."
    }

    # Create and place buttons
    for label, cmd_template in commands.items():
        btn = ttk.Button(root, text=label, command=lambda cmd_template=cmd_template: run_command(cmd_template, duration_var))
        btn.pack(pady=10)
        balloon.bind_widget(btn, msg="Command: " + cmd_template.format("[duration]") + "\nExplanation: " + explanations[label])

    root.mainloop()

if __name__ == "__main__":
    main()
