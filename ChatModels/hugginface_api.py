from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    
)

model = ChatHuggingFace(
    llm=endpoint
)

result = model.invoke("Who is the father of physics??")
print(result.content)
