from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4.1', api_key="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")
result = llm.invoke("What is the capital of France?")
print(result)