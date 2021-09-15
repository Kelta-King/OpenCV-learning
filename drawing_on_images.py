import cv2 as c

# Image read
img = c.imread("Images/lena.jpg", 1)

# Draw a line. Parameters: img, coordinate 1, coordinate 2, color, thickness
img = c.line(img, (0,0), (255,255), (255, 0, 0), 5)

# Arrowed line
img = c.arrowedLine(img, (0,255), (255,255), (0, 255, 0), 5)

# Rectnagel parameters: img, top-left coordiate, bottom-right coordinate, color, thickness
img = c.rectangle(img, (100,100), (300,300), (0, 0, 255), 5)

# If the thickness is in -ve, then it will fill the rectangle with the color
img = c.rectangle(img, (500,500), (300,300), (0, 0, 255), -5)

# Circle methor parameters: img, center, radius, color, thickness. If thickness in -ve, it will fill it.
img = c.circle(img, (400,400), 30, (255, 255, 0), 5)

# To add text on image use putText()
font = c.FONT_HERSHEY_SIMPLEX
img = c.putText(img, 'Lena', (100,100), font, 4, (255, 255, 255), 5)

"""
More like polygons, eclipse. Watch online
"""

# Image show
c.imshow("image", img)

# Keep thee tab open
c.waitKey(0)
c.destroyAllWindows()
