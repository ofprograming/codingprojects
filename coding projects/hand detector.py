import cv2 
from handTrackingModule import handTracker

cap = cv2.VideoCapture(0)

# Create an instance of the handTracker class
tracker = handTracker()

while True:
    success, image = cap.read()
    if not success:
        print("Failed to read frame")
        continue

    # Use the handTracker class to process the frame and detect hands
    image = tracker.HandsFinder(image)
    
    cv2.imshow("Hand Tracking", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2
