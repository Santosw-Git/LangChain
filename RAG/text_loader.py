from langchain_community.document_loaders import TextLoader
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

parser = StrOutputParser()

loader = TextLoader("../files/cricket.txt",encoding="utf-8")
documents = loader.load()
# print(documents)
# print(type(documents))

# print(documents[0].page_content)
# print(documents[0].metadata)

prompt = PromptTemplate(
    template="Write a 100 line summary on \n {document}",
    input_variables=["document"]
)

text_document = documents[0].page_content

chain = prompt | llm | parser

result = chain.invoke({"document": text_document})
print(result)