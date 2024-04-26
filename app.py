from langchain_community.chat_models import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain

print("Launching LLM Agent Learning Project")

llm = ChatOllama(model="llama3:instruct", temperature=0)
summary_template = """
Given the information {information} about a person I want you to create:
1. A short summary
2. Two interesting facts about them
"""

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

chain = LLMChain(llm=llm, prompt=summary_prompt_template)

res = chain.invoke(input={"information": "joe is a really cool guy that'd 33 yrs old"})

print(res['text'])