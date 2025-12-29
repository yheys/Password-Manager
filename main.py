from tkinter import *
from  tkinter import messagebox
import random
import pyperclip
import json


#-----------------------password generator ----------------------#
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-="

    password = ""
    for _ in range(8):
        password += random.choice(letters + numbers + symbols)

    PEntry.delete(0, END)
    PEntry.insert(0, password)
    pyperclip.copy(password)


#-----------------------save  password ----------------------#
def Save():
    webE = WEntry.get()
    emaE = EEntry.get()
    passE = PEntry.get()
    new_data={
        webE:
            {"Email":emaE,
             "Password":passE
            }
    }

    if webE == "" or emaE == "" or passE == "" or emaE == "yheyskebede2015@gmail.com":
        messagebox.showinfo(title="Warning", message="You missed something.")
        return

    is_ok = messagebox.askokcancel(
        title="Confirm",
        message=f"Is this all correct?\n\nWebsite: {webE}\nEmail: {emaE}\nPassword: {passE}"
    )

    if is_ok:
        try:
            with open("Data.json", "r") as data:
                file=json.load(data)
                file.update(new_data)
            with open("Data.json", "w") as data:
                json.dump(file, data, indent=4)
        except:
            with open("Data.json", "w") as data:
                    json.dump(new_data, data, indent=4)


        WEntry.delete(0, END)
        PEntry.delete(0, END)
        EEntry.delete(0, END)
        messagebox.showinfo(title = "Success",message = "Password saved successfully!")


#----------------------------- search ----------------------#
def search():
    webE = WEntry.get()
    try:
        with open("Data.json", "r") as data:
            file = json.load(data)
    except:
        messagebox.showinfo(title=f"Error", message=f"Sorry!No data File Found.")
    else:
        if webE in file:
            messagebox.showinfo(title=f"{webE}",message=f"Email: {file[webE]['Email']}\n Password:{file[webE]['Password']}" )
        else:
            messagebox.showinfo(title=f"Error",message=f"Sorry,No information about {webE}.")

    WEntry.delete(0, END)
    PEntry.delete(0, END)
    EEntry.delete(0, END)


#-----------------------ui setup----------------------#

window=Tk()
window.minsize(600,600)
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=500,height=500,)
lock=PhotoImage(file="lock.png")
canvas.create_image(250,250,image=lock)
canvas.grid(column=2,row=1,columnspan=4,sticky="w")

website=Label(text="Website:")
website.grid(column=1,row=3,sticky="e")
website.focus()



email=Label(text="Email/Username:")
email.grid(column=1,row=4,sticky="e")

password=Label(text="Password:")
password.grid(column=1,row=5,sticky="e")

add=Button(text="Add",width=36,command=Save)
add.grid(row=6,column=2,columnspan=4,sticky="w")

generator=Button(text="Generate Password",command=generate_password)
generator.grid(row=5,column=3,sticky="e")

search=Button(text="Search",width=15,command=search)
search.grid(row=3,column=3,sticky="e")

WEntry=Entry(width=30)
WEntry.grid(column=2,row=3,columnspan=3,sticky="w")

EEntry=Entry(width=45)
EEntry.grid(column=2,row=4,columnspan=4,sticky="w")
EEntry.insert(0,"yheyskebede2015@gmail.com")

PEntry=Entry(width=25)
PEntry.grid(column=2, row=5, columnspan=2, sticky="w")

warning=Label(text="You miss something",fg="red")
warning.grid(column=2,row=2)
warning.grid_remove()

confirm=Label(text="You Successfully Added the Password.",fg="green")
confirm.grid(column=2,row=2)
confirm.grid_remove()











window.mainloop()