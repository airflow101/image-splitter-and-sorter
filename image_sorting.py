import os, sys
from tkinter import *
from PIL import ImageTk, Image

directory_of_images = sys.argv[1]

def main():
    root = Tk()

    #Labels
    myLabel = Label(root, text="Image Sorter")

    #Buttons
    positive_button = Button(root, text = "Positive\n(Cracks)"
    , pady = 10, width = 20, bg = "green", command = positive())
    negative_button = Button(root, text = "Negative\n(No Cracks)"
    , pady = 10, width = 20, bg = "red", command = negative())

    #Positioning
    positive_button.grid(row = 2, column = 0)
    negative_button.grid(row = 2, column = 3)

    root.mainloop()

def positive():
    return

def negative():
    return

if __name__ == "__main__":
    main()
