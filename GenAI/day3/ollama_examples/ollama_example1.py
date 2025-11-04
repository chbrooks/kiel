from ollama import chat

messages = [
  {
    'role': 'user',
    'content': 'What state is Kiel in?',
  },
]

response = chat('orca-mini', messages=messages)
print(response['message']['content'])
print(f"What else in in this response?: {response}")