import cv2
import os

# Create the Sketches directory if it doesn't exist
if not os.path.exists('Sketches'):
    os.makedirs('Sketches')

cap = cv2.VideoCapture(0)

def dodge(x, y):
    return cv2.divide(x, 255 - y, scale=256)

count = 1

while True:
    success, img = cap.read()
    if not success:
        break
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGrayInv = 255 - imgGray
    imgBlur = cv2.GaussianBlur(imgGrayInv, ksize=(21, 21), sigmaX=5, sigmaY=0)
    finalImg = dodge(imgGray, imgBlur)
    
    cv2.imshow('Face', finalImg)  # Sketched Image

    key = cv2.waitKey(1)
    
    if key & 0xFF == ord('q'):
        break
    if key & 0xFF == ord(' '):  # Press spacebar to take photo
        filename = f'Sketches/Image {count}.jpg'
        cv2.imwrite(filename, finalImg)
        print(f'Image saved as {filename}')
        count += 1

cap.release()
cv2.destroyAllWindows()
