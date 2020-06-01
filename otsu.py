import numpy as np
import mahotas
import cv2


image = cv2.imread("1img.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

T = mahotas.thresholding.otsu(blurred)
print("Otsu’s threshold: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)

