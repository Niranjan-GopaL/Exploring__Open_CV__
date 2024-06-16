# READ THE NOTEBOOK for complete understanding ; THESE ARE THE CODE THAT YOU NEED TO ALWAYS REMEMBER ;
# Better programmer like this  ;
import cv2

# you could get cv2.cvtColor cpp error => you are accessing the wrong webcam
cap = cv2.VideoCapture(0)

while cap.isOpened(): 
    
    # frame is the image, ret is wheather success or not
    ret, frame = cap.read()

    y,x = 150, 250
    correct_frame = frame[y: y+250, x: x+250, :]
    
    # displaying frame
    cv2.imshow('Image Collection', correct_frame)

    # You can press A and save the image in ANCHOR folder ; press P and save the image in POSITIVE folder // this code is the LAST CODE BLOCK in jn

    # Quit on pressing Q to exit gracefully ; No need of KeyboardInterrupt
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# THIS IS WHAT YOU NEED TO EXECUTE when something goes wrong

# releases the webcame
cap.release()
# releases the image show frame
cv2.destroyAllWindows()