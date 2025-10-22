from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain.prompts import PromptTemplate

load_dotenv()

question_template = PromptTemplate(
    input_variables=["product"], template="What is the color of a {product}?"
)

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)

chain = question_template | model

result = chain.invoke({"product": "apple"})

print(result.content)
