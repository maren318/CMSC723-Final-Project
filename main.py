# go to groq_query.ipynb, use jupyter notebook during dev

# import os
# import json
# from groq import Groq
#
# with open('../GSM-IC/GSM-IC_2step.json', 'r') as file:
#     messages = json.load(file)
#
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY")
#     # api_key=''
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of low latency LLMs",
#         }
#     ],
#     model="llama3-8b-8192",
# )
# print(chat_completion.choices[0].message.content)