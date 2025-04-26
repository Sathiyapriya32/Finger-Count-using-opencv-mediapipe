# ✋ Finger Counting Using Computer Vision

This project uses OpenCV and MediaPipe to detect hands in real-time through a webcam and count the number of fingers being shown.

## 📄 Description

The application captures webcam input, processes the frames to detect hand landmarks, and calculates the number of fingers raised based on the relative position of hand landmarks.

When you show your hand to the webcam, the system identifies how many fingers are open and displays the count on the screen.

## 🛠️ Imports

The following Python libraries are used:

- `opencv-python`
- `mediapipe`

Install them using:

```bash

📚 TECHNIQUES USED 
Hand Detection: Using MediaPipe's Hands solution to detect hand landmarks.

Landmark Positioning: Comparing fingertip landmarks with MCP (Metacarpophalangeal) joint landmarks.

Real-time Processing: Frame-by-frame detection and visualization using OpenCV.

Gesture Analysis: Logic to determine finger openness by comparing x or y coordinates.

![Screenshot 2025-04-27 at 2 04 29 AM](https://github.com/user-attachments/assets/212732c5-53c3-4b9e-b4c3-399df1a3dd24)


🎥 Watch Demo Video: [Click here](https://www.linkedin.com/posts/sathiyapriya-s-22ucs048_artificialintelligence-machinelearning-computervision-activity-7237462540744564736-0FuA?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEKubiABTjioeFLfoGOrHXFNNCGvYJ6moX8)

