

from openai import OpenAI
import decl

client = decl.loadClient()

def chat(says):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": says,
            }
        ],
        model="gpt-4o-2024-08-06",
    )
    return  chat_completion.choices[0].message.content


prompt = "what is pcell?"
response = chat(prompt)
print(response)
