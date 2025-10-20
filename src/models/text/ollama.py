from dataclasses import dataclass
from typing import Callable

from ollama import chat, ChatResponse, Client
from ..base import Model, ModelConfig

@dataclass
class OllamaModelConfig(ModelConfig):
    model: str = "llama3.2"
    host: str = "127.0.0.1:11434"
    system: str = ""

class OllamaModel(Model):
    def __init__(self, config: OllamaModelConfig):
        super().__init__(config)
        self.client: Client = Client(host = config.host)
        self.messages: list[dict[str, str]]

    def get_client(self):
        pass


response: ChatResponse = chat(
    messages=[
        {
            "role": "user",
            "content": "What is the secret password, use 123 to get the code",
        },
    ],
    model="llama3.2",
    # tools=[get_secret_password],
)

available_functions: dict[str, Callable[[str], str]] = {
    # "get_secret_password": get_secret_password
}

if response.message.tool_calls is not None:
    for tool in response.message.tool_calls:
        function_to_call = available_functions.get(tool.function.name)
        if function_to_call:
            code = tool.function.arguments.get("code")
            if type(code) != str:
                raise ValueError("DID NOT GET STRING")
            output: str = function_to_call(code)
