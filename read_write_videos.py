import cv2 as c

# Capture video from the default camera. To specify video, just provide name instead of 0
cap = c.VideoCapture(0)

# Fourcc is specified using this function
fourcc = c.VideoWriter_fourcc(*'XVID')

# Output variable in which the output get stored. (name, furcc, frame rate, resolution)
out = c.VideoWriter('Output/output.mp4', fourcc, 20.0, (640, 480))

# If the window is opened then this loop continues
while cap.isOpened():

    # ret is boolean and frame containe values of each frame
    # ret is true if frame is captured, false otherwise
    ret, frame = cap.read()

    if(ret):
        # print(cap.get(c.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(c.CAP_PROP_FRAME_HEIGHT))

        # Converting to gray scale
        gray = c.cvtColor(frame, c.COLOR_BGR2GRAY)
        
        # Showing frame as an image
        c.imshow('frame', gray)

        # In the output.write method, the parameter must be frame. Gray will not work
        out.write(frame)

        # If the q key is pressed
        # Here, with waitKey we will wait for user input and then after the input we will check it in next condition of ord('q')
        if (c.waitKey(1)) & (0xFF == ord('q')):
            break
    
    else:
        break

cap.relese()
out.relese()
cap.destroyAllWindows()