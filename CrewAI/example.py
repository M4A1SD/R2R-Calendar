#!/usr/bin/env python
"""
Example usage of the Assistant Team Calendar Management System.

This script demonstrates how to use the assistant_team package for
natural language calendar event management.

Make sure to set your OPENAI_API_KEY in a .env file before running.
"""

import asyncio
import os
from assistant_team import kickoff, kickoff_with_calendar_state, CalendarState

def basic_example():
    """Example of basic usage with default kickoff."""
    print("🚀 Running basic example...")
    print("Note: This will start an interactive flow")
    
    # Uncomment the line below to run the interactive flow
    # kickoff()

async def advanced_example():
    """Example of advanced usage with custom state."""
    print("🎯 Running advanced example with custom state...")
    
    # Create a custom state with conversation context
    custom_state = CalendarState(
        chat_history="User mentioned they have a busy week next week and need to schedule important meetings.",
        user_input="Schedule a team meeting tomorrow at 2pm in the main conference room and a client presentation on Friday at 10am",
        existing_events="Tomorrow 10:00 AM - 11:00 AM: Daily standup meeting\nFriday 2:00 PM - 3:00 PM: One-on-one with manager"
    )
    
    try:
        # Process the request asynchronously
        events_added = await kickoff_with_calendar_state(custom_state)
        
        print(f"\n✅ Successfully processed calendar request!")
        print(f"📅 Added {len(events_added)} event(s):")
        
        for i, event in enumerate(events_added, 1):
            print(f"\n{i}. {event.get('summary', 'Untitled Event')}")
            print(f"   📍 Location: {event.get('location', 'No location')}")
            print(f"   🕐 Start: {event.get('start', {}).get('dateTime', 'Unknown')}")
            print(f"   🕑 End: {event.get('end', {}).get('dateTime', 'Unknown')}")
            
    except Exception as e:
        print(f"❌ Error processing calendar request: {e}")

def main():
    """Main function to run examples."""
    print("🤖 Assistant Team Calendar Management - Examples")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        return
    
    print("\n1. Basic Example (Interactive)")
    basic_example()
    
    print("\n2. Advanced Example (Programmatic)")
    asyncio.run(advanced_example())
    
    print("\n🎉 Examples completed!")

if __name__ == "__main__":
    main() 