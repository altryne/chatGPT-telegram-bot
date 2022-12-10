import io
import os
import warnings

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


async def drawWithStability(prompt):
  stability_api = client.StabilityInference(
    key=os.environ.get('STABILITY_API_KEY'),  # API Key reference.
    verbose=True,  # Print debug messages.
    engine="stable-diffusion-768-v2-1",  # Set the engine to use for generation.
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-inpainting-v1-0 stable-inpainting-512-v2-0
  )
  split_prompts, seed = generate_prompts(prompt)
  # Set up our initial generation parameters.
  answers = stability_api.generate(
    prompt=split_prompts,

    # If a seed is provided, the resulting generated image will be deterministic. What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
    # Note: CLIP Guided generations will attempt to stay near the original generation, however unlike non-clip guided inference, there's no way to guarantee a deterministic result, even with the same seed.
    steps=50,  # Step Count defaults to 50 if not specified here.
    cfg_scale=7.0,
    seed=seed,
    # Influences how strongly your generation is guided to match your prompt. Setting this value higher increases the strength in which it tries to match your prompt. Defaults to 7.0 if not specified.
    width=768,  # Generation width, defaults to 512 if not included.
    height=768,  # Generation height, defaults to 512 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2S_ANCESTRAL,

    # Choose which sampler we want to denoise our generation with. Defaults to k_dpmpp_2s_ancestral. CLIP Guidance only supports ancestral samplers.
    # (Available Samplers: ddim, k_euler_ancestral, k_dpm_2_ancestral, k_dpmpp_2s_ancestral)
    guidance_preset=generation.GUIDANCE_PRESET_FAST_GREEN  # Enables CLIP Guidance.
  )

  for resp in answers:
    for artifact in resp.artifacts:
      if artifact.finish_reason == generation.FILTER:
        warnings.warn(
          "Your request activated the API's safety filters and could not be processed."
          "Please modify the prompt and try again.")
      if artifact.type == generation.ARTIFACT_IMAGE:
        return artifact.binary, artifact.seed

def generate_prompts(prompt_string):
  prompt_string = prompt_string.replace('\\','')
  # Split the prompt string into individual prompts
  prompts = prompt_string.split('|')

  # Create a list to store the generated prompts
  generation_prompts = []
  seed = 0
  # Loop through the prompts and create a generation.Prompt object for each one
  for prompt in prompts:
    # Split the prompt into its text and weight
    prompt_parts = prompt.split(':')
    text = prompt_parts[0].strip()
    weight = 1.0
    if len(prompt_parts) > 1:
      try:
        weight = float(prompt_parts[1].strip())
      except ValueError:
        weight = 1.0

      # in case we have the seed in the like this "prompt | seed: 123123123123"
      if text == "seed":
        seed = int(weight)
        continue

    # Create the generation.Prompt object and add it to the list
    generation_prompt = generation.Prompt(text=text, parameters=generation.PromptParameters(weight=weight))
    generation_prompts.append(generation_prompt)

  return generation_prompts, seed
