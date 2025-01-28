# Webhook Tool

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Webhook Tool is a simple Python tool that allows users to send webhooks at specified intervals. This tool prompts the user for the interval in milliseconds, the name of the webhook, and the message to be sent, and then sends the message to the webhook URLs listed in `webhooks.txt`.

## Features

- Prompts the user for the interval in milliseconds to send webhooks.
- Prompts the user for a name for the webhook, generates a random name if left blank.
- Prompts the user for the message to be sent.
- Reads webhook URLs from the `webhooks.txt` file.
- Ability to delete all webhook URLs in bulk.

## Requirements

- Python 3.x
- Required libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd webhook-tool
   ```
3. Install the required dependencies:
 ```sh
 pip install -r requirements.txt
 ```
 ## Usage
Run the main application:

```sh
python src/main.py
```

Follow the prompts to enter the interval, webhook name, and message to be sent. The tool will send webhooks based on the provided information.

# Sending Webhooks
   1. Add webhook URLs to the webhooks.txt file.
   2. Run the application and select the 1. Send Webhooks option.
   3. Enter the requested information, and the tool will start sending webhooks.

# Deleting Webhooks
   1. Run the application and select the 2. Delete All Webhooks option.
   2. The tool will delete all webhook URLs listed in the webhooks.txt file.

# File Structure
webhook-tool/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   └── webhook/
│       ├── client.py
│       └── utils.py
└── webhooks.txt

README.md: Information about the project.
requirements.txt: Required Python libraries.
src/main.py: Main application file.
src/webhook/client.py: Webhook client class.
src/webhook/utils.py: Utility functions.
webhooks.txt: List of webhook URLs.

# Contributing

If you would like to contribute, please submit a pull request or open an issue. All contributions and feedback are welcome!

# License

This project is licensed under the MIT License. See the LICENSE file for more information.


This project is a great starting point for anyone looking to create a simple webhook sending tool using Python. Happy coding!

