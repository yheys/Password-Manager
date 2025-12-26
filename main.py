from tkinter import *
#-----------------------pasdword generstor----------------------#
#-----------------------save  passdword----------------------#





#-----------------------ui setup----------------------#

window=Tk()
window.minsize(600,600)
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=300,height=300)
lock=PhotoImage(file="lock.png")
canvas.create_image(170,170,image=lock)
canvas.grid(column=2,row=1,columnspan=4)

website=Label(text="Website:")
website.grid(column=1,row=2,sticky="e")
website.focus()


email=Label(text="Email/Username:")
email.grid(column=1,row=3,sticky="e")

password=Label(text="Password:")
password.grid(column=1,row=4,sticky="e")

add=Button(text="Add",width=36)
add.grid(row=5,column=2,columnspan=4,sticky="w")

generator=Button(text="Generate Password")
generator.grid(row=4,column=3,sticky="w")

WEntry=Entry(width=45)
WEntry.grid(column=2,row=2,columnspan=4,sticky="w")

EEntry=Entry(width=45)
EEntry.grid(column=2,row=3,columnspan=4,sticky="w")
EEntry.insert(0,"yheyskebede2015@gmail.com")

WEntry=Entry(width=20)
WEntry.grid(column=2,row=4,sticky="w")











window.mainloop()