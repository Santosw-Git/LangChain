# chain_Method.py
class Chain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def invoke(self, input):
        return self.llm.invoke(self.prompt.invoke(input))
