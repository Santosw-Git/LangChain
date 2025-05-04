from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda,RunnablePassthrough
from pydantic import BaseModel, Field
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
prompt1 = PromptTemplate(
    
    template="write the joke on this given topic {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt1 | llm | parser

def word_count(text):
    return len(text.split())

# coverting the function into the runnable lambda
runnable_word_counter  = RunnableLambda(word_count)

# print(runnable_word_counter.invoke("The quick brown fox jumps over the lazy dog"))

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "Word_count": runnable_word_counter

}
)

final_chain = chain | parallel_chain

result = final_chain.invoke({"topic":"black hole"})
print(result)
print(result["Word_count"])
print(result["joke"])