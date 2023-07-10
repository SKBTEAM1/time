import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Create the main window
window = tk.Tk()
window.title("AM/PM Clock with SKB Logo")
window.geometry("400x300")

# Create a label for the clock display
clock_label = ttk.Label(window, font=("Arial", 40))
clock_label.pack(pady=20)

# Create a label for the colorful logo
logo_label = ttk.Label(window, font=("Arial", 20))
logo_label.pack(fill=tk.X)

# Function to update the clock display
def update_clock():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    window.after(1000, update_clock)

# Function to update the logo label with colored text
def update_logo():
    logo_text = "SKB"
    logo_label.config(text="")
    colors = ["red", "green", "blue"]  # You can add more colors here

    for i, char in enumerate(logo_text):
        color = colors[i % len(colors)]
        logo_label.config(text=logo_label["text"] + char, foreground=color)
        window.update()
        window.after(500)

    window.after(2000, update_logo)

# Start updating the clock and logo
update_clock()
update_logo()

# Run the main loop
window.mainloop()
