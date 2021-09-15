import cv2 as c

cap = c.VideoCapture(0)

# With cap.get methods, different values of camera can be accessed
print(cap.get(c.CAP_PROP_FRAME_WIDTH))
print(cap.get(c.CAP_PROP_FRAME_HEIGHT))

# Setting values using set methods
# This values will be set to the possible values. If values are very high then it will set maximum value
cap.set(c.CAP_PROP_FRAME_WIDTH, 1208)
cap.set(c.CAP_PROP_FRAME_HEIGHT, 720)

# Video reading and showing
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:

        c.imshow('image', frame)

        if c.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
c.destroyAllWindows()
