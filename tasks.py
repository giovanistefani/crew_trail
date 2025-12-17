from crewai import Task


def create_research_task(agent, topic):
    """Create a research task for gathering information."""
    return Task(
        description=f"""Conduct comprehensive research on the following topic: {topic}
        
        Your research should include:
        1. Key facts and statistics
        2. Recent developments and trends
        3. Expert opinions and perspectives
        4. Relevant examples and case studies
        
        Provide a well-organized summary of your findings.""",
        agent=agent,
        expected_output="A detailed research report with key findings, statistics, and insights."
    )


def create_writing_task(agent, topic):
    """Create a writing task for content creation."""
    return Task(
        description=f"""Based on the research findings, write an engaging article about: {topic}
        
        The article should:
        1. Have a compelling introduction
        2. Present information in a logical flow
        3. Include relevant examples and data
        4. Have a strong conclusion
        5. Be approximately 500-800 words
        
        Write in a clear, professional tone that is accessible to a general audience.""",
        agent=agent,
        expected_output="A well-written article of 500-800 words with clear structure and engaging content."
    )


def create_review_task(agent):
    """Create a review task for quality assurance."""
    return Task(
        description="""Review the written article for:
        
        1. Accuracy of information
        2. Clarity and readability
        3. Grammar and spelling
        4. Logical flow and structure
        5. Overall quality and impact
        
        Provide specific feedback and suggestions for improvement.
        If the article meets all quality standards, approve it for publication.""",
        agent=agent,
        expected_output="A comprehensive review with specific feedback and final approval or revision suggestions."
    )
