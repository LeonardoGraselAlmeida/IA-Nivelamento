from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

result = model.invoke("Hello, how are you?")
print(result.content)
