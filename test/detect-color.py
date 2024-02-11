import pyautogui
import numpy as np
import cv2
import time
import pygetwindow as gw

template_image_save_path = 'D:\\fisher-py\\media\\message-caught-test.png'

# Get the window associated information
window = gw.getWindowsWithTitle("OLD METIN2")[0]
window_rect = window.left + 2650, window.top + 621, 140, 26
window.activate()
time.sleep(2)

def detect_color():
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot(region=window_rect)
    screenshot.save(template_image_save_path)
    time.sleep(1)

    # Convert the screenshot to an OpenCV image (BGR format)
    screenshot_cv2 = np.array(screenshot)
    screenshot_cv2 = cv2.cvtColor(screenshot_cv2, cv2.COLOR_RGB2BGR)

    # Convert the image to LAB color space
    lab_img = cv2.cvtColor(screenshot_cv2, cv2.COLOR_BGR2LAB)

    # Define the range of gray colors in LAB color space
    lower_bound = np.array([0, 128, 128], dtype=np.uint8)  # Lower bound for gray color
    upper_bound = np.array([255, 128, 128], dtype=np.uint8)  # Upper bound for gray color

    # Create a mask to detect gray colors
    mask = cv2.inRange(lab_img, lower_bound, upper_bound)

    # Check if any pixel in the mask is non-zero (i.e., the color was detected)
    if np.any(mask != 0):
        print("Color detected!")
    else:
        print("Color not detected.")

while True:
    detect_color()
    time.sleep(3)
