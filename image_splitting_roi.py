import os, sys
import cv2
from PIL import Image

split_dimension = int(sys.argv[1])
directory_of_originals = sys.argv[2]
directory_of_results = sys.argv[3]
if not os.path.exists(directory_of_results):
    os.mkdir(directory_of_results)

folder_of_positive = "Positive"
folder_of_negative = "Negative"

directory_of_positive = os.path.join(directory_of_results, folder_of_positive)
directory_of_negative = os.path.join(directory_of_results, folder_of_negative)

if not os.path.exists(directory_of_positive):
    os.mkdir(directory_of_positive)

if not os.path.exists(directory_of_negative):
    os.mkdir(directory_of_negative)

def split_image(directory, filename):
    directory = os.path.join(directory_of_originals, filename)
    current_file, file_format = os.path.splitext(filename)
    print(directory)
    im = cv2.imread(directory)
    height_im, width_im, channels = im.shape
    height_im_show = height_im //8
    width_im_show = width_im //8

    # Select ROI
    cv2.namedWindow("Image",2)
    cv2.resizeWindow("Image", width_im_show, height_im_show)
    r = cv2.selectROI("Image", im, True, False)

    imCrop = im[(int(r[1])):(int(r[1]+r[3])), (int(r[0])):(int(r[0]+r[2]))]

    #Positive
    width = imCrop.shape[0]
    height = imCrop.shape[1]
    print(imCrop.size)
    for x in range(0, width, split_dimension):
        for y in range(0, height,  split_dimension):
            box = (x, y, x + split_dimension, y + split_dimension)
            # result_im = imCrop.crop(box)
            result_im = imCrop[x:(x+split_dimension), y:(y+split_dimension)]
            filename_result = current_file + "_" + str(x) + str(y) + file_format
            cv2.imwrite(os.path.join(directory_of_positive, filename_result), result_im)

    #Convert to Black
    for pixel_y in range(int(r[1]), int(r[1]+r[3])):
        for pixel_x in range((int(r[0])), (int(r[0]+r[2]))):
            im.itemset((pixel_y, pixel_x, 0), 0) #Set B to 255
            im.itemset((pixel_y, pixel_x, 1), 0) #Set G to 255
            im.itemset((pixel_y, pixel_x, 2), 0)

    #Negative
    width = im.shape[0]
    height = im.shape[1]
    print(im.size)
    for x in range(0, width, split_dimension):
        for y in range(0, height,  split_dimension):
            # box = (x, y, x + split_dimension, y + split_dimension)
            result_im = im[x:(x+split_dimension), y:(y+split_dimension)]
            filename_result = current_file + "_" + str(x) + str(y) + file_format
            cv2.imwrite(os.path.join(directory_of_negative, filename_result), result_im)

for filename in os.listdir(directory_of_originals):
    if filename.endswith(".JPG") or filename.endswith(".jpg"):
        split_image(directory_of_originals, filename)
