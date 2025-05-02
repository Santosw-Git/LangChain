from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
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
    template = "WRITE THE NOTES FROM THE GIVEN DOCUMENT\n {document}",
    input_variables=["document"]
)

prompt2 = PromptTemplate(
    template="Generate the quiz from the following document. /n {document}",
    input_variables=["document"]
)

prompt3 = PromptTemplate(
    template="Merge the given Notes and Quiz. /n {notes} /n {quiz}",
    input_variables=["notes", "quiz"]
)

document = """MySQL is a widely used open-source relational database management system (RDBMS) developed originally by MySQL AB and now owned by Oracle Corporation. It uses Structured Query Language (SQL) to manage and manipulate data, making it a powerful tool for storing structured information. MySQL is known for its speed, reliability, and ease of use, which has led to its widespread adoption in web development, data warehousing, and cloud applications. It supports a variety of storage engines such as InnoDB, which provides ACID-compliant transactions, and MyISAM, which is optimized for fast read operations. MySQL runs on multiple platforms including Windows, Linux, and macOS, and is often used as part of the LAMP stack (Linux, Apache, MySQL, PHP/Python). Key features of MySQL include strong security with access control and encryption, scalability to handle large datasets, and support for replication to improve availability and performance. Its open-source nature makes it freely available, with commercial versions offering additional features for enterprise use. The database is highly compatible with many programming languages and frameworks, including PHP, Java, Python, and Node.js. Despite its many strengths, MySQL does have some limitations, such as less comprehensive support for advanced analytics and strict ANSI SQL compliance compared to other systems like PostgreSQL. Still, it remains a top choice for developers and businesses due to its active community, extensive documentation, and the robustness required for both small-scale and large-scale applications. Whether used in content management systems like WordPress or in complex e-commerce platforms, MySQL continues to be a dependable and efficient solution for relational data storage and management.
"""
parser =  StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | llm | parser,
        "quiz": prompt2 | llm | parser
    }
)

merge_chain = prompt3 | llm | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"document": document})
print(result)