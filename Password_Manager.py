from tkinter import *
from tkinter import messagebox
import random
#--------------------------------------Random Password Generator---------------------------------------------#
Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def generate_random_pass():
    password=""
    password_entry.delete(0,END)
    random_list_alpha=[Alphabets[random.randint(0,24)] for _ in range(0,6)]
    random_list_no=[Numbers[random.randint(0,8)] for _ in range(0,4)]

    new_list=random_list_alpha+random_list_no
    password= ""
    for i in range(0,10):
      password+=str(new_list[random.randint(0,8)])
    password_entry.insert(0,password)
    

#--------------------------------------Function Add Password-------------------------------------------------#
def add_password():
 if entry_website.get() and password_entry.get() != "":
    website=entry_website.get()
    password=password_entry.get()
    add_data(website,password)

 else:
    messagebox.showinfo(title="Password Manager",message="Empty Fields")

#----------------------------------------Create File---------------------------------------------------------#
def add_data(website,password):
 is_ok= messagebox.askokcancel(title="Confirm",message="Do u wish to Save the Password")
 if is_ok:
   with open("data.txt","w") as file:
    file.write(f"{website} | {entry_email.get()} | {password}\n")
    entry_website.delete(0,END)
    password_entry.delete(0,END)
 else:
   pass
#--------------------------------------UI Setup -------------------------------------------------------------#
window=Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)
logo_img=PhotoImage(file="./Downloads/logo.png")
canvas=Canvas(height=200,width=200)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#------------------------------------------Components---------------------------------------------------------#
Label_website=Label(text="Website")
Label_website.grid(row=1,column=0)

entry_website=Entry(width=35)
entry_website.grid(row=1,column=1,columnspan=2)
entry_website.focus()

email_lable=Label(text="Email")
email_lable.grid(row=2,column=0)
entry_email=Entry(width=35)
entry_email.grid(row=2,column=1,columnspan=2)
entry_email.insert(0,"user@gmail.com")

password_lable=Label(text="Password")
password_lable.grid(row=3,column=0)
password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

generate_password_button=Button(text="Generate Pasword",command=generate_random_pass)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=30,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)

#-----------------------------------------------------------------------------------------------------------------#
window.mainloop()

 




















