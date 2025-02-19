import os
from typing import Any, Dict
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff
from app.src.tools.DBAPISearchTool import DBAPISearchTool
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@CrewBase
class My_Crew:
    '''My Crew class'''

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def chatbot(self) -> Agent:
        """Creates the 'chatbotAgent' agent."""

        return Agent(
            config=self.agents_config["chatbot"],  
            tools=[DBAPISearchTool()],
            verbose=True,
        )
    
    @task
    def chatbot_task(self) -> Task:
        """Creates the 'chatbotTask' task."""

        return Task(
            config=self.tasks_config["chatbot_task"],  
            human_input=True,
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the 'chatbotCrew' crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            memory=True,
            planning=True
        )
    
# if __name__ == "__main__":
#     my_crew = My_Crew()
#     result = my_crew.crew().kickoff()

#     print("###################")
#     print(result)
