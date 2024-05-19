# MT2 Py-Fisher

This is a Python project that includes functionalities for interacting MT2 game window for in-game fishing. It also supports sending Slack messages / in-game message delivery and handling messages in the queue.

## Structure

The project has the following structure:

- `fisher.py`: Main script.
- `media/`: Directory for media files.
- `task_scheduler/`: Contains scripts for handling tasks and messages.
  - `ingame_message_handler.py`: Handles in-game messages.
  - `message_queue_handler.py`: Handles message queues.
  - `scheduler.py`: Handles task scheduling.
- `test/`: Contains test scripts.
  - `detect-color.py`: Test script for color detection.
  - `request.py`: Test script for handling requests.
- `utils/`: Contains utility scripts.
  - `keyboard.py`: Handles keyboard interactions.
  - `slack_client.py`: Handles interactions with Slack.

## Slack Client

The Slack client is implemented in [`slack_client.py`](utils/slack_client.py). It includes functions for sending text messages and text messages with image attachments to a specific Slack channel.

## Setup

To set up the project, you need to install the required Python packages. You can do this by running:

```sh
pip install
```

## Usage
To run the main script, use the following command:

```sh
python fisher.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
