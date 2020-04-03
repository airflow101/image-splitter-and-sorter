import os, sys, shutil
import random
from PIL import Image

directory = sys.argv[1]
PICK_AMOUNT = int(sys.argv[2])
FOLDER_NAME = "Picked"
destination = os.path.join(directory, FOLDER_NAME)

if not os.path.exists(destination):
    os.mkdir(destination)

filenames = []

for filename in os.listdir(directory):
    if filename.endswith(".JPG") or filename.endswith(".jpg"):
        filenames.append(filename)

random.seed(18)
chosen = random.sample(filenames, PICK_AMOUNT)

for filename in chosen:
    shutil.copy2(os.path.join(directory, filename), destination)
