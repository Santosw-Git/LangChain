from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",  
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY,
    # max_output_tokens=200
)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser

input_data = {'topic': 'black hole'}

result = chain.invoke(input_data)

print(result)
print(type(result))

# Optionally, visualize the chain's graph
chain.get_graph().print_ascii()
