# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import pyperclip
from random import randint, choice, shuffle
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save():

    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{"email":email,"password":password}}

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 :
          messagebox.showinfo(title="Oops",message="Please do not leave any fields empty!")

    else:
        # To read the json file and update it.
        try:
            with open ("../python-projects/PROJECT-29/data.json","r") as file:
                data=json.load(file)
        except FileNotFoundError:
            with open ("../python-projects/PROJECT-29/data.json","w") as new_file:
                json.dump(new_data,new_file,indent=4)
        
        # To write the updated data into json file.
        else:
            data.update(new_data)
            with open("../python-projects/PROJECT-29/data.json","w") as write_file:
                json.dump(data,write_file,indent=4)

        finally:
            website_entry.delete(0,"end")
            password_entry.delete(0,"end")
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website=website_entry.get()
    try:
        with open("../python-projects/PROJECT-29/data.json","r") as read_file:
            data_dict=json.load(read_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data_dict:
            email=data_dict[website]["email"]
            password=data_dict[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        
        else:
            messagebox.showinfo(title="Oops",message=f"Details of {website} doesn't exist.")

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=Canvas(width=200,height=200)
project_image=PhotoImage(file="../python-projects/PROJECT-29/logo.png")
canvas.create_image(100,100,image=project_image)

canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry=Entry(width=30)
website_entry.grid(row=1,column=1)
website_entry.focus()

search_button=Button(text="Search",command=find_password,width=15)
search_button.grid(row=1,column=2)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry=Entry(width=49)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "lucky@gmail.com")

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry=Entry(width=30)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="Generate Password",command=generate_password,width=15)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=42,command=Save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()