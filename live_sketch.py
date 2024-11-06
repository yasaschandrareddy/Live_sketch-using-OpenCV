import cv2
import os

#creating the folder for storing captured images
if not os.path.exists('Sketches'):
    os.makedirs('Sketches')

cap = cv2.VideoCapture(0)

def dodge(x, y):
    return cv2.divide(x, 255 - y, scale=256)

count = 1

while True:
    #opening of webcam to read the live feed
    success, img = cap.read()
    if not success:
        break
    #converting the colored image to gray image i.e black and white
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGrayInv = 255 - imgGray
    imgBlur = cv2.GaussianBlur(imgGrayInv, ksize=(21, 21), sigmaX=5, sigmaY=0)
    finalImg = dodge(imgGray, imgBlur)
    
    cv2.imshow('Face', finalImg)  # Displaying Sketched Image in real-time

    key = cv2.waitKey(1)
    
    if key & 0xFF == ord(' '):  # Press spacebar to take and display the photo

        filename = f'Sketches/Image_{count}.jpg'
        cv2.imwrite(filename, finalImg)
        print(f'Image saved as {filename}')
        stored_img = cv2.imread(filename)  # Load the saved image
        cv2.waitKey(0)  # Wait until any key is pressed to close the image
        break  
    elif key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
