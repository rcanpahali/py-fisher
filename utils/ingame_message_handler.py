import queue
import sys
import time
import threading
import schedule
import pyautogui
import numpy as np
import cv2
import time
import random
import pygetwindow as gw

from utils.slack_client import send_text_message_with_image_to_slack

SCHEDULE_TIME_IN_SECONDS = 10

exit_signal_ingame_message_handler = threading.Event()
template_image_save_path = 'D:\\fisher-py\\media\\new-message-detected.png'

# Get the window associated information
window = gw.getWindowsWithTitle("OLD METIN2")[0]
window_rect = window.left, window.top, window.width, window.height
window_text_rect = window.left + 2650, window.top + 621, 140, 26

def detect_pixel_color():
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot(region=window_text_rect)

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
        return True
    else:
        return False

##############
def check_available_tasks():
    print("Available scheduled tasks:")
    for job in schedule.get_jobs():
        print(f"Job: {job.job_func.__name__}, Next run: {job.next_run}")
#########

def check_for_ingame_message():
    check_available_tasks() 
    print("Checking for in-game message")
    if detect_pixel_color(): # Detect the text pixel color of the message sender
            screenshot = pyautogui.screenshot(region=window_rect)
            screenshot.save(template_image_save_path)
            time.sleep(0.5)
            send_text_message_with_image_to_slack("New message detected", template_image_save_path) 



# Function to run the scheduler
def run_scheduler():
    global SCHEDULE_TIME_IN_SECONDS
    print("Setting up the task scheduler for ingame message handler")
    schedule.every(SCHEDULE_TIME_IN_SECONDS).seconds.do(check_for_ingame_message)
    try:
        while not exit_signal_ingame_message_handler.is_set():
            schedule.run_pending()
            time.sleep(1)
    except:
        print("Stopping the program.")
        exit_signal_ingame_message_handler.set()
        sys.exit(0)

def setup_ingame_message_handler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()