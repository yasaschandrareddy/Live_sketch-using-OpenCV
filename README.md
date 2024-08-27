# Sketch Camera Application

This is a simple Python application that captures webcam footage, applies a sketch effect to the frames in real-time, and allows the user to save images by pressing the spacebar. The application also allows the user to quit by pressing the 'q' key.

## Requirements

- Python 3.x
- OpenCV (`cv2` library)

You can install OpenCV using pip:

```bash
pip install opencv-python 

How It Works
Main Features
Capture Video from Webcam:

The application uses OpenCV to access the webcam feed in real-time.
Apply Sketch Effect:

Each frame from the webcam is converted to grayscale.
An inverted grayscale image is created.
The inverted image is blurred using a Gaussian filter.
A "dodge blend" operation is applied between the original grayscale image and the blurred inverted image, resulting in a sketch effect.
Save Sketched Images:

The user can press the spacebar to save the current sketched frame as an image.
The images are saved in the Sketches directory.
Exit the Application:

Press 'q' to quit the application.
Directory Structure
The application automatically creates a Sketches directory to store the captured images. If the directory does not exist, it will be created when the application starts.

Code Breakdown
Importing Libraries:

cv2 is used for all computer vision tasks.
os is used to handle directory creation.
Directory Creation:

The application checks if the Sketches directory exists and creates it if it doesn't.
Capturing Video:

The webcam is accessed using cv2.VideoCapture(0).
Processing Frames:

Each frame is converted to grayscale.
An inverted grayscale image is created.
The inverted image is blurred using a Gaussian blur.
The sketch effect is achieved using a custom dodge function that blends the grayscale image with the blurred image.
Displaying Frames:

The sketched frame is displayed in a window titled "Face".
Saving Images:

The user can save the current frame by pressing the spacebar. The saved image will be stored in the Sketches directory with a sequential filename (e.g., Image 1.jpg).
Exiting the Application:

Press 'q' to exit the application.
How to Use
Run the Python script:

bash
Copy code
python sketch_camera.py
A window titled "Face" will appear, showing the sketched output of the webcam feed.

Press the spacebar to capture and save an image in the Sketches directory.

Press 'q' to exit the application.

Troubleshooting
Webcam Not Working:

Ensure your webcam is properly connected.
Check if any other applications are using the webcam.
No Image Saved:

Make sure you are pressing the spacebar while the webcam feed is active.
Verify that the Sketches directory exists.
