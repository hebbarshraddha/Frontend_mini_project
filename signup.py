
from tkinter import *
from tkinter import messagebox  # Added import for messagebox
from PIL import Image, ImageTk
import ast

window=Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False,False)

# def signup():
#     usern=user.get()
#     passw=password.get()
#     confpassw=confpassword.get()

#     if passw==confpassw:
#         try:
#             file=open('')

# img=PhotoImage(file="signup.jpg")
# Label(window,image=img,border=0,bg='white').place(x=50,y=90)
image_path = 'C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\signup.jpg'
image = Image.open(image_path)
img = ImageTk.PhotoImage(image)

# Place the image on the window
Label(window, image=img, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
####---------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=="":
        user.insert(0,"Username")    

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light', 11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
##########----------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    if password.get()=="":
        password.insert(0,"Password")    

password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light', 11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
######---
def on_enter(e):
    confpassword.delete(0,'end')
def on_leave(e):
    if confpassword.get()=="":
        confpassword.insert(0,"Confirm Password")    

confpassword=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light', 11))
confpassword.place(x=30,y=220)
confpassword.insert(0,' Confirm Password')
confpassword.bind('<FocusIn>',on_enter)
confpassword.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

######---
Button(frame,width=39,pady=7,text="Sign Up",bg='#57a1f8',fg='white',border=0).place(x=35,y=280)
label=Label(frame,text="I have an account",fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)

window.mainloop()



