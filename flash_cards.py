import pandas as pd
from tkinter import *
from random import randint
##B1DDC6
#4AA47B
FONT = ('Arial', 50, 'normal')
BACKGROUND_COLOR = "#4AA47B"
MAX_RANGE = 997
#setting up a screen
screen = Tk()
screen.title('Russian Flashcards')
screen.configure(background = BACKGROUND_COLOR, padx = 50, pady = 50)

#imported images
flashcard_back = PhotoImage(file = 'images/card_back.png')
flashcard_front = PhotoImage(file='images/card_front.png')
right =  PhotoImage(file='images/right1.png')
wrong =  PhotoImage(file='images/wrong1.png')

#imported csv
data = pd.read_csv("russian.csv")
data = data.to_dict(orient="records")

#first word
index = randint(1,MAX_RANGE)
pair = data[index]
# --------------------- FILL ------------------- #
def fill(card, language, dictionary):
    canvas.delete('all')
    canvas.create_image(400, 300, image = card)
    canvas.create_text(380, 150, font = FONT, text = language)
    canvas.create_text(380, 300, font = ('Arial', 50, 'bold'), text = dictionary)

# --------------------- DICTIONARY UPDATE ------ #
def update(indexing):
    global data
    data.remove(data[indexing])
    data = pd.DataFrame(data)
    data.to_csv("russian.csv", index = False)
    data = pd.read_csv("russian.csv")
    data = data.to_dict(orient = "records")
# --------------------- CHANGE ----------------- #
def change_and_forward():
    global pair, index, MAX_RANGE
    update(index)
    MAX_RANGE -= 1
    index = randint(1,MAX_RANGE)
    pair = data[index]
    fill(flashcard_front,'Russian', pair['Russian'])
    screen.after(3000, flash)

def change():
    global pair, index
    index = randint(1,MAX_RANGE)
    pair = data[index]
    fill(flashcard_front,'Russian', pair['Russian'])
    screen.after(3000, flash)
# --------------------- FLASH ------------------ #
def flash():
    global pair
    fill(flashcard_back, 'English', pair['English'])
# --------------------- SET UP ----------------- #
#Canvas
canvas = Canvas()
canvas = Canvas(width = 800, height = 600, bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 3)
fill(flashcard_front, 'Russian', pair['Russian'])

#Button for the right answer
right_button = Button(width = 100, height = 100, image = right,
                      bg = BACKGROUND_COLOR, highlightthickness = 0, command = change_and_forward)
right_button.grid(row = 2, column = 0, padx = 5, pady = 5)

#Button for the wrong answer
wrong_button = Button(width = 100, height = 100, image = wrong,
                      bg = BACKGROUND_COLOR, highlightthickness = 0, command = change)
wrong_button.grid(row = 2, column = 2, padx = 5, pady = 5)

screen.after(3000, flash)
   
screen.mainloop()