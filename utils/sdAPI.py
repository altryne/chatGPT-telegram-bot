import os
import requests
async def drawWithStability(prompt):

  engine_id = "stable-diffusion-512-v2-0"
  api_host = os.getenv('API_HOST', 'https://api.stability.ai')
  url = f"{api_host}/v1alpha/generation/{engine_id}/text-to-image"

  output_file = os.getenv('OUT_DIR', '.') + "/text_to_image.png"

  apiKey = os.getenv("STABILITY_API_KEY")
  if apiKey is None:
    raise Exception("Missing Stability API key.")

  payload = {
    "cfg_scale": 7,
    "clip_guidance_preset": "FAST_BLUE",
    "height": 512,
    "width": 512,
    "samples": 1,
    "sampler": "K_EULER_ANCESTRAL",
    "seed": 0,
    "steps": 30,
    "text_prompts": [
      {
        "text": prompt,
        "weight": 1
      }
    ],
  }

  headers = {
    "Content-Type": "application/json",
    "Accept": "image/png",
    "Authorization": apiKey
  }

  response = requests.post(url, json=payload, headers=headers)

  if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

  # Write the bytes from response.content to a file
  return response.content
