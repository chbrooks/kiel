from ollama import chat

from ollama import chat
messages = [
    {'role': 'system',
     'content': 'You are a tutor. Do not answer math questions, but instead provide hints. Answer all other questions normally.'},
]

while True:
  user_input = input('Chat with history: ')
  response = chat(
    'llama3.1',
    messages=[*messages, {'role': 'user', 'content': user_input}],
  )

  # Add the response to the messages to maintain the history
  messages += [
    {'role': 'user', 'content': user_input},
  ]
  print(response.message.content + '\n')