from openai import OpenAI
from apikey import apikey
import os

os.environ['OpenAI_api_key'] = apikey
OpenAI_api_key = apikey

client = OpenAI()
audio_file = ("path","rb")

print("Generating text....")
response = client.audio.transcriptions.create(
    model="wisper-1",
    file = audio_file,
    response_format="text",
)

print(response)
