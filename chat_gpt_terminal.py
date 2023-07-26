#!/usr/bin/env python3
import os
import openai
from dotenv import load_dotenv
load_dotenv()

key = os.environ.get('OPENAI_TOKEN')
openai.api_key = key

steering_prompt = "Write a macos terminal command to perform the users request. Return only the text that should be directly written into the user's terminal session. If no feasible macos command is possible then return the phrase `NO COMMAND FOUND`."

query = input("> ").strip()

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
        "role": "system",
        "content": steering_prompt
    },
    {
        "role": "user",
        "content": query
    }
  ],
  temperature=1.0,
  max_tokens=75,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

subresp = response['choices'][0]['message']['content']
print(f"\n{subresp}")

cont = input(f'\nRun this command? [Y/n]: ')
if not cont.lower().startswith('n'):
    print()
    os.system(subresp)
else:
    print('stopping')
