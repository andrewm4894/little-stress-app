import tkinter as tk
from tkinter import ttk, IntVar
from PIL import Image, ImageTk
import os
import subprocess
from tkinter import simpledialog, messagebox
import Pmw


def run_command(command_template, duration_var):
    duration = duration_var.get()
    cmd = command_template.format(duration)
    try:
        subprocess.Popen(cmd, shell=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def stop_stress_ng():
    try:
        subprocess.run(["pkill", "stress-ng"])
    except Exception as e:
        messagebox.showerror("Error", str(e))



root = tk.Tk()
root.title("Stress-ng Command Runner")

Pmw.initialise(root)
balloon = Pmw.Balloon(root)  # for the tooltips

default_image_path = os.path.join(os.path.dirname(__file__), "fire.jpeg")

# Set duration frame
duration_frame = ttk.LabelFrame(root, text="Set Duration (seconds)", padding="10")
duration_frame.pack(padx=10, pady=5, fill="x", expand=True)

duration_var = IntVar(value=15)  # Default duration set to 15 seconds
duration_spinbox = ttk.Spinbox(duration_frame, from_=1, to=3600, textvariable=duration_var, width=5)
duration_spinbox.pack(pady=5)

# Commands and their explanations
commands = {
    "cpu_load.jpeg": "stress-ng --cpu 4 --timeout {}s",
    "memory_load.jpeg": "stress-ng --vm 2 --vm-bytes 256M --timeout {}s",
    "io_load.jpeg": "stress-ng --io 4 --timeout {}s",
    "hdd_load.jpeg": "stress-ng --hdd 2 --timeout {}s",
    "socket_load.jpeg": "stress-ng --sock 6 --timeout {}s",
    "matrix_load.jpeg": "stress-ng --matrix 2 --timeout {}s",
    "fork_bomb.jpeg": "stress-ng --fork 4 --timeout {}s",
    "yield_load.jpeg": "stress-ng --yield 4 --timeout {}s",
    "sem_load.jpeg": "stress-ng --sem 4 --timeout {}s"
}

explanations = {
    "cpu_load": "This stresses the CPU with 4 workers for a specified duration.",
    "memory_load": "This stresses the virtual memory with 2 workers and 256M bytes per worker for a specified duration.",
    "io_load": "Stresses the I/O by spawning 4 workers.",
    "hdd_load": "Stresses the hard drive by spawning 2 workers.",
    "socket_load": "Stresses sockets by creating 6 workers.",
    "matrix_load": "Stresses CPU by performing matrix multiplications with 2 workers.",
    "fork_bomb": "This is a fork bomb, spawning processes exponentially.",
    "yield_load": "This aggressively yields the processor, stressing kernel scheduling.",
    "sem_load": "This stresses semaphore operations with 4 workers."
}

# Button frame
button_frame = ttk.LabelFrame(root, text="Stress Commands", padding="10")
button_frame.pack(padx=10, pady=5, fill="x", expand=True)

# Create and place buttons in two columns within button_frame
row = 0
col = 0
for image_file, cmd_template in commands.items():
    try:
        # Attempt to load the specific image
        image_path = os.path.join(os.path.dirname(__file__), image_file)
        image = Image.open(image_path)
    except FileNotFoundError:
        # If specific image isn't found, load the default image
        image = Image.open(default_image_path)
        
    photo = ImageTk.PhotoImage(image)

    # Create a button with the image
    btn = tk.Button(button_frame, image=photo, command=lambda cmd_template=cmd_template: run_command(cmd_template, duration_var))
    btn.image = photo  # Keep a reference to prevent garbage collection
    btn.grid(row=row, column=col, pady=10, padx=5, sticky='w'+'e')
    balloon.bind(btn, "Command: " + cmd_template.format("[duration]") + "\nExplanation: " + explanations[image_file.replace(".png", "").replace(".jpeg", "")])

    # Logic for 3x3 layout
    col += 1
    if col == 3:
        col = 0
        row += 1

# Create and place the stop button
stop_button = ttk.Button(root, text="Stop All Stressing", command=stop_stress_ng)
stop_button.pack(pady=10)

root.mainloop()
