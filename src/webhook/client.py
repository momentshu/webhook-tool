import requests

class WebhookClient:
    def __init__(self, webhook_file='webhooks.txt'):
        self.webhook_file = webhook_file
        self.webhooks = self.load_webhooks()

    def load_webhooks(self):
        try:
            with open(self.webhook_file, 'r') as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            return []

    def send_webhook(self, url, message):
        try:
            response = requests.post(url, json={'message': message})
            return response.status_code, response.text
        except requests.exceptions.RequestException as e:
            return None, str(e)