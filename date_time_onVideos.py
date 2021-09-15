import cv2 as c
import datetime

# Start capturing
cap = c.VideoCapture(0)

# Capturing
while(cap.isOpened()):

    # Reading
    ret, frame = cap.read()

    if(ret):

        # Setting font
        font = c.FONT_HERSHEY_SIMPLEX

        # Adding text as the now date and time
        text = str(datetime.datetime.now())

        # Putting date time text on video
        frame = c.putText(frame, text, (10, 50), font, 1, (255, 255, 255), 2)

        # Showing video
        c.imshow('video', frame)

        # Closing by clicking q
        if c.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

# Never forgot to relese these values
cap.release()
c.destroyAllWindows()