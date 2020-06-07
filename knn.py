from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

# load the image
im = Image.open('IMG_8132.JPG')
width, height = im.size
im1 = im.crop((0, 1000, width, height - 1000))
width1,height1 = im1.size
im1 = im1.resize((int(width1 / 12), int(height1 / 12)))
# im1.show()
im_array = np.array(im1.convert('L'))

#Prepare array to put back to
b = np.empty_like(im_array)

#Convert image to flat array
intensity = im_array.ravel()
print(intensity.dtype)

#Map Pixel
map_pix = np.zeros((im_array.shape[0] * im_array.shape[1], 2))
map_pix = map_pix.astype('i')
print(im_array.shape[0])
for i in range(0, im_array.shape[0]):
    for j in range(0, im_array.shape[1]):
        map_pix[i * im_array.shape[1] + j] = [i, j]


# #Initialize Color Intensity Map
# index_value = np.arange(0, 256)
# color_intensity_map = np.zeros(256)
# color_intensity_map = color_intensity_map.astype('i')
# for index in intensity:
#     color_intensity_map[index] = color_intensity_map[index] + 1
# maximum_amount = color_intensity_map.max()
# color_intensity_map = color_intensity_map.astype('f')
# for i in range(0, len(color_intensity_map)):
#     color_intensity_map[i] = color_intensity_map[i] * 256 / maximum_amount
# color_intensity_map = color_intensity_map.reshape(256, 1)

#KNN Classifier
for n in [3, 5, 9, 21]:
    neigh = KNeighborsClassifier(n_neighbors=n, weights='uniform')
    neigh.fit(map_pix, intensity)

    for i in range(0, im_array.shape[0]):
        for y in range(0, im_array.shape[1]):
            b[i][y] = neigh.predict([[i, y]])

    # compare = np.equal(im_array, b)
    # for i in range(0, im_array.shape[0]):
    #     for j in range(0, im_array.shape[1]):
    #         if not compare[i][j]: b[i][j] = 0

    f = plt.figure()
    f.add_subplot(1,2, 1)
    plt.imshow(np.rot90(im_array,3), cmap="gray")
    f.add_subplot(1,2, 2)
    plt.imshow(np.rot90(b,3), cmap="gray")
    name = "k = " + str(n)
    plt.savefig(name, dpi = 500)
