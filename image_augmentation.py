import os, sys
import imageio
from imgaug import augmenters as iaa
from imgaug.augmentables.batches import UnnormalizedBatch

directory = sys.argv[1]
BATCH_SIZE = 10

#Save Folders Creation
def create_folder(folder_names):
    for foldername in folder_names:
        folder_dir = os.path.join(directory, foldername)
        if not os.path.exists(folder_dir):
            os.mkdir(folder_dir)

folder_names = ["Rotation and Translation", "Gaussian Blur", "Brightness Contrast", "Salt and Pepper"]

create_folder(folder_names)

folder_dir = []
for folder_name in folder_names:
    folder_dir.append(os.path.join(directory, folder_name))


#Features
#Rotation and Translation
def transrot(batches):
    aff = iaa.Sequential([iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}), iaa.Rot90((1,3))])
    with aff.pool(processes=3, maxtasksperchild=10, seed=1) as pool:
        batches_aug = pool.map_batches(batches)
    for i in range(len(filenames_result)):
        imageio.imwrite(os.path.join(folder_dir[0], filenames_result[i]), batches_aug[i//BATCH_SIZE].images_aug[i%BATCH_SIZE])


#Gaussian Blur
def gaussian(batches):
    with iaa.GaussianBlur(sigma=(0.0, 3.0)).pool(processes=3, maxtasksperchild=10, seed=1) as pool:
        batches_aug = pool.map_batches(batches)
    for i in range(len(filenames_result)):
        imageio.imwrite(os.path.join(folder_dir[1], filenames_result[i]), batches_aug[i//BATCH_SIZE].images_aug[i%BATCH_SIZE])

#Brightness and Contrast
def brightcont(batches):
    augm = iaa.Sequential([iaa.MultiplyBrightness((0.5, 1.5)), iaa.GammaContrast((0.5, 2.0))])
    with augm.pool(processes=3, maxtasksperchild=10, seed=1) as pool:
        batches_aug = pool.map_batches(batches)
    for i in range(len(filenames_result)):
        imageio.imwrite(os.path.join(folder_dir[2], filenames_result[i]), batches_aug[i//BATCH_SIZE].images_aug[i%BATCH_SIZE])

#Salt and Pepper
def saltpepper(batches):
    with iaa.SaltAndPepper(0.1).pool(processes=3, maxtasksperchild=10, seed=1) as pool:
        batches_aug = pool.map_batches(batches)
    for i in range(len(filenames_result)):
        imageio.imwrite(os.path.join(folder_dir[3], filenames_result[i]), batches_aug[i//BATCH_SIZE].images_aug[i%BATCH_SIZE])


#Augmenter Initialization
def augment(batches):
    transrot(batches)
    gaussian(batches)
    brightcont(batches)
    saltpepper(batches)


#Read directory_of_images
opened_images = []
batches = []
filenames_result = []

if __name__ == '__main__':
    for filename in os.listdir(directory):
        if filename.endswith(".JPG") or filename.endswith(".jpg"):
            current_file, file_format = os.path.splitext(filename)
            filenames_result.append(current_file + "_Augmented" + file_format)
            file = os.path.join(directory, filename)
            opened_images.append(imageio.imread(file))
            if len(opened_images) == BATCH_SIZE:
                batches.append(UnnormalizedBatch(images=opened_images))
                opened_images = []

    if len(opened_images) > 0:
        batches.append(UnnormalizedBatch(images=opened_images))

    augment(batches)
