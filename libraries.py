import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# archivo = open("image.txt" , "w")

while (True):
    #Capture frame by frame
    ret, frame = cap.read()

    #our operation on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    archivo.write(str(gray))
    #display the resulting frame
    cv2.imshow('frame', gray)

    #print(str(gray))

    if cv2.waitKey(1) == ord('q'):
        break
#when everything done, release the capture
archivo.close()
cap.release()
cv2.destroyAllWindows()
