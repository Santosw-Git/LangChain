from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "what is your country name?"
documents = [
    "what is your country name?",
    "the name of my country is Nepal",
    "I am from Nepal",
    "I live in Nepal"
]

# result = embeddings.embed_query(text)
result = embeddings.embed_documents(documents)
print(str(result))