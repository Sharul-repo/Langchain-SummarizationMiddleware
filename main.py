from langchain.agents.middleware import SummarizationMiddleware
from model import local_llm
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

llm = local_llm()
summerizer_llm = local_llm()

def add_tool(a: float, b: float) -> float:
    """add 2 numbers"""
    return a + b

def multiplication_tool(a: float, b: float) -> float:
    """multiply 2 numbers"""
    return a * b

checkpointer = InMemorySaver()

agent = create_agent(
    model=llm,
    tools=[add_tool, multiplication_tool],
    prompt="You are an assistant who replies in 10 words only.",
    checkpointer=checkpointer,
    middleware=[
        SummarizationMiddleware(
            model=summerizer_llm,
            max_tokens_before_summary=2000,
            messages_to_keep=20,
            summary_prompt="Summarize previous context briefly.",
        ),
    ],
)

config = {"configurable": {"user_id": "1", "thread_id": "1"}}

def main():
    while True:
        user_input = input("Chat with the assistant: ")
        if user_input.lower().strip() == "exit":
            print("👋 Goodbye!")
            break

        result = agent.invoke({"messages": [{"role": "user", "content": user_input}]}, config=config)

        print(result)

if __name__ == "__main__":
    main()
