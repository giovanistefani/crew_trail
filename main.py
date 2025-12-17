#!/usr/bin/env python3
"""
CrewAI Trail - A content creation workflow using CrewAI

This application demonstrates how to use CrewAI to orchestrate multiple AI agents
working together to research, write, and review content.
"""

import os
from dotenv import load_dotenv
from crew import create_crew


def main():
    """Main entry point for the CrewAI Trail application."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        print("You can use .env.example as a template.")
        return
    
    print("=" * 60)
    print("Welcome to CrewAI Trail!")
    print("=" * 60)
    print()
    
    # Get topic from user
    topic = input("Enter a topic for content creation (or press Enter for default): ").strip()
    
    if not topic:
        topic = "The impact of artificial intelligence on modern business"
        print(f"Using default topic: {topic}")
    
    print()
    print("=" * 60)
    print("Starting the crew workflow...")
    print("=" * 60)
    print()
    
    try:
        # Create and run the crew
        crew = create_crew(topic)
        result = crew.run()
        
        print()
        print("=" * 60)
        print("Crew execution completed!")
        print("=" * 60)
        print()
        print("Final Result:")
        print("-" * 60)
        print(result)
        print("-" * 60)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check your API key and try again.")


if __name__ == "__main__":
    main()
