

# StructuredOutputParser is a parser that expects the model's output to follow a structured schema like a Python Pydantic model (which defines fields and types).
# It parses the raw LLM output (like messy text) into a structured Python object.

# Why use StructuredOutputParser instead of simple JsonOutputParser?
# **Use `StructuredOutputParser` instead of `JsonOutputParser` because it validates, corrects, and structures the model's output safely using Pydantic models, even when the output is imperfect.**

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema

load_dotenv()

import os 
# print(os.environ["HUGGINGFACEHUB_API_TOKEN"])

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = "fact1", description="The first fact of the schema"),
    ResponseSchema(name = "fact2", description="The second fact of the schema"),
    ResponseSchema(name = "fact3", description="The third fact of the schema")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give 3 facts about the {topic} \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# promt = template.invoke({"topic":"black_hole"})

# result = model.invoke(promt)

# final_data = parser.parse(result.content)
# print(final_data)

chain = template | model | parser

result = chain.invoke({"topic": "black_hole"})
print(result)
