import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


# Memory Router auto-stores and retrieves memories - just change the base_url!
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.supermemory.ai/v3/https://api.openai.com/v1/",
    default_headers={
        "x-supermemory-api-key": os.getenv("SUPERMEMORY_API_KEY"),
        "x-sm-user-id": "jeremy",
    },
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "I love cooking Italian food!"}],
)

print(response.choices[0].message.content)
