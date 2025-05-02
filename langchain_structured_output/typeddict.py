from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from typing import TypedDict, Annotated,Optional

from dotenv import load_dotenv

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id = "HuggingFaceH4/zephyr-7b-beta",
    task = "summarization",
)

model = ChatHuggingFace(
    llm=endpoint
)

class Review(TypedDict):
    summary: Annotated[str, "The summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review"] 
    pros: Annotated[Optional[list[str]], "The pros of the review"]
    cons: Annotated[Optional[list[str]], "The cons of the review"]
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("I can't believe how disappointing this entire experience has been. Nothing worked as promised, and every step was filled with frustration and regret. The service was slow, the support was unhelpful, and the product quality was shockingly poor. I wasted both time and money, and I wouldn’t recommend this to anyone looking for something reliable or worthwhile.")
print(result)


    
