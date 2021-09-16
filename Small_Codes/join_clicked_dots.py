import cv2 as c
import numpy as np

# Call back fuction declaration
def mouse_click(evt, x, y, flags, params):

    # Left button click
    if evt == c.EVENT_LBUTTONDOWN:

        # Drawing circle on the image at x,y coordinate
        c.circle(img, (x, y), 3, (255, 255, 255), -1)

        # Adding the point in points list
        points.append((x, y))

        # If the points are more than 1 then only draw lines
        if len(points) > 1:

            # Draw line from last point to secondlast point
            c.line(img, points[-2], points[-1], (255, 255, 0), 2)

        # Show image
        c.imshow("image", img)


# Image read
img = np.zeros((512, 512, 3), np.uint8)

# Showing image
c.imshow("image", img)

# Setting callback function
c.setMouseCallback("image", mouse_click)

# Points list
points = []

# Wait for closing
c.waitKey(0)
c.destroyAllWindows()
