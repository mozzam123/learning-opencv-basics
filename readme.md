## Image Capture with OpenCV

### This project allows users to capture images using a webcam, save them in color, and convert them to grayscale automatically. Additionally, it includes an edge detection feature using the Canny algorithm.


### Folder Structure
```text
captured_images/    # Directory for storing captured color images
gray_images/        # Directory for storing grayscale images
main.py            # Main script for capturing and processing images
edge_detection.py   # Script for real-time edge detection using Canny algorithm
```

### Requirements
Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install opencv-python
```

### Usage
Run the script to start capturing images:
```bash
python main.py
```

- Press ```s``` to save a captured image
- The color image is saved in the ```captured_images/``` directory
- The grayscale version is saved in the ```gray_images/``` directory
- Press ```q``` to quit the program

Run the edge detection script:
```bash
python edge_detection.py
```

- Displays the blurred and edge-detected versions of the webcam feed in real time

- Press q to quit the program

### Features
- Capture images from a webcam
- Save both color and grayscale versions
- Automatically organize images into separate directories
- Perform real-time Canny edge detection on a webcam feed
