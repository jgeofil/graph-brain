# %%
import os
from pprint import PrettyPrinter
from mem0 import MemoryClient
from dotenv import load_dotenv
# %%


# %%
load_dotenv()

client = MemoryClient()
# %%

messages = [
    {
        "role": "user",
        "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts.",
    },
    {
        "role": "assistant",
        "content": "Hello Alex! I see that you're a vegetarian with a nut allergy.",
    },
]

client.add(messages, user_id="alex")


query = "What can I cook for dinner tonight?"

filters = {"OR": [{"user_id": "alex"}]}

response = client.search(query, version="v2", filters=filters)

print(PrettyPrinter(4).pformat(response))
