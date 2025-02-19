import cv2
import time

# Load your YOLOv8 model
from ultralytics import YOLO
model = YOLO('best.pt')

# Labels
labels = [
    "Bear", "Cheetah", "Crocodile", "Elephant", "Fox", "Giraffe", "Hedgehog", "Human",
    "Leopard", "Lion", "Lynx", "Ostrich", "Rhinoceros", "Tiger", "Zebra"
]
last_detected_time = time.time()
# Function to run inference on an image
def run_inference_on_image(image):
    global last_detected_time
    results = model(image)[0]

    detected = False
    detected_animal = None

    for x1, y1, x2, y2, conf, lab in results.boxes.data.tolist():
        label = labels[int(lab)]
        detected = True
        detected_animal = label

        # Draw the bounding box
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        # Display the label
        cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # If an animal is detected, check the cooldown
    current_time = time.time()
    if detected and (current_time - last_detected_time > 5):
        last_detected_time = current_time


        print(f"Animal Detected: {detected_animal}")

    return image


# Initialize webcam capture
cap = cv2.VideoCapture(0)  # 0 for default webcam

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Run inference and draw bounding boxes with labels on the frame
    frame = run_inference_on_image(frame)

    # Show the resulting frame
    cv2.imshow("Webcam Inference", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()