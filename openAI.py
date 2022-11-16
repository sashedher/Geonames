import openai
import apikey

openai.api_key = apikey.key_openAI

# get prebuild string
_prompt = ""


response = openai.Completion.create(
  model="text-davinci-001",
  prompt=_prompt,
  temperature=1.0,
  max_tokens=128,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=1
)