import cv2

def find_camera_indexes(max_index=10):
    available_indexes = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_indexes.append(i)
            cap.release()
    return available_indexes

camera_indexes = find_camera_indexes()
print("Available camera indexes:", camera_indexes)
