import queue
import sys
import time
import threading
import schedule

from utils.slack_client import send_text_message_to_slack

SCHEDULE_TIME_IN_SECONDS = 20

# Create a queue to store messages
message_queue = queue.Queue()
# Set up an event to signal the threads to exit
exit_signal_slack_message_handler = threading.Event()

# Function to add messages to the queue
def add_message_to_queue(message):
    print(message)
    message_queue.put(message)

# Function to check the queue
def get_message_from_queue():
    if not message_queue.empty():
        return message_queue.get()
    return None

# Function to check the queue and send messages to Slack
def check_and_send_messages():
    print("Checking for messages in the queue: ", message_queue.qsize())
    message = get_message_from_queue()
    if message:
        send_text_message_to_slack(message)

# Function to run the scheduler
def run_scheduler():
    global SCHEDULE_TIME_IN_SECONDS
    print("Setting up the task scheduler for slack message handler")
    schedule.every(SCHEDULE_TIME_IN_SECONDS).seconds.do(check_and_send_messages)
    try:
        while not exit_signal_slack_message_handler.is_set() or (not message_queue.empty() and exit_signal_slack_message_handler.is_set()): # Wait for the queue to be empty before exiting
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Stopping the program.")
        exit_signal_slack_message_handler.set()
        sys.exit(0)

def setup_message_queue_handler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()