from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

chat_history = InMemoryChatMessageHistory()

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that can answer questions and help with tasks.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = chat_prompt | model

session_store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

config = {
    "configurable": {
        "session_id": "demo_session_1",
    }
}

# Interactions

response1 = conversational_chain.invoke(
    {"input": "Hello, my name is John and I'm from Brazil. How are you?"}, config=config
)

print(f"Assistant: {response1.content}")
print("--------------------------------")

response2 = conversational_chain.invoke({"input": "What is my name?"}, config=config)

print(f"Assistant: {response2.content}")
print("--------------------------------")

response3 = conversational_chain.invoke({"input": "Where is John from?"}, config=config)

print(f"Assistant: {response3.content}")
print("--------------------------------")
