from crewai import Agent, Crew
from langchain.chat_models import ChatOpenAI

planner = Agent("Planner", llm=ChatOpenAI(), goal="Create test strategy for feature changes")
executor = Agent("Executor", llm=ChatOpenAI(), goal="Write and validate test cases")

crew = Crew(name="Autonomous QA Team", agents=[planner, executor])
crew.kickoff("Validate user signup and profile update features")
