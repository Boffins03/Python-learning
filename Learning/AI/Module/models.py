from openai import OpenAI
from apikey import apikey
from io import BytesIO
from PIL import Image
import requests
import os

def setup_openai(apikey):
    os.environ['OpenAI_api_key'] = apikey
    OpenAI_api_key = apikey
    client = OpenAI()
    return client

def text_generate(client,prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}])

    return response.choices[0].message.content

def image_generate(client,prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt = prompt,
    size = "1024x1024",
    n=1,)
    image_url = response.data[0].url
    image = requests.get(image_url)
    image = Image.open(BytesIO(image.content))
    return image

def audio_to_text(client,audio_file):
    response = client.audio.transcriptions.create(
    model="wisper-1",
    file = audio_file,
    response_format="text",)
    return response