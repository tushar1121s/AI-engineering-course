import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key kahan hai bhaai")


client = Groq(api_key=my_api_key)

model ="llama-3.3-70b-versatile"
role="user"
# Prompt = "you are using data till which year to answer the questions"
Prompt = "Do u know we are currently in which year"

message= {
    "role" : role,
    "content" : Prompt

}

messages = [message]
response = client.chat.completions.create(model=model,messages = messages)
# print(response)

print(response.choices[0].message.content)