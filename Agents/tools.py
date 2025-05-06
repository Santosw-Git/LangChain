from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import requests
from langchain_core.tools import tool

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",  
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY,
    # max_output_tokens=200
)

# Tool creation
@tool

def multiply_numbers(x: int, y: int) -> int:
    '''On given 2 numbers x and y it multiplies them and returns the result'''
    return x * y

print(multiply_numbers.invoke({'x':2,'y':3}))
print(multiply_numbers.args)
print(multiply_numbers.description)
print(multiply_numbers.name)

# Tool binding
# Tool binding is the mechanism by which an LLM is linked to external tools—like web search, calculators, code execution environments, or custom APIs—so it can invoke these tools during inference to provide more accurate or dynamic outputs.

llm_with_tools = llm.bind_tools([multiply_numbers])
