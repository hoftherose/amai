from typing import Callable

from ollama import chat, ChatResponse


class ChatSession:
    def __init__(self):
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
