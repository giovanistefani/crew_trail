# CrewAI Trail

A content creation workflow powered by CrewAI that demonstrates how multiple AI agents can collaborate to research, write, and review high-quality content.

## Overview

CrewAI Trail is a demonstration project that uses the [CrewAI](https://github.com/joaomdmoura/crewAI) framework to orchestrate a team of AI agents working together. The system includes:

- **Research Agent**: Gathers comprehensive information on a given topic
- **Writer Agent**: Creates engaging content based on research findings
- **Reviewer Agent**: Reviews and ensures quality of the final output

## Features

- 🤖 Multi-agent collaboration using CrewAI
- 🔍 Automated research and information gathering
- ✍️ Content generation with AI-powered writing
- ✅ Quality review and validation
- 🔄 Sequential workflow process
- 💬 Interactive command-line interface

## Prerequisites

- Python 3.10 or higher
- OpenAI API key (required for agent operations)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/giovanistefani/crew_trail.git
cd crew_trail
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

## Usage

Run the main application:
```bash
python main.py
```

The application will prompt you to enter a topic for content creation. You can either:
- Enter your own topic
- Press Enter to use the default topic

The crew will then:
1. Research the topic
2. Write an article based on the research
3. Review the article for quality

## Project Structure

```
crew_trail/
├── main.py           # Entry point for the application
├── crew.py           # Crew configuration and orchestration
├── agents.py         # Agent definitions and configurations
├── tasks.py          # Task definitions for agents
├── requirements.txt  # Python dependencies
├── .env.example      # Example environment variables
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## How It Works

1. **Research Phase**: The Research Agent uses search and scraping tools to gather information about the topic
2. **Writing Phase**: The Writer Agent takes the research findings and creates a well-structured article
3. **Review Phase**: The Reviewer Agent checks the article for accuracy, clarity, and quality

All agents work sequentially, with each agent building upon the work of the previous one.

## Dependencies

- `crewai`: Framework for orchestrating AI agents
- `crewai-tools`: Additional tools for agents (search, web scraping)
- `python-dotenv`: Environment variable management

## Configuration

You can customize the agents and tasks by modifying:
- `agents.py`: Agent roles, goals, and backstories
- `tasks.py`: Task descriptions and expected outputs
- `crew.py`: Crew composition and process flow

## Troubleshooting

### API Key Issues
If you see an error about the API key:
- Ensure your `.env` file exists and contains a valid `OPENAI_API_KEY`
- Check that the key is properly formatted (no extra spaces)

### Installation Issues
If you encounter installation problems:
- Ensure you're using Python 3.10 or higher
- Try creating a virtual environment first:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI)
- Powered by OpenAI's language models