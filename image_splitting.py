import os, sys
from PIL import Image

split_dimension = int(sys.argv[1])
directory_of_originals = sys.argv[2]
directory_of_results = sys.argv[3]
if not os.path.exists(directory_of_results):
    os.mkdir(directory_of_results)


def split_image(directory, filename):
    directory = os.path.join(directory_of_originals, filename)
    print(directory)
    im = Image.open(directory)
    current_file, file_format = os.path.splitext(filename)
    width, height = im.size
    print(im.size)
    for x in range(0, width, split_dimension):
        for y in range(0, height,  split_dimension):
            box = (x, y, x + split_dimension, y + split_dimension)
            result_im = im.crop(box)
            filename_result = current_file + "_" + str(x) + str(y) + file_format 
            result_im.save(os.path.join(directory_of_results, filename_result))

for filename in os.listdir(directory_of_originals):
    if filename.endswith(".JPG"):
        split_image(directory_of_originals, filename)
