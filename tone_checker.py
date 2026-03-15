from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

def check_tone(message):
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": f"Review this SMS message for tone: '{message}'. Reply with ONLY one of these: GOOD, TOO FORMAL, TOO CASUAL, TOO HARSH. Then one sentence explaining why."
            }
        ]
    )
    return response.content[0].text