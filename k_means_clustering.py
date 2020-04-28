import numpy as np
import cv2
import os, sys, shutil

directory_of_images = sys.argv[1]

FOLDER_NAME = "Result"
destination = os.path.join(directory_of_images, FOLDER_NAME)

if not os.path.exists(destination):
    os.mkdir(destination)

filenames_list = []
for filename in os.listdir(directory_of_images):
    if (not filename.endswith("_n.JPG")) and (not filename.endswith("_p.JPG")) and (not filename.endswith("_p.jpg")) and (not filename.endswith("_n.jpg")) and (filename.endswith(".JPG") or filename.endswith(".jpg")):
        filenames_list.append(filename)

def kmc(filename):
    img = cv2.imread(os.path.join(directory_of_images, filename), -1)
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    current_file, file_format = os.path.splitext(filename)
    filename_saved = current_file + "_K_Means_C" + file_format

    cv2.imwrite(os.path.join(destination, filename_saved), res2)

    numpy_horizontal = np.hstack((img, res2))

    filename_saved = current_file + "_KMC_Combined" + file_format
    cv2.imwrite(os.path.join(destination, filename_saved), numpy_horizontal)

for filename in filenames_list:
    kmc(filename)
