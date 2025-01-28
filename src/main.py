import requests
import time
import random
import os
from random_username.generate import generate_username
from rich.console import Console
from rich import print as rprint
from rich.text import Text
import fade
console = Console()

def print_with_typing_effect(text, delay=0.05):
    for char in text:
        console.print(char, end='', style="yellow")
        time.sleep(delay)
    print()
def print_input_with_typing(prompt, delay=0.05):
    for char in prompt:
        console.print(char, end='', style="cyan")
        time.sleep(delay)
    return input()

def load_webhooks():
    with open('webhooks.txt', 'r') as file:
        return [line.strip() for line in file if line.strip()]

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(f"Successfully deleted webhook: {webhook_url}")
            return True
        else:
            print(f"Failed to delete webhook {webhook_url}. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error deleting webhook: {str(e)}")
        return False

def delete_all_webhooks():
    webhooks = load_webhooks()
    if not webhooks:
        print("No webhooks found in webhooks.txt!")
        return
    
    print("\nStarting to delete webhooks...\n")
    deleted_webhooks = []
    
    for webhook in webhooks:
        if delete_webhook(webhook):
            deleted_webhooks.append(webhook)
        
    print(f"\nDeleted {len(deleted_webhooks)} webhooks successfully!")

def send_webhook(webhook_url, message, username):
    try:
        data = {
            "content": message,
            "username": username if username else random.choice(generate_username())
        }
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            named_tuple = time.localtime() # get struct_time
            time_string = time.strftime("%H:%M:%S", named_tuple)
            RESET = "\033[0m"
            GRAY = "\033[90m"
            BLUE = "\033[34m"
            print(f"{GRAY}[{BLUE}{time_string}{GRAY}] {RESET} {username if username else random.choice(generate_username())} sent message successfully to your webhooks!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending webhook: {str(e)}")

def webhook_sender():
    webhooks = load_webhooks()
    if not webhooks:
        print("No webhooks found in webhooks.txt!")
        return
    
    while True:
        try:
            delay = float(print_input_with_typing("Enter delay between messages (in milliseconds): ")) / 1000
            break
        except ValueError:
            print("Please enter a valid number!")
    
    username = print_input_with_typing("Enter webhook username (leave empty for random usernames): ").strip()
    message = print_input_with_typing("Enter message to send: ").strip()
    
    if not message:
        print("Message cannot be empty!")
        return
    
    print_with_typing_effect("\nStarting to send messages...\n")
    
    try:
        while True:
            for webhook in webhooks:
                send_webhook(webhook, message, username)
                time.sleep(delay)
    except KeyboardInterrupt:
        print("\nStopping webhook sender...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        asciiText = '''
███╗   ███╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗██╗  ██╗██████╗ ██████╗
████╗ ████║██╔═══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝╚██╗██╔╝██╔══██╗██╔══██╗
██╔████╔██║██║   ██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║    ╚███╔╝ ██████╔╝██║  ██║
██║╚██╔╝██║██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║    ██╔██╗ ██╔══██╗██║  ██║
██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ██╔╝ ██╗██║  ██║██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
'''
        
        print(fade.fire(asciiText))    
        for option in [
            "1. Send Webhooks",
            "2. Delete All Webhooks",
            "3. Exit"
        ]:
            print_with_typing_effect(option)

        choice = print_input_with_typing("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            webhook_sender()
            input(print_input_with_typing("\nPress Enter to continue..."))
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            delete_all_webhooks()
            input(print_input_with_typing("\nPress Enter to continue..."))
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()