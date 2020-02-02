import os, sys
from tkinter import *
from PIL import ImageTk, Image

directory_of_images = sys.argv[1]

def main():
    #Root
    root = Tk()
    root.title("Image Sorting")

    #Buttons
    positive_button = Button(root, text = "Positive\n(Cracks)"
    , pady = 5, width = 15, bg = "green", command = positive())
    negative_button = Button(root, text = "Negative\n(No Cracks)"
    , pady = 5, width = 15, bg = "red", command = negative())

    #Image Viwer
    image = ImageTk.PhotoImage(Image.open("Result_227\IMG_0056_00.JPG"))
    image_view = Label(image = image)

    #Positioning
    image_view.grid(row = 0, column = 0, columnspan = 2)
    positive_button.grid(row = 1, column = 0)
    negative_button.grid(row = 1, column = 1)

    root.mainloop()

def positive():
    return

def negative():
    return

if __name__ == "__main__":
    main()
