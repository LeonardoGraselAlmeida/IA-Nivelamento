from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke about my name!",
)

text = prompt.format(name="John")

print(text)
