# MotionSlide



## Overview

The **MotionSlide** is a innovative desktop application that allows users to seamlessly control their presentations and computer interactions using intuitive hand gestures detected via a webcam. Built with Python, MediaPipe for hand tracking, and PyAutoGUI/Keyboard for system control, this tool aims to provide a hands-free, dynamic, and engaging way to deliver presentations and navigate your desktop.

## Features

  * **Cursor Control:** Move your mouse cursor across the screen using right-hand movements.
  * **Click Actions:** Perform left and right clicks with specific right-hand finger gestures.
  * **Screenshot Capture:** Quickly take screenshots of your screen with a right-hand fist gesture.
  * **Scrolling:** Scroll up and down through documents or web pages using left-hand gestures.
  * **Volume Control:** Adjust system volume up or down with designated left-hand gestures.
  * **Application Switching:** Easily switch between open applications using a left-hand gesture (e.g., `Win + Tab` on Windows).
  * **Cursor Freeze/Unfreeze:** Toggle the cursor movement on/off for precise control or when hands are not actively controlling.

## Getting Started

### Prerequisites

  * **Webcam:** A functional webcam is required for hand detection.
  * **Python:** Python 3.x installed on your system.
  * **Operating System:** Designed for Windows and macOS environments.

### Installation (from Source)

If you wish to run the application directly from the source code:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/Gesture-Controlled-Presentation-Tool.git
    cd Gesture-Controlled-Presentation-Tool
    ```

    (Replace `yourusername` and `Gesture-Controlled-Presentation-Tool` with your actual GitHub details)

2.  **Install Dependencies:**

    ```bash
    pip install opencv-python mediapipe pyautogui keyboard numpy
    ```

### How to Run

1.  **Navigate to the project directory** in your terminal or command prompt.
2.  **Run the script:**
    ```bash
    python your_main_script_name.py
    ```
    (Replace `your_main_script_name.py` with the actual name of your Python script, e.g., `virtual_mouse.py`)

## Usage

Once the application is running, a live feed from your webcam will appear. Position your hands clearly in front of the camera to begin gesture control.

### Default Gesture Mappings:

**Right Hand (Cursor & Clicks)**

  * **Movement:** Control cursor position.
  * **Right Hand Fist (`[0,0,0,0,0]`):** Take a screenshot.
  * **Right Hand Index Finger Up (`[0,1,0,0,0]`):** Right-click.
  * **Right Hand Middle Finger Up (`[0,0,1,0,0]`):** Left-click.
  * **Right Hand Thumb Down (`[0,X,X,X,X]`):** Freeze cursor movement. (Check `cursor_frozen = finger_status[0] == 0` in code for exact logic)

**Left Hand (Scrolling & System Actions)**

  * **Left Hand Index Finger Up:** Scroll Up.
  * **Left Hand Middle Finger Up:** Scroll Down.
  * **Left Hand Fist (`[0,0,0,0,0]`):** Activate `Win + Tab` (Application Switcher).
  * **Left Hand Index Finger & Thumb Touching (`lm[8]` & `lm[4]`):** Volume Up.
  * **Left Hand Middle Finger & Thumb Touching (`lm[12]` & `lm[4]`):** Volume Down.




-----
