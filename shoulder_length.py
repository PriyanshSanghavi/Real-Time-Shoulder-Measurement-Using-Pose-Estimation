import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def convert_to_cm(pixels, conversion_factor):
    return pixels * conversion_factor


conversion_factor =  0.085

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = pose.process(image_rgb)
    
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, 
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, 
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        
        shoulder_length_px = calculate_distance(left_shoulder, right_shoulder) * frame.shape[1]
        shoulder_length_px += 200
        shoulder_length_cm = convert_to_cm(shoulder_length_px, conversion_factor)
        
        print(f'Shoulder Length: {shoulder_length_cm:.2f} cm')

        cv2.putText(frame, f'Shoulder Length: {shoulder_length_cm:.2f} cm', 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        left_shoulder_px = (int(left_shoulder[0] * frame.shape[1]+15), int(left_shoulder[1] * frame.shape[0]))
        right_shoulder_px = (int(right_shoulder[0] * frame.shape[1]-15), int(right_shoulder[1] * frame.shape[0]))
        cv2.line(frame, left_shoulder_px, right_shoulder_px, (0, 255, 0), 2)
    
    cv2.imshow('Shoulder Length Measurement', frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
