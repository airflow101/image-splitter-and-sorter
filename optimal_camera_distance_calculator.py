import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__' :

    # Read image
    im = cv2.imread("IMG_7447.JPG")
    height_im, width_im, channels = im.shape
    height_im = height_im //8
    width_im = width_im //8

    # Select ROI
    cv2.namedWindow("Image",2)
    cv2.resizeWindow("Image", width_im, height_im)
    roi_ori = cv2.selectROI("Image", im, True, False)
    print(roi_ori)
    roi_interest = cv2.selectROI("Image", im, True, False)
    print(roi_interest)

    area_ori = roi_ori[2] * roi_ori[3]
    area_interest = roi_interest[2] * roi_interest[3]
    percentage = 100 * area_interest / area_ori

    print("Area of Interest Percentage")
    print(percentage)
    total_area = height_im * width_im
    percentage = 100 * area_interest / total_area

    print("Compared to total area")
    print(percentage)

    #3:2
    width_calculation = roi_interest[2]
    if roi_interest[2] % 2 == 1:
        width_calculation += 1

    height_calculation = roi_interest[2] * 3 // 2
    start_point  = roi_interest[0]

    #Normalized to 110
    while height_calculation + 3 < roi_interest[2] * 4.4:
        height_calculation += 3
        width_calculation += 2
        start_point -= 1

    #Test until 150
    optimal_height = height_calculation
    optimal_width = width_calculation
    area = height_calculation * width_calculation
    area_of_interest = roi_interest[2] * height_calculation
    optimal_percentage = area_of_interest / area
    data = [[],[]]
    data[1].append(optimal_percentage)
    data[0].append(area)
    while height_calculation + 3 <= roi_interest[2] * 6:
        height_calculation += 3
        width_calculation += 2
        start_point -= 1
        current_area = height_calculation * width_calculation
        current_roi_area = roi_interest[2] * height_calculation
        percentage =  current_roi_area / current_area
        data[1].append(percentage)
        data[0].append(current_area)
        if percentage > optimal_percentage:
            optimal_height = height_calculation
            optimal_width = width_calculation
            optimal_percentage = percentage

    # print(data)
    plt.plot(data[0], data[1])
    plt.show()

    print("Optimal percentage:")
    print(optimal_percentage)

    print("Optimal width and height in px:")
    print(optimal_width)
    print(optimal_height)

    print("Optimal width and height in mm:")
    final_width = 25 * optimal_width // roi_interest[2]
    final_height = final_width * 1.5
    print(25 * optimal_width // roi_interest[2])
    print(final_height)

    # Crop image
    imCrop = im[int(roi_interest[1]):int(roi_interest[1]+optimal_height), int(start_point):int(start_point+optimal_width)]
    #
    # # Display cropped image
    cv2.namedWindow("ROI",2)
    cv2.imshow("ROI", imCrop)
    height_imCrop, width_imCrop, channels = imCrop.shape
    height_imCrop = height_imCrop // 8
    width_imCrop = width_imCrop // 8
    cv2.resizeWindow("ROI", width_imCrop, height_imCrop)
    cv2.waitKey(0)
