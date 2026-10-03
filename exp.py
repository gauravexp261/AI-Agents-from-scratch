from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1",
    api_key="ollama")

response = client.chat.completions.create(
    model="gemma4:latest",
    messages=[
        {
            "role": "user",
            "content": "Explain MCP like I'm 15"
        }
    ], {"reasoning_effort":"none"}
)

a = {'b':2}
print(**a)