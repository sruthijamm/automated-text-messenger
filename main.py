import os
from ai_generator import generate_message
from tone_checker import check_tone
from dotenv import load_dotenv

load_dotenv()

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    phone_number = os.getenv('PHONE_NUMBER')
    
    prompt = input("What kind of message do you want to send? ")
    
    print("\nGenerating message...")
    message = generate_message(prompt)
    print(f"\nGenerated message:\n{message}")
    
    print("\nChecking tone...")
    tone = check_tone(message)
    print(f"Tone check: {tone}")
    
    confirm = input("\nSend this message? (yes/no): ")
    if confirm.lower() == 'yes':
        send_message(phone_number, message)
        print("Message sent!")
    else:
        print("Message cancelled.")