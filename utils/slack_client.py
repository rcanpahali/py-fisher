# Your Slack API token
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_TOKEN = "xoxb-3746688324391-6515355105621-KKtpAqvlUN3Blt1bETIT9taQ"
SLACK_CHANNEL = "C06JMFY1GGZ" #"py-fisher-logs" channel id

# Initialize the Slack WebClient
slack_client = WebClient(token=SLACK_TOKEN)

# Function to send messages to Slack
def send_text_message_to_slack(message):
    try:
        response = slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        print(f"Message sent to Slack: {response['ts']}")
    except Exception as e:
        print(f"Error sending message to Slack: {str(e)}")

# Function to send messages with image attachment to Slack using files_upload_v2
def send_text_message_with_image_to_slack(message, image_path):
    try:
        # Read the image file as binary data
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        # Upload the image
        response = slack_client.files_upload_v2(                        
            channel=SLACK_CHANNEL,
            initial_comment=message,
            file=image_data,
            filename="new-message-detected.png",
        )
        print(f"Message with image sent to Slack: {response['file']['url_private']}")
    except SlackApiError as e:
        print(f"Error sending message with image to Slack: {e}")