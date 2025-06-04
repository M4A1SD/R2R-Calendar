"""
Calendar Crew Implementation

This module defines the Calendar Crew that handles natural language processing
for calendar event creation and management using CrewAI.

Author: Assistant Team Developer
License: MIT
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@CrewBase
class CalendarCrew:
    """
    Calendar Crew for AI-powered calendar event management.
    
    This crew processes natural language inputs to create and manage
    calendar events using specialized AI agents and tasks.
    """

    # Configuration files for agents and tasks
    # Learn more about YAML configuration:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def calendar_event_manager(self) -> Agent:
        """
        Create the Calendar Event Manager agent.
        
        This agent specializes in interpreting user requests and managing
        calendar information with natural language understanding.
        
        Returns:
            Agent: Configured calendar event manager agent
        """
        return Agent(
            config=self.agents_config["Calendar_event_manager"],
            verbose=True,
        )

    @task
    def create_calendar_events(self) -> Task:
        """
        Create the calendar events creation task.
        
        This task processes user input and generates structured calendar
        events in the proper format for calendar integration.
        
        Returns:
            Task: Configured calendar event creation task
        """
        return Task(
            config=self.tasks_config["Create_calendar_events"],
            agent=self.calendar_event_manager,
        )

    @crew
    def crew(self) -> Crew:
        """
        Create the Calendar Crew.
        
        Assembles the calendar event manager agent and creation task
        into a cohesive crew for processing calendar requests.
        
        Returns:
            Crew: Configured calendar management crew
        """
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
