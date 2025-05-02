import random
from promptemplate import PromptTemplate
from chain_Method import Chain
class LLM:
    def __init__(self):
        print("The llm is created")

    def invoke(self, input):
        dummpy_reponse=[
            "The black hole is not black",
            "the sun is not black",
            "The great scientist is Tikola Tesla"
        ]

        return {
            "Response": random.choice(dummpy_reponse)
        }
    
llm=LLM()
# print(llm)

# print(llm.predict("black hole"))

template = PromptTemplate(
    template='generate the some reponse about the topic {topic} \n',
    input_variables=['topic']
    
)

chain = Chain(llm, template)

result = chain.invoke({'topic':'black hole'})
print(result)