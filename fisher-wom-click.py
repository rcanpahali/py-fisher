import time
import pygetwindow as gw
import random
from pywinauto.application import Application

# Get the window handle
#window = gw.getWindowsWithTitle("New Virtual Machine on DESKTOP-6KUQCER - Virtual Machine Connection")[0]
window = gw.getWindowsWithTitle("New Virtual Machine on DESKTOP-6KUQCER - Virtual Machine Connection")[0]
window.activate()
time.sleep(1)

# Get the window dimensions
window_left, window_top, window_width, window_height = window.left, window.top, window.width, window.height

# Define the safe area to click (excluding 100px from each side)
safe_left = window_left + 100
safe_top = window_top + 100
safe_right = window_left + window_width - 100
safe_bottom = window_top + window_height - 100

# Initialize the application
app = Application().connect(handle=window._hWnd)

# Click 10 times with minimal delay
for _ in range(10):
    # Generate random coordinates within the safe area
    x = random.randint(safe_left, safe_right)
    y = random.randint(safe_top, safe_bottom)
    
    # Move to the generated coordinates and click
    app.window(handle=window._hWnd).click_input(coords=(x - window_left, y - window_top))
    print(f"Clicked at ({x}, {y})")
    
    # Minimal delay to avoid overwhelming the system
    time.sleep(0.1)  # Reduced from 1 second to 0.1 seconds
