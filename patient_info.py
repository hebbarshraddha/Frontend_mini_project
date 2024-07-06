# from tkinter import *
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk
# import pathlib
# from datetime import date
# import os
# from tkinter.ttk import Combobox
# import openpyxl, xlrd
# from openpyxl import Workbook


# root = Tk()
# root.title("Wellness Whisper!")
# root.geometry("1250x700+210+100")
# root.config(bg="#06283D")

# # Check if the Excel file exists, if not create it with headers
# file = pathlib.Path("User_data.xlsx")
# if not file.exists():
#     from openpyxl import Workbook
#     workbook = Workbook()
#     sheet = workbook.active
#     sheet['A1'] = "User Name"
#     sheet['B1'] = "Gender"
#     sheet['C1'] = "Email"
#     sheet['D1'] = "Age"
#     sheet['E1'] = "DOB"
#     workbook.save('User_data.xlsx')

# #gender
# def selection():
#     value=radio.get()
#     if value==1:
#         gender="Male"
#         print(gender) 
#     else:
#         gender="Female"
#         print(gender)        

# # Top frames
# Label(root, text="Email: wellnesswhisper@gmail.com", bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
# Label(root, text="USER DETAILS", bg="#c36464", fg="#fff", font='arial 20 bold').pack(side=TOP, fill=X)

# # Search box
# Search = StringVar()
# Entry(root, textvariable=Search, width=15, bd=2, font='arial 20').place(x=820, y=70)

# # Load and resize the search image
# search_image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\HealthTipGeneratorpython\\images\\search.jpg'  # Update this path
# search_image = Image.open(search_image_path)
# search_image = search_image.resize((30, 30), Image.LANCZOS)  # Resize as needed
# search_img = ImageTk.PhotoImage(search_image)

# # Place the search button
# search_button = Button(root, text="Search", compound=LEFT, image=search_img, width=123, bg='#68ddfa', font="arial 13 bold")
# search_button.place(x=1060, y=66)

# # Load and resize the setting image
# setting_image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\HealthTipGeneratorpython\\images\\setting.jpg'  # Update this path
# setting_image = Image.open(setting_image_path)
# setting_image = setting_image.resize((30, 30), Image.LANCZOS)  # Resize as needed
# setting_img = ImageTk.PhotoImage(setting_image)

# # Place the setting button
# setting_button = Button(root, image=setting_img, bg='#c36464')
# setting_button.place(x=110, y=64)

# # Keep a reference to the images to prevent garbage collection
# root.search_img = search_img
# root.setting_img = setting_img

# ##-------
# framebg = "#EDEDED"  # Define the color for framebg if not defined
# background = "#06283D"  # Define the color for background if not defined
# Label(root,text='User name:',font='arial 13',fg=framebg,bg=background).place(x=30,y=150)
# # Label(root,text='Gender:',font='arial 13',fg=framebg,bg=background).place(x=500,y=150)

# Username=StringVar()
# # Gender=StringVar()

# user_entry=Entry(root,textvariable=Username,width=15,font='arial 10')
# user_entry.place(x=160,y=150)

# # gender_entry=Entry(root,textvariable=Gender,width=15,font='arial 10')
# # gender_entry.place(x=570,y=150)

# ###------
# framefg='black'
# obj=LabelFrame(root,text="User details",font=20,bd=2,width=900,bg=framebg,fg=framefg,height=250,relief=GROOVE)
# obj.place(x=30,y=200)

# Label(obj,text="Full name:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=30)
# Label(obj,text="Gender:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=70)
# Label(obj,text="DOB:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=120)
# Label(obj,text="email",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=160)
# Label(obj,text="Age:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=200)

# Name=StringVar()
# name_entry=Entry(obj,textvariable=Name,width=20,font='arial 10')
# name_entry.place(x=150,y=30)

# DOB=StringVar()
# dob_entry=Entry(obj,textvariable=DOB,width=20,font='arial 10')
# dob_entry.place(x=150,y=120)

# email=StringVar()
# email_entry=Entry(obj,textvariable=email,width=20,font='arial 10')
# email_entry.place(x=150,y=160)

# Age=StringVar()
# age_entry=Entry(obj,textvariable=Age,width=20,font='arial 10')
# age_entry.place(x=150,y=200)







# radio=IntVar()
# R1=Radiobutton(obj,text="Male",variable=radio,value=1,bg=framebg,fg=framefg,command=selection)
# R1.place(x=150,y=70)

# R2=Radiobutton(obj,text="Female",variable=radio,value=1,bg=framebg,fg=framefg,command=selection)
# R2.place(x=150,y=90)



# f=Frame(root,bd=3,bg='black',width=200,height=200,relief=GROOVE)
# f.place(x=1000,y=150)

# # img=PhotoImage(file="C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\HealthTipGeneratorpython\\images\\profile.jpg")
# # lbl=Label(root,bg='black',image=img)
# # lbl.place(x=0,y=0)

# # Load the image using Pillow
# # image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\HealthTipGeneratorpython\\images\\profile.jpg'
# # image = Image.open(image_path)
# # img = ImageTk.PhotoImage(image)
# image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\HealthTipGeneratorpython\\images\\profile.jpg'
# image = Image.open(image_path)
# img = ImageTk.PhotoImage(image)

# # Create a frame
# f = root.Frame(root, bg='black')
# f.pack(fill='both', expand=True)

# # Place the image on the window
# label = root.Label(f, image=img, bg='black')
# label.place(x=0, y=0)
# # Place the image on the window
# # Label(f,root, image=img, bg='black').place(x=0, y=0)



















# root.mainloop()
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pathlib
from datetime import date
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook


root = Tk()
root.title("Wellness Whisper!")
root.geometry("1250x700+210+100")
root.config(bg="#06283D")

# Check if the Excel file exists, if not create it with headers
file = pathlib.Path("User_data.xlsx")
if not file.exists():
    from openpyxl import Workbook
    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = "User Name"
    sheet['B1'] = "Gender"
    sheet['C1'] = "Email"
    sheet['D1'] = "Age"
    sheet['E1'] = "DOB"
    workbook.save('User_data.xlsx')

#Exit
def Exit():
    root.destroy()


#gender
def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
        print(gender)
    else:
        gender = "Female"
        print(gender)

# Top frames
Label(root, text="Email: wellnesswhisper@gmail.com", bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="USER DETAILS", bg="#c36464", fg="#fff", font='arial 20 bold').pack(side=TOP, fill=X)

# Search box
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font='arial 20').place(x=820, y=70)

# Load and resize the search image
search_image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\search.jpg'
search_image = Image.open(search_image_path)
search_image = search_image.resize((30, 30), Image.LANCZOS)  # Resize as needed
search_img = ImageTk.PhotoImage(search_image)

# Place the search button
search_button = Button(root, text="Search", compound=LEFT, image=search_img, width=123, bg='#68ddfa', font="arial 13 bold")
search_button.place(x=1060, y=66)

# Load and resize the setting image
setting_image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\setting.jpg'
setting_image = Image.open(setting_image_path)
setting_image = setting_image.resize((30, 30), Image.LANCZOS)  # Resize as needed
setting_img = ImageTk.PhotoImage(setting_image)

# Place the setting button
setting_button = Button(root, image=setting_img, bg='#c36464')
setting_button.place(x=110, y=64)

# Keep a reference to the images to prevent garbage collection
root.search_img = search_img
root.setting_img = setting_img

# Define framebg and background colors
framebg = "#EDEDED"
background = "#06283D"

Label(root, text='User name:', font='arial 13', fg=framebg, bg=background).place(x=30, y=150)

Username = StringVar()
user_entry = Entry(root, textvariable=Username, width=15, font='arial 10')
user_entry.place(x=160, y=150)

framefg = 'black'
obj = LabelFrame(root, text="User details", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Full name:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=30)
Label(obj, text="Gender:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=70)
Label(obj, text="DOB:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=120)
Label(obj, text="email", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=160)
Label(obj, text="Age:", font="arial 13", bg=framebg, fg=framefg).place(x=30, y=200)

Name = StringVar()
name_entry = Entry(obj, textvariable=Name, width=20, font='arial 10')
name_entry.place(x=150, y=30)

DOB = StringVar()
dob_entry = Entry(obj, textvariable=DOB, width=20, font='arial 10')
dob_entry.place(x=150, y=120)

email = StringVar()
email_entry = Entry(obj, textvariable=email, width=20, font='arial 10')
email_entry.place(x=150, y=160)

Age = StringVar()
age_entry = Entry(obj, textvariable=Age, width=20, font='arial 10')
age_entry.place(x=150, y=200)

radio = IntVar()
R1 = Radiobutton(obj, text="Male", variable=radio, value=1, bg=framebg, fg=framefg, command=selection)
R1.place(x=150, y=70)

R2 = Radiobutton(obj, text="Female", variable=radio, value=2, bg=framebg, fg=framefg, command=selection)
R2.place(x=150, y=90)

# Create a frame for the profile image
f = Frame(root, bd=3, bg='black', width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

# Load the profile image using Pillow
image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\profile.jpg'
image = Image.open(image_path)
image = image.resize((200, 200), Image.LANCZOS)  # Resize the image to fit the frame
img = ImageTk.PhotoImage(image)

# Place the image on the window
label = Label(f, image=img, bg='black')
label.place(x=0, y=0)


#buttom
Button(root,text="Upload",width=19,height=2,font='arial 12 bold',bg='lightblue').place(x=1000,y=370)
saveButton=Button(root,text="Save",width=19,height=2,font='arial 12 bold',bg='lightgreen').place(x=1000,y=450)
resetButton=Button(root,text="Reset",width=19,height=2,font='arial 12 bold',bg='lightpink').place(x=1000,y=530)
ExitButton=Button(root,text="Exit",width=19,height=2,font='arial 12 bold',bg='grey',command=Exit).place(x=1000,y=610)









# Start the main event loop
root.mainloop()
