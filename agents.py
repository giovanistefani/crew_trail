from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


def create_research_agent():
    """Create a research agent that gathers information."""
    return Agent(
        role="Research Analyst",
        goal="Gather comprehensive and accurate information on given topics",
        backstory="""You are an experienced research analyst with a keen eye for detail.
        You excel at finding relevant information from various sources and synthesizing 
        it into clear, actionable insights.""",
        tools=[search_tool, scrape_tool],
        verbose=True,
        allow_delegation=False
    )


def create_writer_agent():
    """Create a writer agent that produces content."""
    return Agent(
        role="Content Writer",
        goal="Create engaging and well-structured content based on research",
        backstory="""You are a talented content writer with years of experience in 
        creating compelling narratives. You have a gift for transforming complex 
        information into clear, engaging content that resonates with readers.""",
        verbose=True,
        allow_delegation=False
    )


def create_reviewer_agent():
    """Create a reviewer agent that ensures quality."""
    return Agent(
        role="Quality Reviewer",
        goal="Review content for accuracy, clarity, and quality",
        backstory="""You are a meticulous editor with an exceptional attention to detail.
        You ensure that all content meets the highest standards of quality, accuracy,
        and clarity before publication.""",
        verbose=True,
        allow_delegation=True
    )
