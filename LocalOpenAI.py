import openai
import os

print(os.getcwd())
filepath = 'K\OpenAI.txt'

with open(filepath, "r") as f:
  openai.api_key = ' '.join(f.readlines())

system_message = "You are an AI tutor that assists school students with math homework problems. You never reveal the right answer to the student. You ask probing questions to identify where the student might be needing help, provide hints and guidance, and provide directional feedback to indicate if the student is moving in the right direction. Do not reveal the correct answer to the student."


# list of system message, user and assistant examples
message_history = [
        {"role": "system", "content": system_message},
        {"role": "system", "name":"example_user", "content": "Help me solve the equation 3x - 9 = 21."},
        {"role": "system", "name":"example_assistant", "content": "Sure! Try moving the 9 to the right hand side of the equation. What do you get?"},
        {"role": "system", "name":"example_user", "content": "3x = 12"},
        {"role": "system", "name":"example_assistant", "content": "Well, there seems to be a mistake. When you move 9 to the right hand side, you need to change its sign. Can you try again?"},
        {"role": "system", "name":"example_user", "content": "3x = 30"},
        {"role": "system", "name":"example_assistant", "content": "That looks good, great job! Now, try to divide both sides by 3. What do you get?"},
        {"role": "system", "name":"example_user", "content": "x = 10"},
        {"role": "user", "content": "Help me solve the equation x - 10 = 2x"}
    ]


# get the chatbot's next response
chat_response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages = message_history,
  max_tokens = 150,
  n=2,
  top_p=1,
  temperature = 1
  )

print(chat_response.choices[0].message.content)
print("\n\n\n\n", chat_response)