from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
import langchain

load_dotenv(dotenv_path='.env',override=True)

client = OpenAI(api_key=os.getenv("PERPLEXITY_API_KEY"),base_url="https://api.perplexity.ai") #Instantiate the API connection to the Perplexity API

messages = [
    {"role": "system","content": "You are an artificial intelligence assistant and you need to engage in a helpful, detailed, polite conversation with a user."},
    {"role": "user","content": "How many atoms are in the universe?"},
]

# chat completion without streaming
response = client.chat.completions.create(
    model="pplx-7b-chat",
    messages=messages,
)
print(response.choices[0].message.content) #Prints the response from the AI, the content of the message.



# # chat completion with streaming
# response_stream = client.chat.completions.create(
#     model="mistral-7b-instruct",
#     messages=messages,
#     stream=True,
# )
# for response in response_stream:
#     print(response.choices[0].message.content)