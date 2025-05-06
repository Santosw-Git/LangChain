from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from weather import get_weather_data  # import the tool function
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash",  
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY,
)

search_tool = DuckDuckGoSearchRun()
weather_tool = get_weather_data  

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search_tool, weather_tool],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, weather_tool],
    verbose=True
)

result = agent_executor.invoke({"input": "Find the capital city of Nepal, then find its current weather condition"})
print(result)
