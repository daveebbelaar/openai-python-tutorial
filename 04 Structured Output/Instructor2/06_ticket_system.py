import instructor
from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum


# --------------------------------------------------------------
# Ticket System Example with Structured Output
# --------------------------------------------------------------

# Patch the OpenAI client
client = instructor.from_openai(OpenAI())


class TicketCategory(str, Enum):
    """Enumeration of categories for incoming tickets."""

    GENERAL = "general"
    ORDER = "order"
    BILLING = "billing"


class CustomerSentiment(str, Enum):
    """Enumeration of customer sentiment labels."""

    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"


class Ticket(BaseModel):
    reply: str = Field(description="Your reply that we send to the customer.")
    category: TicketCategory
    confidence: float = Field(ge=0, le=1)
    sentiment: CustomerSentiment


def process_ticket(customer_message: str) -> Ticket:
    reply = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=Ticket,
        max_retries=3,
        messages=[
            {
                "role": "system",
                "content": "Analyze the incoming customer message and predict the values for the ticket.",
            },
            {"role": "user", "content": customer_message},
        ],
    )

    return reply


# --------------------------------------------------------------
# Billing Issue Example
# --------------------------------------------------------------

ticket = process_ticket("Hi there, I have a question about my bill. Can you help me?")
assert ticket.category == TicketCategory.BILLING

ticket.reply
ticket.category
ticket.confidence
ticket.sentiment

# --------------------------------------------------------------
# Order-Related Example
# --------------------------------------------------------------

ticket = process_ticket("I would like to place an order.")
assert ticket.category == TicketCategory.ORDER
