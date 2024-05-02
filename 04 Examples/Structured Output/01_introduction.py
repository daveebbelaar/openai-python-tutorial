from services.openai_service import OpenAIService

openai_service = OpenAIService()


# --------------------------------------------------------------
# Unstructured output example
# --------------------------------------------------------------

query = "Hi there, I have a question about my bill. Can you help me?"

messages = [
    {
        "role": "system",
        "content": "You're a helpful customer care assistant",
    },
    {
        "role": "user",
        "content": query,
    },
]

response = openai_service.client.chat.completions.create(
    model=openai_service.model,
    messages=messages,
    response_format={"type": "text"},
)

message = response.choices[0].message.content
type(message)
