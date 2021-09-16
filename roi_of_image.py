import cv2 as c
import numpy as np

# Image read
img = c.imread("Images/messi5.jpg", 1)

# Selecting region of interest (ROI)
# Selecting Ball area and storing it in ball variable
ball = img[280:340, 330:390]

# Coping the ball variable on the image according to the coordinates
img[173:233, 100:160] = ball

# Showing image
c.imshow("image", img)

# Waiting for key input
c.waitKey(0)
c.destroyAllWindows()
