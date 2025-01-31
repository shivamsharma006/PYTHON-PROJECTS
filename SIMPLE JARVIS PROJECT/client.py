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
