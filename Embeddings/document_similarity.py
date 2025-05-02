from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me bumrah"

document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)


similarities = cosine_similarity([query_embedding], document_embeddings)[0]
index, score = sorted(list(enumerate(similarities)),key=lambda x:x[1],reverse=True)[0]
print(query)
print(documents[index])
print("The similarity score is",score)
