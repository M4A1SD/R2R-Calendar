#!/usr/bin/env python
"""
Assistant Team - AI Calendar Management System

This module provides the main flow implementation for the AI calendar assistant
powered by CrewAI. It handles natural language processing for calendar events
and manages conversation state.

Author: Assistant Team Developer
License: MIT
"""

import warnings
import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
import re
import json

# Suppress warnings and configure logging
warnings.filterwarnings("ignore", category=Warning)
logging.getLogger('opentelemetry').setLevel(logging.ERROR)

from pydantic import BaseModel, Field
from crewai.flow import Flow, listen, start, or_, router

# Use relative imports for better package structure
from .crews.calendar_crew.calendar_crew import CalendarCrew
from .utils import get_current_date, extract_json_from_text


class CalendarState(BaseModel):
    """
    State model for calendar conversations.
    
    Attributes:
        user_input: Current user request/input
        events_added: List of newly created events from the conversation
    """
    chat_history: str = Field(default="", description="Previous conversation context")
    user_input: str = Field(default="", description="Current user request")
    existing_events: str = Field(default="", description="Current calendar events")
    events_added: List[Dict[str, Any]] = Field(default_factory=list, description="Newly created events")


class CalendarFlow(Flow[CalendarState]):
    """
    Main flow class for handling calendar conversations using CrewAI.
    
    This flow processes user inputs through natural language understanding
    and creates calendar events using AI agents.
    """

    @start()
    def new_conversation(self) -> None:
        """Initialize a new conversation flow."""
        print("Starting new calendar conversation...")

    @listen(or_(new_conversation))
    def user_talks(self) -> None:
        """
        Validate user input before processing.
        
        Raises:
            ValueError: If no user input is provided
        """
        if not self.state.user_input.strip():
            print("ERROR: No user input provided")
            raise ValueError("User input is required")
        
        print(f"📝 Processing user input: {self.state.user_input[:100]}...")

    @listen(user_talks)
    def handle_calendar_request(self) -> List[Dict[str, Any]]:
        """
        Process calendar request using AI crew and extract events.
        
        Returns:
            List of calendar events created from the user input
            
        Raises:
            Exception: If calendar processing fails
        """
        print("📅 Processing calendar request...")
        
        try:
            # Prepare input data for the crew
            crew_inputs = {
                "user_input": self.state.user_input,
                "chat_history": self.state.chat_history,
                "existing_events": self.state.existing_events,
                "current_date": get_current_date()
            }
            
            # Execute the calendar crew
            result = (
                CalendarCrew()
                .crew()
                .kickoff(inputs=crew_inputs)
            )
            
            # Extract and parse events from crew response
            json_data = extract_json_from_text(result.raw)
            events_added = []
            
            if json_data:
                if isinstance(json_data, list):
                    events_added = json_data
                elif isinstance(json_data, dict):
                    events_added = [json_data]
                
                print(f"Successfully parsed {len(events_added)} event(s)")
            else:
                print("No events found in response")
            
            # Store events in state
            self.state.events_added = events_added
            return events_added
            
        except Exception as e:
            print(f"Error processing calendar request: {e}")
            self.state.events_added = []
            raise


async def kickoff_with_calendar_state(custom_state: CalendarState) -> List[Dict[str, Any]]:
    """
    Create and execute a calendar flow with a custom state.
    
    Args:
        custom_state: Pre-configured CalendarState with conversation context
        
    Returns:
        List of events that were successfully added to the calendar
        
    Raises:
        Exception: If flow execution fails
    """
    try:
        calendar_flow = CalendarFlow()
        
        # Set the custom state
        calendar_flow.state.chat_history = custom_state.chat_history
        calendar_flow.state.user_input = custom_state.user_input
        calendar_flow.state.existing_events = custom_state.existing_events
        
        # Execute the flow asynchronously
        await calendar_flow.kickoff_async()
        
        # Return the events that were added
        return getattr(calendar_flow.state, 'events_added', [])
        
    except Exception as e:
        print(f"❌ Error in kickoff_with_calendar_state: {e}")
        raise


def kickoff() -> None:
    """
    Start a calendar flow with default settings (synchronous).
    
    This is the main entry point for simple usage without custom state.
    """
    try:
        print("Starting calendar assistant...")
        calendar_flow = CalendarFlow()
        calendar_flow.kickoff()
    except Exception as e:
        print(f"Error in kickoff: {e}")
        raise


def plot() -> None:
    """
    Generate and display a visual plot of the calendar flow structure.
    
    Useful for understanding the flow diagram and debugging.
    """
    try:
        print("Generating flow diagram...")
        calendar_flow = CalendarFlow()
        calendar_flow.plot()
    except Exception as e:
        print(f"Error generating plot: {e}")
        raise


if __name__ == "__main__":
    # Allow direct execution of the module
    print("Assistant Team Calendar Management")
    print("Running default kickoff...")
    kickoff()
