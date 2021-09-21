import cv2 as c
import numpy as np

# Read image
img1 = c.imread("Images/lena.jpg")

# Making a black image with the same dimention as img1
img2 = np.zeros((512, 512, 3), np.uint8)

# Adding rectangle on img2
c.rectangle(img2, (200, 100), (300, 200), (255, 255, 255), -1)

# All bitwise operators on both images
bitAnd = c.bitwise_and(img2, img1)
bitOr = c.bitwise_or(img2, img1)
bitXor = c.bitwise_xor(img1, img2)

# Not operation which inverses color on one image
bitNot = c.bitwise_not(img1)

# Sowing images
c.imshow("image", img1)
c.imshow("image2", img2)
c.imshow("bitwise", bitNot)

# Waiting for key to destroy open windows
c.waitKey(0)
c.destroyAllWindows()
