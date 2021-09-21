import cv2 as c
import numpy as np

# Track bar call back function
def nope(x):
    pass


# Creating black image
img = np.zeros((500, 500, 3), np.uint8)

# Creating named window first for later use
c.namedWindow("Image")

# Creating trackbars for B,G,R values
c.createTrackbar("B", "Image", 0, 255, nope)
c.createTrackbar("G", "Image", 0, 255, nope)
c.createTrackbar("R", "Image", 0, 255, nope)

# While loop
while True:

    # Showing image
    c.imshow("Image", img)

    # Checking for esc key pressed
    if (c.waitKey(1) & 0xFF) == 27:
        break

    # Getting the trackbar values
    b = c.getTrackbarPos("B", "Image")
    g = c.getTrackbarPos("G", "Image")
    r = c.getTrackbarPos("R", "Image")

    # Setting color of the black image
    img[:] = [b, g, r]

# Destroy all windowws
c.destroyAllWindows()
