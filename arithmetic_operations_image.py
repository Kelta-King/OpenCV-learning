import cv2 as c

# Read image
img = c.imread("Images/messi5.jpg", 1)
img2 = c.imread("Images/lena.jpg", 1)

# Image is a numpy 2d array.
# To see the (height, width, BGR count) use shape attr
print(img.shape)

# To see the total pixels count use size
print(img.size)

# dtype of pixels
print(img.dtype)

# Resize image using resize method.
# Parameters: source, (height, width)
img = c.resize(img, (512, 512))

# Resizing both images are necessary to add them. Otherwise it will give error
img2 = c.resize(img2, (512, 512))

# Add image using add method
img3 = c.add(img, img2)

# Add 2 images with weights of each of them
# Param: src1, weight1, src2,, weight2
img_weighted = c.addWeighted(img, 0.6, img2, 0.1, 0)

# Shoowing simple added image
c.imshow("Image", img3)

# Showing weighted image
c.imshow("Image2", img_weighted)

c.waitKey(0)
c.destroyAllWindows()
