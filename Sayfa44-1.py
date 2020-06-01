import argparse
import imutils
import cv2
import numpy as np

#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

image = cv2.imread('img.jpg')

# examine the dimensions of the image. The images are represented
# as NumPy arrays, so we can use the shape attribute to examine
# the width, height, and number of channels
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# handles displaying the actual image on my screen
# the first parameter is a string, the "title" of the window
# the second parameter is a reference to the image we loaded.
cv2.imshow("Image", image)
cv2.waitKey(0)