# Building an AI-Powered Calendar Agent: A Developer's Journey

## The Problem

I wanted to experiment with building an AI agent, starting with a vision of automated code managing my calendar scheduling. But that scope was too ambitious for a first project, so I decided to start small and solve a specific pain point: Google Calendar's form for creating new events is slow and inefficient. I wanted to use an LLM to make this process faster and more natural.

## Technology Choices and Why

### CrewAI Framework
I picked CrewAI because I first saw it mentioned on Twitter and wanted to learn about AI agent orchestration. Initially, I planned to have the LLM read existing calendar data, but I quickly realized users wouldn't want to share that sensitive information. So I scoped down to focus strictly on new event scheduling.

### WhatsApp Over Telegram
I debated between WhatsApp and Telegram. While Telegram has a more polished API and I had prior experience with it, I chose WhatsApp because:
- It's the app I use daily for note-taking and communication
- It's the most popular messaging app across Europe
- I wanted to make adoption as easy as possible for potential users

## Technical Implementation

### Google Calendar Integration
I couldn't find an easy, ready-to-use solution online, so I quickly coded my own Google Calendar tool with help from Claude AI.

### Microservices Architecture
I had two main modules that I wanted to keep separate and work with in an organized manner. I learned about `pip install -e .` which allows you to install local modules in your pip environment and use them across external projects. This approach let me maintain clean separation while testing each component independently.

### CrewAI Agent Orchestration
As I continued scoping down and focusing on efficiency, I realized I could accomplish the task with just one AI role, making the multi-agent framework almost obsolete. However, I continued building with CrewAI because I wanted to learn more about agent orchestration.

### Prompt Engineering
I focused on making the AI as accurate as possible through careful prompt design:

```python
You are .... Your sole task is ... from {user_input}, ... taking into account ... {current_date}.
```

I used arguments and context to improve accuracy, and included strict formatting rules:

```python
IMPORTANT DATE FORMAT INSTRUCTIONS:
  • The {current_date} value is provided in European/International format (DD/MM/YYYY)
  ...
  • When processing relative dates like "tomorrow", calculate based on the European format {current_date}
```

I also defined clear output requirements:

```python
Your output MUST
  • Be a **Python list of dictionaries** (valid JSON). 
...
```

To address hallucinations, I included explicit fallback instructions:

```python
  • If the user's input does not describe any new events, output an empty list: []
```

### Development Methodology
My approach was methodical: create a small module (like the calendar integration), test it thoroughly, create the CrewAI module, test it independently, then integrate them together. I only moved to the next step after ensuring each component worked perfectly in isolation.

## Infrastructure Decisions

### Backend: FastAPI
I chose FastAPI over Flask because:
- The example code looked cleaner and clearer to me
- I needed async support to handle multiple concurrent requests without appearing slow

### Hosting: Self-Hosted vs VPS
I chose to self-host rather than use a VPS because I wanted to own the server and avoid monthly payments. In retrospect, this might have been a false economy - it didn't actually save money and added complexity.

I initially tried a Raspberry Pi but ran into ARM architecture compatibility issues, so I bought a $100 x86 PC instead.

### Security
Since I was running locally, I had to expose the server to the internet safely. I used ngrok to create a secure tunnel rather than opening ports directly.

## Making It Public: SaaS Implementation

### Frontend Registration
Once everything worked locally, I needed to make it accessible to the public. I created a simple registration UI with Claude AI and hosted it free on Vercel. I incorporated Google OAuth for easy user access and to obtain calendar manipulation tokens.

### Serverless Functions
I chose AWS Lambda over Google Cloud Functions (Google had unfixable payment issues on my end). I used AWS Lambda for the Google OAuth callback to generate and store tokens in AWS DynamoDB.

### User Flow
The complete flow works like this:
1. User sends a message on WhatsApp
2. System retrieves user tokens from database
3. AI processes the input and creates calendar events

### Landing Page
I created a landing page using Bolt.run and hosted it on Netlify.

### Custom Domain Setup
After having both a landing page and registration page, I wanted to own a domain and have them both under one unified name. I chose "r2r.site" (r2r meaning Artur) and purchased the domain. I then configured both hosted sites to work under my custom domain, giving the project a more professional appearance.

## Production Deployment

### WhatsApp Business Integration
I moved from a testing number to production by purchasing a €2.50 phone number and connecting it to Meta Business.

### Linux Deployment
On my new PC, I set up Ubuntu for a nice UI, then used SSH to download my 4 GitHub repositories, install dependencies, configure ngrok and environment variables, and deploy everything.

## Results

The system has been running untouched for 2 months, and I use it every day. The total cost is:
- Electricity for the home server
- €2.50 for the WhatsApp number
- ~€0.01 monthly for AWS services

## Key Learnings

1. **Start small**: Scoping down from a grand vision to a specific problem made the project achievable
2. **Methodical development**: Testing each component independently before integration saved debugging time
3. **User-first thinking**: Choosing WhatsApp over technically superior alternatives based on user adoption
4. **Prompt engineering matters**: Careful attention to AI instructions and output formatting prevents many issues
5. **Total cost of ownership**: Self-hosting isn't always cheaper when you factor in time and complexity

This project taught me valuable lessons about AI integration, microservices architecture, and the importance of solving real problems with appropriate technology choices.

