# 🤖 R2R Calendar - AI-Powered Calendar Assistant

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.100%2B-FF6B6B.svg)](https://crewai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Enhanced%20Version-orange.svg)](https://github.com/yourusername/R2R-Calendar)

> **⚠️ IMPORTANT NOTICE: This is an enhanced/showcase version of a working product. This repository demonstrates improved architecture and design patterns but may not be fully functional. It was created to showcase better code organization and modular design rather than as a production-ready system.**

## 🌟 Overview

R2R Calendar is a AI-powered calendar management system that showcases advanced architecture patterns for integrating conversational AI with calendar management. This version demonstrates how to properly structure a complex system with multiple microservices, including WhatsApp messaging, Google Calendar integration, and CrewAI-powered natural language processing.

### 🏗️ What This Version Demonstrates

- **📐 Microservices Architecture**: Properly separated concerns with dedicated modules
- **🔧 Modular Design**: Each component (WhatsApp, Calendar, CrewAI) as independent packages
- **📦 Professional Packaging**: Proper Python packaging with `setup.py` and `pyproject.toml`
- **🛠️ Development Tooling**: Comprehensive setup scripts and development environment
- **📚 Documentation**: Extensive documentation and examples for each module


### 🎯 Key Features (Design Goals)

- **🗣️ Natural Language Processing**: CrewAI-powered conversation handling
- **📱 WhatsApp Integration**: Professional WhatsApp Business API wrapper
- **📅 Google Calendar Sync**: Robust calendar management module
- **🤖 AI-Powered Assistant**: Multi-agent conversation system
- **☁️ AWS Integration**: Scalable user token management
- **🔄 Event-Driven Architecture**: Proper webhook and message handling


## 🚨 Project Status

This repository represents an **enhanced architectural version** of a working calendar assistant. Key considerations:

- ✅ **Architecture**: Demonstrates best practices for microservices design
- ✅ **Code Quality**: Shows proper Python packaging and project structure
- ✅ **Documentation**: Comprehensive documentation and setup guides
- ⚠️ **Functionality**: May require additional work to be fully operational


### Why This Version Exists

This version was created to:
1. **Showcase Better Architecture**: Demonstrate how the working product is structured
2. **Learning Resource**: Serve as an example of professional Python project organization
3. **Foundation for Future Work**: Provide a solid base for further development
4. **Portfolio Piece**: Display software engineering and architecture skills

## 🏗️ Enhanced Architecture

![Architecture Flow](flow.png)

**Flow:**
1. FastAPI forwards webhook message to CrewAI with GeminiLLM
2. CrewAI processes and sends a json to Calendar Tool
3. FastAPI sends success response back to user via WhatsApp API

## 📁 Enhanced Project Structure

```
R2R-Calendar/
├── main-server/                  # 🖥️ Central orchestration server
│   ├── whatsappBridgedAgent/     # Core business logic
│   ├── requirements.txt          # Server dependencies
│   └── env.example              # Environment template
│
├── whatsapp-module/             # 📱 Professional WhatsApp wrapper
│   ├── whatsappModule/          # Core WhatsApp functionality
│   ├── examples/                # Usage examples
│   ├── pyproject.toml          # Modern Python packaging
│   └── setup.py                # Package installation
│
├── G-calendar-tool/             # 📅 Google Calendar integration
│   ├── my_calendar_module/      # Calendar API wrapper
│   ├── examples.py             # Usage demonstrations
│   ├── requirements.txt        # Module dependencies
│   └── setup.py               # Package setup
│
├── CrewAI/                     # 🤖 AI assistant engine
│   ├── src/assistant_team/     # Multi-agent AI system
│   ├── pyproject.toml         # Package configuration
│   └── CHANGELOG.md           # Version history
│
├── setup.py                   # 🚀 Automated setup system
├── .gitignore                 # Comprehensive ignore rules
└── README.md                  # This documentation
```

## 🚀 Quick Start (Setup Demo)

### Prerequisites

- Python 3.10+
- Git
- Basic understanding of microservices
- API keys (if you want to make it functional)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/R2R-Calendar.git
cd R2R-Calendar

# Run the automated setup
python setup.py

# Or for development mode
python setup.py --dev
```

### Manual Installation (for understanding)

```bash
# Install each module in development mode
pip install -e ./whatsapp-module
pip install -e ./G-calendar-tool  
pip install -e ./CrewAI

# Install main server dependencies
cd main-server
pip install -r requirements.txt
```

## 🔧 Configuration Example

The system is designed with proper configuration management:

```bash
# Copy environment template
cp main-server/env.example main-server/.env

# Edit with your credentials (if making functional)
# OPENAI_API_KEY=your_key_here
# WHATSAPP_ACCESS_TOKEN=your_token_here
# etc.
```

## 📱 Intended Usage Flow

This system was designed to handle conversations like:

```
User → WhatsApp: "Schedule a team meeting tomorrow at 2 PM"
      ↓
Meta Servers → Forward message to webhook via an ngrok tunnel
      ↓
Ngrok Tunnel → Routes to WhatsApp webhook/FastAPI
      ↓
Server Module → Extracts message content, passes to crewAI
      ↓
CrewAI (Gemini LLM) → Processes input, generates JSON
      ↓
Calendar Tool → Receives JSON, creates event
      ↓
WhatsApp API → message sent"✅ Meeting scheduled for [date] at 2:00 PM"
```

## 🛠️ Development Features

### Automated Setup
- **Comprehensive installer**: `setup.py` handles all dependencies
- **Environment validation**: Checks Python version, Git availability
- **Development mode**: Optional dev tools installation



## 📊 What You Can Learn From This Repo

### 1. **Microservices Design**
- How to properly separate concerns
- Inter-service communication patterns
- Dependency management across services

### 2. **Python Packaging**
- Modern `pyproject.toml` usage
- Setuptools configuration
- Development vs production dependencies

### 3. **Project Organization**
- Professional directory structure
- Documentation standards
- Testing organization

### 4. **Integration Patterns**
- API wrapper design
- Configuration management
- Error handling strategies

## 🤝 Contributing & Development

This repository serves as:
- **Learning Resource**: Study the architecture and patterns
- **Starting Point**: Fork and adapt for your own projects  
- **Contribution Base**: Help improve the structure and documentation

## 📄 License & Usage

MIT License - Feel free to use this architectural pattern in your own projects.

## �� Acknowledgments

- **Original Working Version**: This enhanced version is based on a functional calendar assistant
- **Architecture Focus**: Prioritizes clean code and structure over immediate functionality
- **Educational Purpose**: Designed to demonstrate professional software development practices

---

> **Note**: If you're looking for a working calendar assistant, this repo demonstrates the architecture. For production use, you would need to ensure all integrations are properly configured and tested. 