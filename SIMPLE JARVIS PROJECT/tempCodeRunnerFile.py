from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)