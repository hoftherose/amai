from dataclasses import dataclass
from typing import Callable

from ollama import chat, ChatResponse, Client
from ..base import Model, ModelConfig

@dataclass
class OllamaModelConfig(ModelConfig):

class OllamaModel(Model):
    def __init__(self, config: OllamaModelConfig):
        super().__init__(config)
        self.config: ModelConfig = config
        self.client: Client = self.get_client()
        self.messages: list[dict[str, str]] = []
        self.last_response: ChatResponse
        self._available_functions: dict[str, Callable[[str], str]] = {}

    def get_client(self):
        return Client(host = self.host.geturl())

    def chat(self, message: str, tools: list[Callable[[str],str]] | None = None):
        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )
        self.last_response = chat(
            messages=self.messages,
            model=self.config.model,
            tools=tools,
        )
        self.run_tool_calls()
        return self.last_response

    def run_tool_calls(self):
        if (tool_calls := self.last_response.message.tool_calls) is not None:
            for tool in tool_calls:
                function_to_call = self.available_functions.get(tool.function.name)
                if function_to_call:
                    code = tool.function.arguments.get("code")
                    if type(code) != str:
                        raise ValueError("DID NOT GET STRING")
                    output: str = function_to_call(code)
                    self.messages.append({"role": "assistant", "content": f"The result is {output}."})


    @property
    def available_functions(self) -> dict[str, Callable[[str], str]]:
        """The available_functions property."""
        return self._available_functions

    @available_functions.setter
    def available_functions(self, value: dict[str, Callable[[str], str]]):
        self._available_functions = value

