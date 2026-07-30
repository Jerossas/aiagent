import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
    raise RuntimeError("The OpenRouter API key was not found.")


client: OpenAI = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = api_key
)

messages: list[dict] = [
        {
            "role": "user",
            "content": "Why is boot.dev such a great place to learn backend development? Use one paragraph maximum."
        }
]

def main():
    
    response = client.chat.completions.create(model="openrouter/free", messages=messages)
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
