from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
learn = {}
try:
    data = pandas.read_csv('data/to_be_learn.csv',index=False)
except FileNotFoundError:
    gen_data = pandas.read_csv('data/french_words.csv')
    learn = gen_data.to_dict(orient='records')
else:
    learn = data.to_dict(orient='records')


def chng():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def is_known():
    learn.remove(current_card)
    data = pandas.DataFrame(learn)
    data.to_csv('data/to_be_learn.csv')
    chng()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 253, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)
correct_image = PhotoImage(file='images/right.png')
button_correct = Button(image=correct_image, command=chng, highlightthickness=0)

button_correct.grid(row=1, column=1)
wrong_image = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=wrong_image, highlightthickness=0, command=is_known)
button_wrong.grid(row=1, column=0)
chng()
window.mainloop()
