from crewai import Crew, Process
from agents import create_research_agent, create_writer_agent, create_reviewer_agent
from tasks import create_research_task, create_writing_task, create_review_task


class ContentCreationCrew:
    """A crew for researching, writing, and reviewing content."""
    
    def __init__(self, topic):
        """Initialize the crew with a topic."""
        self.topic = topic
        
        # Create agents
        self.research_agent = create_research_agent()
        self.writer_agent = create_writer_agent()
        self.reviewer_agent = create_reviewer_agent()
        
        # Create tasks
        self.research_task = create_research_task(self.research_agent, topic)
        self.writing_task = create_writing_task(self.writer_agent, topic)
        self.review_task = create_review_task(self.reviewer_agent)
        
    def run(self):
        """Execute the crew's workflow."""
        # Create the crew
        crew = Crew(
            agents=[
                self.research_agent,
                self.writer_agent,
                self.reviewer_agent
            ],
            tasks=[
                self.research_task,
                self.writing_task,
                self.review_task
            ],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the crew's tasks
        result = crew.kickoff()
        return result


def create_crew(topic):
    """Factory function to create a content creation crew."""
    return ContentCreationCrew(topic)
