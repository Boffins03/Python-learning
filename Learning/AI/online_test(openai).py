from openai import OpenAI
from apikey import apikey
import os

os.environ['OpenAI_api_key'] = apikey
OpenAI_api_key = apikey

client = OpenAI()
prompt = "largest city in the world"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content":prompt}])

print("Response")
print(response)
print("Message Content:")
print(response.choices[0].message.content)