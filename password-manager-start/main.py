from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Caution!!', message="None of the field can be left blank")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:

            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:

            messagebox.showinfo(title='Confirmation', message='Saved Successfully 😀 ')
            website_text.delete(0, END)
            password_text.delete(0, END)


def search():
    website = website_text.get()
    try:
     with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='File not Found')
    else:
        if website in data:
            email = data [website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        elif len(website) ==0:
            messagebox.showinfo(title="Error", message="Field can't be empty")

        else:
            messagebox.showinfo(title="Error",message=f"No Detail for {website} found")





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)
email_lbl = Label(text="Email/Username:")
email_lbl.grid(row=2, column=0)
password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

website_text = Entry(width=39)
website_text.focus()
website_text.grid(row=1, column=1)

email_text = Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2, sticky=EW)
email_text.insert(0, "abhasucer.it@gmail.com")
password_text = Entry(width=39)
password_text.grid(row=3, column=1)

generate_pwd = Button(text="Generate Password", command=gen_pwd)
generate_pwd.grid(column=2, row=3, sticky=EW)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky=EW)

add = Button(text='Add', width=50, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
