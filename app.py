import openai
from os import environ

openai.api_key = environ['OPENAI_API_KEY']

messages = [{'role': 'system',
             'content': 'You are a helpful assistant.'}]
message = input('message: ')
messages.append(dict(role='user', content=message))

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo-1106',
    messages=messages)

print(response.choices[0].message['content'])