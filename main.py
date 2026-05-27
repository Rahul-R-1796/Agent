from anthropic.types import capability_support
from langchain.agents import create_agent
import os
import pymupdf
from dotenv import load_dotenv
load_dotenv()
def main():
    print("Hello from agent-repo!")
    doc = pymupdf.open("File_Repo/tamil_nadu_wiki.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    print(text)
    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_agent(
        model="openai:gpt-5.4",
        tools = [get_weather],
        system_prompt="You are a helpful Assistant",
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": "Whatclear's the weather in San Francisco?"}]}
    )
    print(result["messages"][-1].content_blocks)


if __name__ == "__main__":
    main()
