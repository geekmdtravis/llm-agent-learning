from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3:instruct", temperature=0)
print("hello, attempting to run my LLM")
#response = llm.invoke("write a react-redux tool, using typescript, that calculates mean arterial blood pressure from systolic and diastolic blood pressures. it should use functional and not class components, and a newer version of redux and use slices")
response = llm.invoke("Please write a sql script that gets vital signs for a given patient by their PID ")
print(response.content)