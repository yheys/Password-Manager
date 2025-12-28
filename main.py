from tkinter import *
from  tkinter import messagebox
import random
import pyperclip
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

    if webE == "" or emaE == "" or passE == "" or emaE == "yheyskebede2015@gmail.com":
        messagebox.showinfo(title="Warning", message="You missed something.")
        return

    is_ok = messagebox.askokcancel(
        title="Confirm",
        message=f"Is this all correct?\n\nWebsite: {webE}\nEmail: {emaE}\nPassword: {passE}"
    )

    if is_ok:
        with open("Data.txt", "a") as data:
            data.write(f"{webE} | {passE} | {emaE}\n")

        messagebox.showinfo(
            title="Success",
            message="Password saved successfully!"
        )

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

WEntry=Entry(width=45)
WEntry.grid(column=2,row=3,columnspan=4,sticky="w")

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