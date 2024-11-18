# Real-Time-Shoulder-Measurement-Using-Pose-Estimation

## Overview
In this Project I used computer vision and pose estimation technology to measure shoulder length in real time using a webcam feed. The project utilizes OpenCV for video capture and visualization, along with MediaPipe's pose estimation module for detecting human body landmarks, specifically focusing on measuring the distance between the left and right shoulder landmarks.

## Features
- **Real-Time Video Capture**: Continuously reads frames from the webcam for live shoulder length measurement.
- **Pose Estimation**: Uses MediaPipe's `Pose` model to detect body landmarks, including the shoulders.
- **Distance Calculation**: Computes the distance between the left and right shoulders in pixels and converts it to centimeters using a conversion factor.
- **Visualization**: Displays the shoulder length measurement and a line connecting the shoulders on the video feed.

### Installation
You can install the dependencies using `pip`:
```bash
pip install opencv-python mediapipe numpy
```

## Usage
1. Connect a webcam to your system.
2. Clone or download this repository.
3. Run the `main.py` file (assuming the script is named `main.py`):
   ```bash
   python main.py
   ```
4. The script will open a video window showing a live feed from your webcam. The detected shoulder length (in centimeters) will be displayed in the video feed, along with a line connecting the detected left and right shoulder points.

### Keyboard Controls
- **Press 'q'**: Close the video window and exit the application.

## Code Explanation

### Main Components
- **Pose Estimation Initialization**:
  ```python
  import cv2
  import mediapipe as mp
  import numpy as np

  mp_pose = mp.solutions.pose
  pose = mp_pose.Pose()
  ```
  This section initializes MediaPipe's `Pose` module for detecting landmarks.

- **Calculate Distance Function**:
  ```python
  def calculate_distance(point1, point2):
      return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
  ```
  Computes the Euclidean distance between two points.

- **Pixel-to-Centimeter Conversion**:
  ```python
  def convert_to_cm(pixels, conversion_factor):
      return pixels * conversion_factor
  ```
  Converts the distance measured in pixels to centimeters using a conversion factor.

- **Main Loop**:
  Captures video frames, detects landmarks, and calculates the shoulder length, displaying the result on the video feed.

## Conversion Factor
The conversion factor used for converting pixels to centimeters is `0.085`. This value may need to be adjusted based on camera settings and the subject's distance from the camera for more accurate measurements.

## Customization
- **Adjusting the Conversion Factor**: You can modify the `conversion_factor` variable based on your requirements to improve measurement accuracy.
- **Visualization**: The color, position, and size of the text and lines can be customized using OpenCV functions.

---

Thank you for using **Real-Time Shoulder Measurement Using Pose Estimation**! If you encounter any issues or have suggestions for improvement, feel free to reach out or contribute to the project.
