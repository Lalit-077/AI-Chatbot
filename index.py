from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("YOUR_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

#convo memory
messages = [
    {
        "role": "system",
        "content": "you are a helpful assistant",
    }
]
while True:
    user_response = input("User: ")

    if user_response.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    # adding user's message to memory
    messages.append({
        "role": "user",
        "content": user_response
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages = messages
        
    )

    assistant_response = response.choices[0].message.content

    # adding bot respose to memory
    messages.append({
        "role":"assistant",
        "content":assistant_response
    })

    print("Assistant:", response.choices[0].message.content)