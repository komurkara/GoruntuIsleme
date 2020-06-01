import argparse
import imutils
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help= "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.imread('img.jpg')
cv2.imshow("original",image)

M = np.float32([[1,0,25],[0,1,50]])


def cv2warpAffine(image, M, param):
    pass


shifted = cv2warpAffine(image, M, (image.shape[1],image.shape[0]))
cv2.imshow("Shifted Down and Right",shifted)

M = np.float32([[1,0,-50],[0,1,-90]])
shifted= cv2.warpAffine(image, M, (image.shape[1],image.shape[0]) )
cv2.imshow("Shifted Up and Left",shifted)
