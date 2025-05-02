from runnables import Runnable
class PromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input):
        return self.template.format(**input)

# template = PromptTemplate(
#     template='generate the some reponse about the topic {topic} \n',
#     input_variables=['topic']
    
# )
# result = template.invoke({'topic':'black hole'})
# print(result)