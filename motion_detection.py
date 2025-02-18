import cv2

# Initialize the webcam
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

# Release the capture and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
