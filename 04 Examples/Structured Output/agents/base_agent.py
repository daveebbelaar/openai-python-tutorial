from abc import ABC, abstractmethod
from services.openai_service import OpenAIService


class Agent(ABC):
    def __init__(self, successor=None):
        self.successor = successor
        self.openai_service = OpenAIService()

    @abstractmethod
    def process(self, ticket):
        pass
