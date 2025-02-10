## Image Capture with OpenCV

### This project allows users to capture images using a webcam, save them in color, and convert them to grayscale automatically. The images are stored in separate directories for color and grayscale versions.

### Folder Structure
```text
captured_images/    # Directory for storing captured color images
gray_images/        # Directory for storing grayscale images
main.py            # Main script for capturing and processing images
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

### Features
- Capture images from a webcam
- Save both color and grayscale versions
- Automatically organize images into separate directories
