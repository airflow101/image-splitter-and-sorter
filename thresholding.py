import cv2
import os, sys, shutil
import numpy as np
from matplotlib import pyplot as plt

directory_of_images = sys.argv[1]

FOLDER_NAME = "Result"
destination = os.path.join(directory_of_images, FOLDER_NAME)

if not os.path.exists(destination):
    os.mkdir(destination)

filenames_list = []
for filename in os.listdir(directory_of_images):
    if (not filename.endswith("_n.JPG")) and (not filename.endswith("_p.JPG")) and (not filename.endswith("_p.jpg")) and (not filename.endswith("_n.jpg")) and (filename.endswith(".JPG") or filename.endswith(".jpg")):
        filenames_list.append(filename)

def thresholding(filename):
    img = cv2.imread(os.path.join(directory_of_images, filename), -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Otsu's thresholding
    ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # plot all the images and their histograms
    images = [img, 0, th2]
    titles = ['Original Image','Histogram',"Processed Image"]

    current_file, file_format = os.path.splitext(filename)
    filename_saved = current_file + "_Thresholded" + file_format

    cv2.imwrite(os.path.join(destination, filename_saved), th2)

    grey_3_channel = cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR)
    numpy_horizontal = np.hstack((img, grey_3_channel))

    filename_saved = current_file + "_Combined" + file_format
    cv2.imwrite(os.path.join(destination, filename_saved), numpy_horizontal)


    for i in range(1):
        plt.subplot(1,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(1,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(1,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.savefig(os.path.join(destination, filename))


for filename in filenames_list:
    thresholding(filename)
