# # # # import tkinter as tk
# # # # from tkinter import ttk
# # # # from PIL import Image, ImageTk

# # # # class WellnessWhisperApp:
# # # #     def __init__(self, root):
# # # #         self.root = root
# # # #         self.root.title("Wellness Whisper")
# # # #         self.root.geometry("600x800")
# # # #         self.root.configure(bg='#fcdede')  # Light peach background color

# # # #         # Create the top frame for navigation buttons
# # # #         top_frame = tk.Frame(self.root, bg='#fcdede')
# # # #         top_frame.pack(side=tk.TOP, fill=tk.X)

# # # #         # Create the Sign In, Sign Up, and Settings buttons
# # # #         signin_button = tk.Button(top_frame, text="Sign In", font=("Arial", 12), bg='#4CAF50', fg='#ffffff')
# # # #         signup_button = tk.Button(top_frame, text="Sign Up", font=("Arial", 12), bg='#2196F3', fg='#ffffff')
# # # #         settings_button = tk.Button(top_frame, text="Settings", font=("Arial", 12), bg='#f0ad4e', fg='#ffffff')

# # # #         signin_button.pack(side=tk.LEFT, padx=10, pady=10)
# # # #         signup_button.pack(side=tk.LEFT, padx=10, pady=10)
# # # #         settings_button.pack(side=tk.LEFT, padx=10, pady=10)

# # # #         # Create the title label
# # # #         title_label = tk.Label(self.root, text="Wellness Whisper", font=("Arial", 24), bg='#fcdede', fg='#333333')
# # # #         title_label.pack(pady=20)

# # # #         # Create a frame for the round buttons
# # # #         button_frame = tk.Frame(self.root, bg='#fcdede')
# # # #         button_frame.pack(expand=True)

# # # #         # Define the button images and names
# # # #         button_info = [
# # # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\heart.jpg", "Button 1"),
# # # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\diabetes.jpg", "Button 2"),
# # # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\parkinsons.jpg", "Button 3"),
# # # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\chatbot.py", "Button 4")
# # # #         ]

# # # #         # Create round buttons with images and names
# # # #         for img_path, name in button_info:
# # # #             self.create_round_button(button_frame, img_path, name)

# # # #     def create_round_button(self, parent, img_path, name):
# # # #         try:
# # # #             # Load the image with LANCZOS method for resizing
# # # #             img = Image.open(img_path)
# # # #             img = img.resize((80, 80), Image.LANCZOS)
# # # #             photo = ImageTk.PhotoImage(img)

# # # #             # Create a canvas to hold the image
# # # #             canvas = tk.Canvas(parent, width=100, height=100, bg='#fcdede', highlightthickness=0)
# # # #             canvas.create_oval(10, 10, 90, 90, fill="#fff")
# # # #             canvas.create_image(50, 50, image=photo)
# # # #             canvas.image = photo
# # # #             canvas.pack(side=tk.LEFT, padx=20, pady=20)

# # # #             # Create a label for the button name
# # # #             label = tk.Label(parent, text=name, font=("Arial", 12), bg='#fcdede', fg='#333333')
# # # #             label.pack()

# # # #         except Exception as e:
# # # #             print(f"Error loading image {img_path}: {e}")

# # # # if __name__ == "__main__":
# # # #     root = tk.Tk()
# # # #     app = WellnessWhisperApp(root)
# # # #     root.mainloop()
# # # import tkinter as tk
# # # from tkinter import ttk
# # # from PIL import Image, ImageTk
# # # import os

# # # class WellnessWhisperApp:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("Wellness Whisper")
# # #         self.root.geometry("600x800")
# # #         self.root.configure(bg='#fcdede')  # Light peach background color

# # #         # Background image
# # #         background_image_path = os.path.join(os.getcwd(), "C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\healthwealth.jpg")  # Update with your image path
# # #         if os.path.exists(background_image_path):
# # #             self.background_img = Image.open(background_image_path)
# # #             self.background_img = self.background_img.resize((600, 800), Image.ANTIALIAS)
# # #             self.bg_photo = ImageTk.PhotoImage(self.background_img)
# # #             bg_label = tk.Label(self.root, image=self.bg_photo)
# # #             bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # #         # Create the top frame for navigation buttons
# # #         top_frame = tk.Frame(self.root, bg='#fcdede')
# # #         top_frame.pack(side=tk.TOP, fill=tk.X)

# # #         # Create the Sign In, Sign Up, and Settings buttons
# # #         signin_button = tk.Button(top_frame, text="Sign In", font=("Arial", 12), bg='#4CAF50', fg='#ffffff')
# # #         signup_button = tk.Button(top_frame, text="Sign Up", font=("Arial", 12), bg='#2196F3', fg='#ffffff')
# # #         settings_button = tk.Button(top_frame, text="Settings", font=("Arial", 12), bg='#f0ad4e', fg='#ffffff')

# # #         signin_button.pack(side=tk.LEFT, padx=10, pady=10)
# # #         signup_button.pack(side=tk.LEFT, padx=10, pady=10)
# # #         settings_button.pack(side=tk.LEFT, padx=10, pady=10)

# # #         # Create the title label
# # #         title_label = tk.Label(self.root, text="Wellness Whisper", font=("Arial", 24), bg='#fcdede', fg='#333333')
# # #         title_label.pack(pady=20)

# # #         # Create a frame for the round buttons
# # #         button_frame = tk.Frame(self.root, bg='#fcdede')
# # #         button_frame.pack(expand=True)

# # #         # Define the button images and names
# # #         button_info = [
# # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\heart.jpg", "Button 1"),
# # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\diabetes.jpg", "Button 2"),
# # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\parkinsons.jpg", "Button 3"),
# # #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\chatbot1.jpg", "Button 4")
# # #         ]

# # #         # Create round buttons with images and names
# # #         for img_path, name in button_info:
# # #             self.create_round_button(button_frame, img_path, name)

# # #     def create_round_button(self, parent, img_path, name):
# # #         # Load the image
# # #         try:
# # #             img = Image.open(img_path)
# # #             img = img.resize((80, 80), Image.LANCZOS)
# # #             photo = ImageTk.PhotoImage(img)

# # #             # Create a button with image and label
# # #             button = tk.Button(parent, image=photo, text=name, font=("Arial", 12), compound=tk.TOP,
# # #                                bg='#fcdede', fg='#333333', bd=0,
# # #                                command=lambda n=name: self.button_click(n))
# # #             button.image = photo
# # #             button.pack(side=tk.LEFT, padx=20, pady=20)

# # #         except FileNotFoundError as e:
# # #             print(f"Error loading image {img_path}: {e}")

# # #     def button_click(self, name):
# # #         print(f"Button '{name}' clicked!")

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = WellnessWhisperApp(root)
# # #     root.mainloop()
# # import tkinter as tk
# # from tkinter import ttk
# # from PIL import Image, ImageTk
# # import os

# # class WellnessWhisperApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Wellness Whisper")
# #         self.root.geometry("600x800")
# #         self.root.configure(bg='#fcdede')  # Light peach background color

# #         # Background image
# #         background_image_path = os.path.join(os.getcwd(), "C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\healthwealth.jpg")  # Update with your image path
# #         if os.path.exists(background_image_path):
# #             self.background_img = Image.open(background_image_path)
# #             self.background_img = self.background_img.resize((600, 800), Image.LANCZOS)  # Using LANCZOS for resizing
# #             self.bg_photo = ImageTk.PhotoImage(self.background_img)
# #             bg_label = tk.Label(self.root, image=self.bg_photo)
# #             bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# #         # Create the top frame for navigation buttons
# #         top_frame = tk.Frame(self.root, bg='#fcdede')
# #         top_frame.pack(side=tk.TOP, fill=tk.X)

# #         # Create the Sign In, Sign Up, and Settings buttons
# #         signin_button = tk.Button(top_frame, text="Sign In", font=("Arial", 12), bg='#4CAF50', fg='#ffffff')
# #         signup_button = tk.Button(top_frame, text="Sign Up", font=("Arial", 12), bg='#2196F3', fg='#ffffff')
# #         settings_button = tk.Button(top_frame, text="Settings", font=("Arial", 12), bg='#f0ad4e', fg='#ffffff')

# #         signin_button.pack(side=tk.LEFT, padx=10, pady=10)
# #         signup_button.pack(side=tk.LEFT, padx=10, pady=10)
# #         settings_button.pack(side=tk.LEFT, padx=10, pady=10)

# #         # Create the title label
# #         title_label = tk.Label(self.root, text="Wellness Whisper", font=("Arial", 24), bg='#fcdede', fg='#333333')
# #         title_label.pack(pady=20)

# #         # Create a frame for the round buttons
# #         button_frame = tk.Frame(self.root, bg='#fcdede')
# #         button_frame.pack(expand=True)

# #         # Define the button images and names
# #         button_info = [
# #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\heart.jpg", "Button 1"),
# #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\diabetes.jpg", "Button 2"),
# #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\parkinsons.jpg", "Button 3"),
# #             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\chatbot1.jpg", "Button 4")
# #         ]

# #         # Create round buttons with images and names
# #         for img_path, name in button_info:
# #             self.create_round_button(button_frame, img_path, name)

# #     def create_round_button(self, parent, img_path, name):
# #         # Load the image
# #         try:
# #             img = Image.open(img_path)
# #             img = img.resize((80, 80), Image.LANCZOS)  # Using LANCZOS for resizing
# #             photo = ImageTk.PhotoImage(img)

# #             # Create a button with image and label
# #             button = tk.Button(parent, image=photo, text=name, font=("Arial", 12), compound=tk.TOP,
# #                                bg='#fcdede', fg='#333333', bd=0,
# #                                command=lambda n=name: self.button_click(n))
# #             button.image = photo
# #             button.pack(side=tk.LEFT, padx=20, pady=20)

# #         except FileNotFoundError as e:
# #             print(f"Error loading image {img_path}: {e}")

# #     def button_click(self, name):
# #         print(f"Button '{name}' clicked!")

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = WellnessWhisperApp(root)
# #     root.mainloop()
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import os

# class WellnessWhisperApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Wellness Whisper")
#         self.root.geometry("600x800")
#         self.root.configure(bg='#fcdede')  # Light peach background color

#         # Background image
#         background_image_path = os.path.join(os.getcwd(), "C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\healthwealth.jpg")  # Update with your image path
#         if os.path.exists(background_image_path):
#             self.background_img = Image.open(background_image_path)
#             self.background_img = self.background_img.resize((600, 800), Image.LANCZOS)  # Using LANCZOS for resizing
#             self.bg_photo = ImageTk.PhotoImage(self.background_img)
#             bg_label = tk.Label(self.root, image=self.bg_photo)
#             bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         # Create the top frame for navigation buttons
#         top_frame = tk.Frame(self.root, bg='#fcdede')
#         top_frame.pack(side=tk.TOP, fill=tk.X)

#         # Create the Sign In, Sign Up, and Settings buttons
#         signin_button = tk.Button(top_frame, text="Sign In", font=("Arial", 12), bg='#4CAF50', fg='#ffffff')
#         signup_button = tk.Button(top_frame, text="Sign Up", font=("Arial", 12), bg='#2196F3', fg='#ffffff')
#         settings_button = tk.Button(top_frame, text="Settings", font=("Arial", 12), bg='#f0ad4e', fg='#ffffff')

#         signin_button.pack(side=tk.LEFT, padx=10, pady=10)
#         signup_button.pack(side=tk.LEFT, padx=10, pady=10)
#         settings_button.pack(side=tk.LEFT, padx=10, pady=10)

#         # Create the title label
#         title_label = tk.Label(self.root, text="Wellness Whisper", font=("Arial", 24), bg='#fcdede', fg='#333333')
#         title_label.pack(pady=20)

#         # Create a frame for the round buttons
#         button_frame = tk.Frame(self.root, bg='#fcdede')
#         button_frame.pack(expand=True)

#         # Define the button images and names
#         button_info = [
#             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\heart.jpg", "Heart Disease prediction"),
#             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\diabetes.jpg", "Diabetes prediction"),
#             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\parkinsons.jpg", "Parkinson's disease prediction"),
#             ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\chatbot1.jpg", "Chatbot")
#         ]

#         # Create round buttons with images and names in a grid layout
#         row = 0
#         column = 0
#         for img_path, name in button_info:
#             self.create_round_button(button_frame, img_path, name, row, column)
#             column += 1
#             if column == 2:  # Two columns per row
#                 row += 1
#                 column = 0

#     def create_round_button(self, parent, img_path, name, row, column):
#         # Load the image
#         try:
#             img = Image.open(img_path)
#             img = img.resize((80, 80), Image.LANCZOS)  # Using LANCZOS for resizing
#             photo = ImageTk.PhotoImage(img)

#             # Create a button with image and label
#             button = tk.Button(parent, image=photo, text=name, font=("Arial", 12), compound=tk.TOP,
#                                bg='#fcdede', fg='#333333', bd=0,
#                                command=lambda n=name: self.button_click(n))
#             button.image = photo
#             button.grid(row=row, column=column, padx=20, pady=20)

#         except FileNotFoundError as e:
#             print(f"Error loading image {img_path}: {e}")

#     def button_click(self, name):
#         print(f"Button '{name}' clicked!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WellnessWhisperApp(root)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class WellnessWhisperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wellness Whisper")
        self.root.geometry("600x800")
        self.root.configure(bg='#fcdede')  # Light peach background color

        # Background image
        background_image_path = os.path.join(os.getcwd(), "C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\healthwealth.jpg")  # Update with your image path
        if os.path.exists(background_image_path):
            self.background_img = Image.open(background_image_path)
            self.background_img = self.background_img.resize((600, 800), Image.LANCZOS)  # Using LANCZOS for resizing
            self.bg_photo = ImageTk.PhotoImage(self.background_img)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create the top frame for navigation buttons
        top_frame = tk.Frame(self.root, bg='#fcdede')
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # Create the Sign In, Sign Up, and Settings buttons
        signin_button = tk.Button(top_frame, text="Sign In", font=("Arial", 12), bg='#4CAF50', fg='#ffffff')
        signup_button = tk.Button(top_frame, text="Sign Up", font=("Arial", 12), bg='#2196F3', fg='#ffffff')
        settings_button = tk.Button(top_frame, text="Settings", font=("Arial", 12), bg='#f0ad4e', fg='#ffffff')

        signin_button.pack(side=tk.LEFT, padx=10, pady=10)
        signup_button.pack(side=tk.LEFT, padx=10, pady=10)
        settings_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create the title label
        title_label = tk.Label(self.root, text="Wellness Whisper", font=("Arial", 24), bg='#fcdede', fg='#333333')
        title_label.pack(pady=20)

        # Create a frame for the round buttons
        button_frame = tk.Frame(self.root, bg='#fcdede')
        button_frame.pack(expand=True)

        # Define the button images and names
        button_info = [
            ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\heart.jpg", "Heart disease prediction"),
            ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\diabetes.jpg", "Diabetes prediction"),
            ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\parkinsons.jpg", "Parkinson's disease prediction"),
            ("C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\chatbot1.jpg", "Chatbot")
        ]

        # Create round buttons with images and names in a grid layout
        row = 0
        column = 0
        for img_path, name in button_info:
            self.create_round_button(button_frame, img_path, name, row, column)
            column += 1
            if column == 2:  # Two columns per row
                row += 1
                column = 0

    def create_round_button(self, parent, img_path, name, row, column):
        # Load the image
        try:
            img = Image.open(img_path)
            img = img.resize((80, 80), Image.LANCZOS)  # Using LANCZOS for resizing
            photo = ImageTk.PhotoImage(img)

            # Create a button with image and label
            button = tk.Button(parent, image=photo, text=name, font=("Arial", 12), compound=tk.TOP,
                               bg='#fcdede', fg='#333333', bd=0, relief=tk.RAISED,  # Adding relief and bd for outline
                               command=lambda n=name: self.button_click(n))
            button.image = photo
            button.grid(row=row, column=column, padx=20, pady=20)

        except FileNotFoundError as e:
            print(f"Error loading image {img_path}: {e}")

    def button_click(self, name):
        print(f"Button '{name}' clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WellnessWhisperApp(root)
    root.mainloop()
