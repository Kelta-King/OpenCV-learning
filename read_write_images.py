import cv2 as c

# Read image
img = c.imread('Images/lena.jpg', 0)

# Show Image
c.imshow('image', img)

# Wait for closing the image
key = c.waitKey(0)

# Save the image if s is pressed
if key == ord('s'):
    c.imwrite('img.png', img)

# Close the image id q is pressed
elif key == ord('q'):
    c.destroyAllWindows()

