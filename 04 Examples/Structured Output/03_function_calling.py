from services.openai_service import OpenAIService
import json

openai_service = OpenAIService()


# --------------------------------------------------------------
# Structured output example using function calling
# --------------------------------------------------------------

query = "Hi there, I have a question about my bill. Can you help me?"

function_name = "chat"

tools = [
    {
        "type": "function",
        "function": {
            "name": function_name,
            "description": f"Function to respond to a customer query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "Your response to the ticket.",
                    },
                },
                "required": ["content"],
            },
        },
    }
]

messages = [
    {
        "role": "system",
        "content": "You're a helpful customer care assistant.",
    },
    {
        "role": "user",
        "content": query,
    },
]

response = openai_service.client.chat.completions.create(
    model=openai_service.model,
    messages=messages,
    tools=tools,
    tool_choice={"type": "function", "function": {"name": function_name}},
)

tool_call = response.choices[0].message.tool_calls[0]
type(tool_call)

function_args = json.loads(tool_call.function.arguments)
type(function_args)
