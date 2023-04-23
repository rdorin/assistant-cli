import requests, os

# streaming chunk size
CHUNK_SIZE = 1024

XI_API_KEY = print(os.environ['XI_API_KEY'])

# # for training a custom voice
# VOICE_SAMPLE_PATH1 = "<path-to-file>"
# VOICE_SAMPLE_PATH2 = "<path-to-file>"

OUTPUT_PATH = "./elli.mpeg"
voice_id = None

# add_voice_url = "https://api.elevenlabs.io/v1/voices/add"

headers = {
  "Accept": "application/json",
  "xi-api-key": XI_API_KEY
}

# data = {
#     'name': 'Voice name',
#     'labels': '{"accent": "American", "gender": "Female"}',
#     'description': 'An old American male voice with a slight hoarseness in his throat. Perfect for news.'
# }

# files = [
#     ('files', ('sample1.mp3', open(VOICE_SAMPLE_PATH1, 'rb'), 'audio/mpeg')),
#     ('files', ('sample2.mp3', open(VOICE_SAMPLE_PATH2, 'rb'), 'audio/mpeg'))
# ]

# response = requests.post(add_voice_url, headers=headers, data=data, files=files)
# voice_id = response.json()["voice_id"]

# endpoint for voice_ids: https://api.elevenlabs.io/v1/voices
ELLI_VOICE = "MF3mGyEYCl7XYWbV9V6O"
BELLA_VOICE = "EXAVITQu4vr4xnSDxMaL"
RACHEL_VOICE = "21m00Tcm4TlvDq8ikWAM"
if not voice_id:
    voice_id = RACHEL_VOICE


# get default voice settings
response = requests.get(
    "https://api.elevenlabs.io/v1/voices/settings/default",
    headers={ "Accept": "application/json" }
).json()
stability, similarity_boost = response["stability"], response["similarity_boost"]

tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

headers["Content-Type"] = "application/json"

data = {
  "text": "Hello, nice to meet you",
  "voice_settings": {
    "stability": stability,
    "similarity_boost": similarity_boost
  }
}

response = requests.post(tts_url, json=data, headers=headers, stream=True)

with open(OUTPUT_PATH, 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)

# Retrieve history. It should contain generated sample.
history_url = "https://api.elevenlabs.io/v1/history"

headers = {
  "Accept": "application/json",
  "xi-api-key": XI_API_KEY
}

response = requests.get(history_url, headers=headers)

print(response.text)