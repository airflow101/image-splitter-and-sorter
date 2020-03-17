import os, sys, shutil
from tkinter import *
from PIL import ImageTk, Image

directory_of_images = sys.argv[1]

filenames_list = []
for filename in os.listdir(directory_of_images):
    if (not filename.endswith("_n.JPG")) and (not filename.endswith("_p.JPG")) and (not filename.endswith("_p.jpg")) and (not filename.endswith("_n.jpg")) and (filename.endswith(".JPG") or filename.endswith(".jpg")):
        filenames_list.append(filename)

number_of_files = len(filenames_list)
current_files = 0

folder_of_positive = "Positive"
folder_of_negative = "Negative"

directory_of_positive = os.path.join(directory_of_images, folder_of_positive)
directory_of_negative = os.path.join(directory_of_images, folder_of_negative)

if not os.path.exists(directory_of_positive):
    os.mkdir(directory_of_positive)

if not os.path.exists(directory_of_negative):
    os.mkdir(directory_of_negative)

#Root
root = Tk()
root.title("Image Sorting")

#Image Viewer
image = 0
image_view = 0

#Label
number_indicator = Label(text = "Images left =\n" + str(number_of_files))
file_indicator = Label(text = "Filename:\n" + str(filenames_list[current_files])[:-4])

def refresh_status():
    global file_indicator
    global number_indicator
    file_indicator.grid_forget()
    number_indicator.grid_forget()
    number_indicator = Label(text = "Images left =\n" + str(number_of_files))
    file_indicator = Label(text = "Filename:\n" + str(filenames_list[current_files])[:-4])
    file_indicator.grid(row = 3 ,column = 0)
    number_indicator.grid(row = 3, column = 1)

def change_image(index):
    global image
    global image_view
    image = ImageTk.PhotoImage(Image.open(os.path.join(directory_of_images
    , filenames_list[index])))
    image_view = Label(image = image)
    image_view.grid(row = 0, column = 0, columnspan = 2)

change_image(current_files)

def insert_indicator(indicator):
    filename = filenames_list[current_files]
    index = filename.find('.')
    return filename[:index] + indicator + filename[index:]

def copy_to(directory_of_transfer, indicator):
    shutil.copy2(os.path.join(directory_of_images, filenames_list[current_files]),
    directory_of_transfer)
    os.rename(os.path.join(directory_of_images, filenames_list[current_files])
    , os.path.join(directory_of_images, insert_indicator(indicator)))

def positive():
    global image_view
    global current_files
    global number_of_files
    image_view.grid_forget()
    copy_to(directory_of_positive, "_p")
    filenames_list.pop(current_files)
    number_of_files -= 1
    if number_of_files == current_files:
        current_files = 0
    refresh_status()
    change_image(current_files)

def negative():
    global image_view
    global current_files
    global number_of_files
    image_view.grid_forget()
    copy_to(directory_of_negative, "_n")
    filenames_list.pop(current_files)
    number_of_files -= 1
    if number_of_files == current_files:
        current_files = 0
    refresh_status()
    change_image(current_files)

def next():
    global image_view
    global current_files
    image_view.grid_forget()
    current_files =  (current_files + 1) % number_of_files
    change_image(current_files)
    return

def previous():
    global image_view
    global current_files
    image_view.grid_forget()
    if current_files == 0:
        current_files = number_of_files - 1
    else:
        current_files -= 1
        current_files %= number_of_files
    change_image(current_files)
    return

#Buttons
positive_button = Button(root, text = "Positive\n(Cracks)"
, pady = 5, width = 15, bg = "green", command = positive)
negative_button = Button(root, text = "Negative\n(No Cracks)"
, pady = 5, width = 15, bg = "red", command = negative)

next_button = Button(root, text = "Next >"
, pady = 5, width = 15, command = next)
previous_button = Button(root, text = "Previous <"
, pady = 5, width = 15, command = previous)

#Positioning
positive_button.grid(row = 1, column = 0)
negative_button.grid(row = 1, column = 1)
next_button.grid(row = 2, column = 1)
previous_button.grid(row = 2, column = 0)
file_indicator.grid(row = 3 ,column = 0)
number_indicator.grid(row = 3, column = 1)

root.mainloop()
