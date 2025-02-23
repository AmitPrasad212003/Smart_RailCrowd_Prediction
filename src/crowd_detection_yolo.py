# import cv2
# import torch
# from ultralytics import YOLO

# # Load YOLOv8 model
# model = YOLO("yolov8n.pt")

# # Open video stream
# cap = cv2.VideoCapture("data/station_cctv.mp4")

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # Perform detection
#     results = model(frame)
    
#     # Draw results on frame
#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
#     cv2.imshow("Crowd Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()



import cv2
import torch
import numpy as np

# Load YOLOv8 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Open video stream
cap = cv2.VideoCapture('data/station_cctv.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform detection
    results = model(frame)
    detections = results.pandas().xyxy[0]  # Bounding boxes
    
    # Filter people class (class 0 in COCO dataset)
    people = detections[detections['class'] == 0]
    count = len(people)
    
    # Draw bounding boxes
    for _, row in people.iterrows():
        cv2.rectangle(frame, (int(row['xmin']), int(row['ymin'])), (int(row['xmax']), int(row['ymax'])), (0, 255, 0), 2)
    
    # Display count
    cv2.putText(frame, f'People Count: {count}', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Crowd Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
