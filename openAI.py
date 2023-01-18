import openai
import apikey

openai.api_key = apikey.key_openAI

# get prebuild string
def generate_sentence(_prompt):
  _prompt= "convert the following sentence into natural language sentence.\n" +_prompt
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=_prompt,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]["text"]