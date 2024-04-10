# --------------UI------------------------
from tkinter import *

window = Tk()
window.minsize(height=600, width=600)
window.config(padx=50,pady=50)

# image canvas
canvas = Canvas(width=200, height=200)  # Adjust canvas size
image = PhotoImage(file="logo.png")  # Provide the complete file path
canvas.create_image(100, 100, image=image)  # Adjust image coordinates
canvas.grid(row=0,column=1)

# website label
website_label = Label(text="Website :")
website_label.grid(column=0,row=1)

# website text
website_field = Entry(width=40)
website_field.grid(row=1,column=1,sticky="w")
website_field.focus()

# email label
email_label = Label(text="Email :")
email_label.grid(column=0,row=2)

# email text
email_field = Entry(width=53)
email_field.grid(row=2,column=1,sticky="w")
email_field.insert(0,"np968738@gmail.com")

# password label
password_label = Label(text="Password :")
password_label.grid(column=0,row=3)

# password text
password_field = Entry(width=25)
password_field.grid(row=3,column=1,sticky="w")

# passowrd_generate button
password_button = Button(text="Generate Password",width=20)
password_button.grid(row=3,column=1,sticky="e")

# add function
def on_click():
    website_name = website_field.get()
    print(website_name)
    email_text = email_field.get()
    print(email_text)
    password_text = password_field.get()
    print(password_text)

# add button button
add_button = Button(text="ADD",width=45,command=on_click)
add_button.grid(row=4,column=1,sticky="w")

window.mainloop()

# ------------Password Generate-----------

# --------------Add Data to file----------