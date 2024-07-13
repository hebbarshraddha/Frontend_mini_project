import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Friendly Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg='#1e1e2e')

        # Load and set the background image using Pillow
        image_path = "C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\chatbot11.jpg"
        image = Image.open(image_path)
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Create the title label
        self.title_label = tk.Label(root, text="Have a Conversation with Our Friendly Bot", font=("Arial", 20), bg='#1e1e2e', fg='#ffffff')
        self.title_label.place(relx=0.5, rely=0.05, anchor="center")

        # Create the chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg='#2e2e3e', fg='#ffffff')
        self.chat_display.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.15)
        self.chat_display.config(state=tk.DISABLED)

        # Create the user input area
        self.user_input = tk.Entry(root, font=("Arial", 14), bg='#3e3e4e', fg='#ffffff')
        self.user_input.place(relwidth=0.7, relheight=0.08, relx=0.05, rely=0.87)

        # Create the ask button
        self.ask_button = tk.Button(root, text="Ask", font=("Arial", 14), bg='#5e5e6e', fg='#ffffff')
        self.ask_button.place(relwidth=0.2, relheight=0.08, relx=0.75, rely=0.87)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
