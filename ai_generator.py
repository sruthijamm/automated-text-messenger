import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

def generate_message(prompt):
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": f"Write a short, natural SMS message for this situation: {prompt}. Keep it under 3 sentences. No emojis unless it fits. Just the message text, nothing else."
            }
        ]
    )
    return response.content[0].text