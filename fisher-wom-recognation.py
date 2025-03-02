from datetime import datetime
import time
import pygetwindow as gw
import os
import cv2
import numpy as np
import dxcam

# Sleep for a while to ensure the window is ready
time.sleep(1)

objective = f'D:\\Repos\\py-fisher\\py-fisher\\media\\objective\\objective.jpg'
# Load the objective image
objective_img = cv2.imread(objective, cv2.IMREAD_GRAYSCALE)

# Get the window handle
window = gw.getWindowsWithTitle("Windows Virtual Machine on DESKTOP-6KUQCER - Virtual Machine Connection")[0]
window.activate()
time.sleep(1)

# Get the window coordinates
left, top, right, bottom = window.left, window.top, window.right, window.bottom

# Define the region to capture (top-left 128x128 pixels)
capture_width = 128
capture_height = 128
capture_left = left + 85
capture_top = top + 157
capture_right = capture_left + capture_width
capture_bottom = capture_top + capture_height

# Create the camera object
camera = dxcam.create()

# Capture the screen region
frame = camera.grab(region=(capture_left, capture_top, capture_right, capture_bottom))

# Convert the frame to a numpy array
frame_np = np.array(frame)

## TODOs: 
# find a way to compare the screenshot with the objective image
# if the screenshot contains the objective icon, then click on exact location on the screen

#####################

# Convert the captured frame to grayscale
frame_gray = cv2.cvtColor(frame_np, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(frame_gray, objective_img, cv2.TM_CCOEFF_NORMED)

# Set a threshold for matching
threshold = 0.8
loc = np.where(result >= threshold)

# Check if the objective icon is found
if len(loc[0]) > 0:
    # Get the location of the match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    match_loc = max_loc

    # Calculate the center of the matched region
    match_center_x = match_loc[0] + objective_img.shape[1] // 2
    match_center_y = match_loc[1] + objective_img.shape[0] // 2

    # Calculate the exact screen coordinates
    screen_x = capture_left + match_center_x
    screen_y = capture_top + match_center_y

    # Click on the exact location
    #import pyautogui
    #pyautogui.click(screen_x, screen_y)
    #print(f"Clicked on the objective icon at ({screen_x}, {screen_y})")
else:
    print("Objective icon not found in the screenshot")

#####################

# Save the image
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output = f'D:\\Repos\\py-fisher\\py-fisher\\media\\screenshot_{timestamp}.png'
cv2.imwrite(output, frame_np)

# Open the saved screenshot
os.startfile(output)

print(f"Screenshot saved to {output}")
