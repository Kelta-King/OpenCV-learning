import cv2 as c
import numpy as np

# To get all events of cv2 library
events = [i for i in dir(c) if "EVENT" in i]

# Defining the call back function
def click_mouse(event, x, y, flags, param):

    # If the event is left button click
    if event == c.EVENT_LBUTTONDOWN:

        # Putting text on image according to the coordinates
        val = str("(" + str(x) + " , " + str(y) + ")")
        font = c.FONT_HERSHEY_COMPLEX
        c.putText(img, val, (x, y), font, 0.5, (255, 255, 0), 1)
        c.imshow("image", img)

    # If the event is right button click
    elif event == c.EVENT_RBUTTONDOWN:

        # Putting text on image according to the BGR count
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        val = str("(" + str(blue) + "," + str(green) + "," + str(red) + ")")
        font = c.FONT_HERSHEY_COMPLEX
        c.putText(img, val, (x, y), font, 0.5, (255, 255, 0), 1)
        c.imshow("image", img)


# Read image
# img = np.zeros((512, 512, 3), np.uint8)
img = c.imread("Images/lena.jpg", 1)

# Show image
c.imshow("image", img)

# Setting mouse callback function. Here, the first parameter must be the title of shown image
c.setMouseCallback("image", click_mouse)

# Waiting for closing
c.waitKey(0)
c.destroyAllWindows()
