#right now all this does is ask the LLM a single hardcoded question, then print the response.
#todo: how to securely deal with API keys
#todo: use questions from GSM json

import os
import json
from groq import Groq

with open('./GSM-IC/GSM-IC_mstep.json', 'r') as file:
    messages = json.load(file)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
    # api_key='gsk_Ibs2AHZ2canttellyoutherestforsecurity'
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)