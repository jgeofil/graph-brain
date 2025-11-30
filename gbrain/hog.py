import os
from posthog.ai.gemini import Client
from posthog import Posthog
from dotenv import load_dotenv

load_dotenv()


posthog = Posthog(os.environ["POSTHOG_API_KEY"], host="https://us.i.posthog.com")

client = Client(api_key=os.environ["GEMINI_API_KEY"], posthog_client=posthog)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Tell me a fun fact about hedgehogs"],
    posthog_distinct_id="specific_user",  # Override default
)

print(response)
