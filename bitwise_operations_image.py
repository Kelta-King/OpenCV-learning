import cv2 as c
import numpy as np

img1 = c.imread("Images/lena.jpg")
img2 = np.zeros((512, 512, 3), np.uint8)

c.rectangle(img2, (200, 100), (300, 200), (255, 255, 255), -1)

bitAnd = c.bitwise_and(img2, img1)
bitOr = c.bitwise_or(img2, img1)
bitNot = c.bitwise_not(img1)
bitXor = c.bitwise_xor(img1, img2)

c.imshow("image", img1)
c.imshow("image2", img2)
c.imshow("bitwise", bitNot)

c.waitKey(0)
c.destroyAllWindows()
