# 🤖 Assistant Team - AI Calendar Management

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/powered%20by-CrewAI-orange.svg)](https://crewai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced AI-powered calendar assistant built with [CrewAI](https://crewai.com) that manages your calendar events through natural language processing. This intelligent system can understand, schedule, and manage calendar events using conversational AI.

## ✨ Features

- 🗣️ **Natural Language Processing**: Schedule events using everyday language
- 📅 **Smart Calendar Integration**: Seamless integration with calendar systems
- 🧠 **Conversation Memory**: Maintains context across interactions
- 🌍 **Timezone Support**: Intelligent timezone handling (Asia/Jerusalem)
- 🔄 **Flexible State Management**: Customizable conversation states
- 📊 **Event Parsing**: Extract multiple events from complex descriptions
- 🎯 **Conflict Detection**: Aware of existing events to prevent conflicts

## 🚀 Quick Start

### Prerequisites

- Python 3.10-3.12
- OpenAI API key
- `my_calendar_module` installed in your environment

### Installation

```bash
# Clone the repository
git clone https://github.com/M4A1SD/assistant-team.git
cd assistant-team

# Install in development mode
pip install -e .

# Or install directly from GitHub
pip install git+https://github.com/M4A1SD/assistant-team.git
```

### Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 📖 Usage

### Basic Usage

```python
from assistant_team import kickoff

# Simple kickoff with default state
kickoff()
```

### Advanced Usage with Custom State

```python
from assistant_team import kickoff_with_calendar_state, CalendarState

# Create a custom state with context
custom_state = CalendarState(
    chat_history="User mentioned wanting to meet with the development team.",
    user_input="Schedule a team meeting tomorrow at 2pm in the conference room",
    existing_events="25/2/2025 10:00 AM - 11:00 AM: Daily standup meeting"
)

# Process the request asynchronously
events_added = await kickoff_with_calendar_state(custom_state)
print(f"Successfully added {len(events_added)} events")
```

### Calendar State Model

```python
class CalendarState(BaseModel):
    chat_history: str = ""        # Previous conversation context
    user_input: str = ""          # Current user request
    existing_events: str = ""     # Current calendar events
    events_added: list = []       # Newly created events
```

## 🏗️ Project Structure

```
assistant_team/
├── src/
│   └── assistant_team/
│       ├── main.py                    # Main flow implementation
│       ├── utils.py                   # Utility functions
│       ├── crews/
│       │   └── calendar_crew/
│       │       ├── calendar_crew.py   # Crew implementation
│       │       └── config/
│       │           ├── agents.yaml    # Agent configurations
│       │           └── tasks.yaml     # Task definitions
│       └── tools/                     # Custom tools directory
├── pyproject.toml                     # Project configuration
├── README.md                          # Project documentation
└── .gitignore                         # Git ignore rules
```

## 🛠️ Development

### Setting up for Development

```bash
# Clone the repository
git clone https://github.com/yourusername/assistant-team.git
cd assistant-team

# Install in development mode with dependencies
pip install -e .

# Run the flow visualizer
python -c "from assistant_team.main import plot; plot()"
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

## 📝 API Reference

### Main Functions

- `kickoff()`: Start the calendar flow with default settings
- `kickoff_with_calendar_state(state)`: Start with custom state (async)
- `plot()`: Visualize the CrewAI flow structure

### Utilities

- `get_current_date()`: Get formatted current date/time
- `extract_json_from_text(text)`: Parse JSON from LLM responses

## 🌐 Date Format Support

This assistant uses **European date format (DD/MM/YYYY)** by default:
- "4/3" means March 4th (not April 3rd)
- "15/12" means December 15th
- Timezone: Asia/Jerusalem with automatic DST handling



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Join CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## 🆘 Support

For questions, issues, or contributions:
- 📧 Email: developer@assistantteam.com
- 🐛 Issues: [GitHub Issues](https://github.com/M4A1SD/assistant-team/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/M4A1SD/assistant-team/discussions)

---

**Built with ❤️ using CrewAI**
