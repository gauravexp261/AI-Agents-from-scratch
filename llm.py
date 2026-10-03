import json
import os
import urllib.request
from dataclasses import dataclass
from openai import OpenAI



# Format
@dataclass
class Response:
    """Structured response from LLM calls."""
    content: str = ""
    reasoning: str | None = None
    tool_call: dict | None = None
    metadata: dict | None = None
    

class LLM:
    def __init__(
        self,
        model: str,
        api_key: str = "ollama",
        think: bool = False,
        temperature: float | None = None,):
       
        """Initialize the LLM with the given model."""

        self.model = model
        self.base_url = "http://localhost:11434/v1"
        self.api_key = api_key
        self.think = think
        self.temperature = temperature

        # OpenAI client configured to talk to Ollama
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )
        
    def generate(
        self,
        messages: list[dict],
        tools: list | None = None,
    ) -> Response:
        """Generate a response from the LLM."""

        # Build optional parameters
        kwargs = {}

        if tools:
            kwargs["tools"] = tools

        if not self.think:
            kwargs["reasoning_effort"] = "none"
        else:
            kwargs["reasoning_effort"] = "medium"

        if self.temperature is not None:
            kwargs["temperature"] = self.temperature

        # Call Ollama through OpenAI SDK
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs,
        )

        # Extract assistant message
        message = response.choices[0].message
                    
        # Extract reasoning
        reasoning = getattr(message, "reasoning", None)

        if reasoning is None:
            reasoning = getattr(message, "reasoning_content", None)

        # Extract tool call
        tool_calls = message.tool_calls
        tool_call = tool_calls[0] if tool_calls else None

        # Metadata
        metadata = {
            "model": response.model,
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
        }

        return Response(
            content=message.content,
            reasoning=reasoning,
            tool_call=tool_call,
            metadata=metadata,
        )
        
        
if __name__ == "__main__":       
    llm = LLM(model="gemma4:latest", think=True)
    response = llm.generate([{"role": "user", "content": "what is 2+2"}])
    print(response)