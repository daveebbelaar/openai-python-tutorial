from services.openai_service import OpenAIService
import json

openai_service = OpenAIService()


# --------------------------------------------------------------
# Structured output example using response_format
# --------------------------------------------------------------

query = "Hi there, I have a question about my bill. Can you help me?"

messages = [
    {
        "role": "system",
        "content": "You're a helpful customer care assistant. Always response in json format with content as the key",
    },
    {
        "role": "user",
        "content": query,
    },
]

response = openai_service.client.chat.completions.create(
    model=openai_service.model,
    messages=messages,
    response_format={"type": "json_object"},
)

message = response.choices[0].message.content
type(message)

message_json = json.loads(message)
type(message_json)
