import cv2
import os
import datetime

# Create a directory to save images if it doesn't exist
save_dir = "captured_images"
gray_image_dir = "gray_images"
os.makedirs(save_dir, exist_ok=True)
os.makedirs(gray_image_dir, exist_ok=True)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    if key == ord('q'):  # Press 'q' to exit
        break
    elif key == ord('s'):  # If any key is pressed, save the image
        color_img = os.path.join(save_dir, f"captured_image{datetime.datetime.now()}.jpg")
        cv2.imwrite(color_img, frame)

        # Read the saved image
        image = cv2.imread(color_img)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        saved_gray_path = os.path.join(gray_image_dir, f"captured_gray_image{datetime.datetime.now()}.jpg")
        cv2.imwrite(saved_gray_path, gray_image)

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
