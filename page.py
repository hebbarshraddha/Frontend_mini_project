
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Welcome to Wellness Whisper 🌟")
root.geometry("800x600")

# Load background image
bg_image = Image.open("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\healthwealth.jpg")
bg_image = bg_image.resize((800, 600), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor='nw')

# Create a frame for the content
frame = tk.Frame(canvas, bg='#ff7e5f', bd=0)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Add a title label with emojis
title = ttk.Label(frame, text="Welcome to Wellness Whisper 🌿✨", font=('Arial', 30, 'bold'), background='#ff7e5f', foreground='white')
title.pack(pady=20)

# Add a subtitle label with emojis
subtitle = ttk.Label(frame, text="Your journey to a healthier and happier life starts here. 😊💪🍎", font=('Arial', 16), background='#ff7e5f', foreground='white')
subtitle.pack(pady=10)

# Run the application
root.mainloop()
