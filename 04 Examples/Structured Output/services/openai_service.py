import os
from openai import OpenAI
from dotenv import load_dotenv


class OpenAIService:
    def __init__(self, model="gpt-3.5-turbo-0125"):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model

    @property
    def client(self):
        if not hasattr(self, "_client"):
            self._client = OpenAI()
        return self._client


if __name__ == "__main__":
    openai_service = OpenAIService()

    messages = [
        {
            "role": "system",
            "content": "You're a helpful assistant",
        },
        {"role": "user", "content": f"Hi there!"},
    ]

    response = openai_service.client.chat.completions.create(
        model=openai_service.model,
        messages=messages,
        temperature=0.1,
    )

    message = response.choices[0].message.content

    print(message)
