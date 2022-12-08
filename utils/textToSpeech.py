import os

import requests
import json
def textToSpeech(text, **kwargs):

  url = "https://play.ht/api/v1/convert"

  payload = json.dumps({
    "voice": "Hunter",
    "content": [

    ]
  })
  headers = {
    'Authorization': os.environ.get('PLAYHT_API_KEY'),
    'X-User-ID': os.environ.get('PLAYHT_USER_ID'),
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(f"{response.json()}")
