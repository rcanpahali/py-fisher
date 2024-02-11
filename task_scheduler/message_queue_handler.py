import queue

from utils.slack_client import send_text_message_to_slack

SCHEDULE_TIME_IN_SECONDS = 20

# Create a queue to store messages
message_queue = queue.Queue()

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
def setup_message_queue_handler(task_scheduler):
    global SCHEDULE_TIME_IN_SECONDS
    print("Setup the message queue handler")
    task_scheduler.every(SCHEDULE_TIME_IN_SECONDS).seconds.do(check_and_send_messages)