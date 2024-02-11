import pyautogui
from pyKey import pressKey, releaseKey
import time

# Keyboard events
def press_one():
    pressKey('1')
    time.sleep(0.5)
    releaseKey('1')

def press_two():
    pressKey('2')
    time.sleep(0.5)
    releaseKey('2')

def press_space():    
    pressKey('SPACEBAR')
    time.sleep(0.5)
    releaseKey('SPACEBAR')

def click_on_message_box():
    pyautogui.click(2650, 621)

# Predifiend actions
def prepare_for_fishing():
    time.sleep(2)
    print("\nPreparing for fishing\n")
    press_one()

    time.sleep(1.5)
    press_space()