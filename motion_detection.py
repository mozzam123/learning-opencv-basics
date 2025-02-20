import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

# Initialize the tracker
tracker = cv2.TrackerKCF.create()

# Initialize the tracking state
tracking = False
bbox = None

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)
    fgmask = fgbg.apply(blurred)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:
            (x, y, w, h) = cv2.boundingRect(contour)

            if not tracking:
                # Start tracking the first detected object
                bbox = (x, y, w, h)
                tracker.init(frame, bbox)
                tracking = True
            else:
                # Update the tracker and draw bounding box
                success, bbox = tracker.update(frame)
                if success:
                    (x, y, w, h) = [int(v) for v in bbox]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Motion Detection & Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
