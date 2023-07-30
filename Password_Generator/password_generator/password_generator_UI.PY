from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from time import sleep
import customtkinter
import random
import string
import os


letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
hex_chars = string.hexdigits

PASSWORD_LENGTH = 15

def add_to_clipboard(text):
    command = "echo " + text.strip() + "| clip"
    os.system(command)


def generator():
    password = ""
    while len(password) < PASSWORD_LENGTH:
        password += random.choice(letters + digits + hex_chars + punctuation)
    password_label["text"] = password

    add_to_clipboard(password)
    sleep(1)
    messagebox.showinfo("","Copied!")


def multiples_generates(): 
    password = ""
    num_entry = int(multigen_entry.get())
    sleep(1)

    try:
        messagebox.showinfo("","Archive Created!")

        with open("Passwords.txt", "a") as psw:
            i=1
            while i <= num_entry:
                # Combine all character sets and shuffle them
                all_chars = list(letters + digits + hex_chars + punctuation)
                random.shuffle(all_chars)

                # Generate a password using the shuffled characters
                password = "".join(random.choice(all_chars) for _ in range(PASSWORD_LENGTH))
                psw.write(f"{password}\n")

                i += 1
    except ValueError:
        messagebox.showinfo("","Invalid value!")


#------------------------------UI1config
#--------------------------window
root = Tk()
root.title("PassGenUI")
root.geometry("200x350")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.iconbitmap(r"img\icon\key.ico")
root.configure(background="#141414")
root.eval("tk::PlaceWindow . center")
#--------------------------window

#--------------------------theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
#--------------------------theme
#------------------------------UI1config


#----------------------------------widgets
#------------------------------Label
password_label = Label(
    root,
    text="",
    font="Consolas 13",
    fg="#22ff00",
    background="black",
    relief="solid",
    height=5,
    width=20
)
password_label.grid(
    column=0,
    row=0
)
#------------------------------Label

#------------------------------entry
multigen_entry = customtkinter.CTkEntry(
    root,
    text_color="#22ff00",
    font=customtkinter.CTkFont(family="<Consolas>", size=14),
    fg_color="black",
    placeholder_text="    quantity ",
    width=100
)
multigen_entry.grid(
    column=0,
    row=1,
    padx=10,
    pady=(20,20)
)
#------------------------------entry

#------------------------------ctkbutton
multigen_ctkbutton = customtkinter.CTkButton(
    root,
    text="Multiple Passwords",
    font=customtkinter.CTkFont(family="<Consolas>", size=14),
    command=multiples_generates,
    height=35,
    width=150
)
multigen_ctkbutton.grid(
    column=0,
    row=2,
    padx=20,
    pady=(10,20)    
)
#------------------------------ctkbutton

#------------------------------ctkbutton
generate_ctkbutton = customtkinter.CTkButton(
    root,
    text="Generate",
    font=customtkinter.CTkFont(family="<Consolas>", size=14),
    command=generator,
    height=35,
    width=150
)
generate_ctkbutton.grid(
    column=0,
    row=3,
    padx=10,
    pady=(10,20)
)
#------------------------------ctkbutton
#----------------------------------widgets

#--------------windowstart
root.mainloop()

