
from runnables import Runnable

class RunnableConnector(Runnable):
    
    def __init__(self, runnablesList):
        self.runnablesList = runnablesList

    def invoke(self, input):
        for runnable in self.runnablesList:
            input = runnable.invoke(input)

        return input
