from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
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


class FeedBack(BaseModel):
    sentiment:  Literal["positive", "negative"] = Field(description="Feed back of given review")

parser2=PydanticOutputParser(pydantic_object=FeedBack)
parser = StrOutputParser()

template1 = PromptTemplate(
    template="Write the sentiment of given topic. /n {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
    
)

classifier_chain = template1 | llm | parser2

# result = classifier_chain.invoke({'topic':'you are wounderful'}).sentiment
# print(result)

template2 = PromptTemplate(
    template="Write the simple response of given positive feedback. \n {feedback}",
    input_variables=["feedback"],
)

template3 = PromptTemplate(
    template="Write the simple response of given negative feedback. \n {feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', template2|llm|parser),
    (lambda x: x.sentiment == 'negative', template3|llm|parser),
    RunnableLambda(lambda x: "counld find the sentiment")
)

chain = classifier_chain | branch_chain
result = chain.invoke({'topic':'you are not wounderful'})
print(result)