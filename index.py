from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("YOUR_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

while True:
    user_response = input("User: ")

    if user_response.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_response}
        ]
    )

    print("Assistant:", response.choices[0].message.content)