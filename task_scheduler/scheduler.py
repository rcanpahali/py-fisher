import os
import sys
import time
import threading
import schedule

from task_scheduler.message_queue_handler import setup_message_queue_handler
from task_scheduler.ingame_message_handler import setup_ingame_message_handler

# Set up an event to signal the threads to exit
exit_signal = threading.Event()
task_scheduler = schedule.Scheduler()

# Function to run the scheduler
def run_scheduler():
    print("Setup task schedulers:")
    setup_message_queue_handler(task_scheduler)
    setup_ingame_message_handler(task_scheduler)
    try:
        while not exit_signal.is_set():
            task_scheduler.run_pending()     
            time.sleep(1)
    except Exception as e:
        print(f"Exception occurred: {e} - Stopping the program.")
        exit_signal.set()        

def setup_task_scheduler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()