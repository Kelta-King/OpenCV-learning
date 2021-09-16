import cv2 as c
import numpy as np

# Defining call back function
def mouse_click(evt, x, y, flags, param):

    # Left button click check
    if evt == c.EVENT_LBUTTONDOWN:

        # Getting colors of earch coordinates
        # Here, first y and then x will produce correct output. Not x then y.
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        # Creating a blank image
        img2 = np.zeros((512, 512, 3), np.uint8)

        # Filling each coordinates of blank image with the BGR color
        img2[:] = [blue, green, red]

        # Showing new color image
        c.imshow("color", img2)


# Reading image
img = c.imread("../Images/lena.jpg", 1)

# Showing image
c.imshow("image", img)

# Setting callback function
c.setMouseCallback("image", mouse_click)

# Waiting for key down
c.waitKey(0)
c.destroyAllWindows()
