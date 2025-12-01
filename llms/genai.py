from google import genai
from google.genai import types

# Only run this block for Gemini Developer API
client: genai.Client = genai.Client(api_key="GEMINI_API_KEY")

model: types.Model = client.models.get(model="gemini-2.5-flash-exp")

response: types.GenerateContentResponse = model.generate_content(
    user_id="me", content="Hello, how are you?"
)

print(response.text)
