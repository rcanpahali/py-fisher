import cv2
import numpy as np
import pyautogui
import time
import sys
import random
import pygetwindow as gw

from utils.keyboard import press_space, prepare_for_fishing

from task_scheduler.scheduler import exit_signal, setup_task_scheduler
from task_scheduler.message_queue_handler import add_message_to_queue

print("\nFisher script started.\n")
time.sleep(5)

# Global variables
template_image_path = 'D:\\fisher-py\\media\\objective.png'
template_image_save_path = 'D:\\fisher-py\\media\\caught.png'
template_image = cv2.imread(template_image_path)
template_match_threshold = 0.55
templating_delay = 0.35

# Bypass variables
max_detection_attempts_threshold = 75
bypass_on_fail = True
bypass_total_fail_threshold = 3
bypass_fail_count = 0

# Statistical variables
start_time = time.time()
pull_attempts = 0
detection_attempts = 0
max_detection_attempts_count = 0

# Get the window associated information
window = gw.getWindowsWithTitle("OLD METIN2")[0]
window_rect = window.left, window.top, window.width, window.height
window_rect_aoi = window.left + 500, window.top, window.width - 1000, window.height - 700
window.activate()
time.sleep(1)

# Function to check for the presence of the image
def check_for_image():
    global detection_attempts
    global pull_attempts
    global max_detection_attempts_count

    # Take a screenshot for the area of interest
    screenshot = pyautogui.screenshot(region=window_rect_aoi)

    # Convert the screenshot to a NumPy array
    screen_image = np.array(screenshot)
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGB2BGR)

    # Match the template in the screenshot
    result = cv2.matchTemplate(screen_image, template_image, cv2.TM_CCOEFF_NORMED)

    if np.max(result) >= template_match_threshold:
        print("\nImage detected. Score: ", np.max(result))

        pull_attempts += 1
        detection_attempts = 0

        pull_hook()
        prepare_for_fishing()        
    else:
        detection_attempts += 1
        max_detection_attempts_count = max(detection_attempts, max_detection_attempts_count)
        print("Image not detected: ", detection_attempts)
        return False

def pull_hook():
    # Check if the window is active
    if not window.isActive:
        window.activate()
        time.sleep(0.1)

    # Generate a random delay for the hook pull
    random_number = random.uniform(0.1, 0.7)
    hook_delay = round(random_number, 5)    

    print("Pulling the hook, delay: ", hook_delay, " - attempt: ", pull_attempts)
    time.sleep(hook_delay)
    press_space()

# Function to check for the unexpected attempt count
def check_for_unexpected_attempt_count():
    global detection_attempts
    global bypass_on_fail
    global bypass_fail_count 

    if detection_attempts >= max_detection_attempts_threshold:
        add_message_to_queue("Unexpected detection attempt count threshold hit: " + str(detection_attempts))
                
        if bypass_on_fail:
            # Bypass the threshold on fail for a few times
            if bypass_fail_count >= bypass_total_fail_threshold:
                add_message_to_queue("Bypassing threshold limit reached")
                return True                 
            
            print("Bypassing the threshold")
            add_message_to_queue("Bypassing the threshold")
            detection_attempts = 0
            time.sleep(5)

            # Take a screenshot and continue processing
            screenshot = pyautogui.screenshot(region=window_rect)    
            screenshot.save('D:\\fisher-py\\media\\bypass_on_fail_' + str(bypass_fail_count) + '.png')                                          
            bypass_fail_count = bypass_fail_count + 1

            continuously_check_for_image()
            return False
        else:
            return True

# Function to continuously check for the image
def continuously_check_for_image():
    global templating_delay
    prepare_for_fishing()
    try:
        while True:
            time.sleep(templating_delay)
            if check_for_image():
                break
            if check_for_unexpected_attempt_count():
                raise TimeoutError("Unexpected attempt count")  
            if exit_signal.is_set():
                raise InterruptedError("Exit signal received")          
    except (KeyboardInterrupt, TimeoutError, InterruptedError):
        global start_time
        global max_detection_attempts_count
        global bypass_fail_count
    
        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time_minutes = elapsed_time_seconds / 60

        print(f"\nMax failed attempts bypass count:", bypass_fail_count)
        print(f"Max failed attempts count:", max_detection_attempts_count)                

        print(f"\nScript started at: {time.ctime(start_time)}")
        print(f"Script ended at: {time.ctime(end_time)}")
        print(f"Script execution time: {elapsed_time_minutes:.2f} minutes ({elapsed_time_seconds:.2f} seconds)")
        
        exit_signal.set()

        print("\nPress any key to quit.\n")
        input()  # Wait for user to press any key
        sys.exit(1) # Exit the script

setup_task_scheduler()
continuously_check_for_image()