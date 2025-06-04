"""
Assistant Team - AI Calendar Management System

A CrewAI-powered calendar assistant that manages events through natural language processing.
Provides intelligent scheduling, conversation memory, and seamless calendar integration.

Author: Assistant Team Developer
License: MIT
"""

__version__ = "0.4.0"
__author__ = "Assistant Team Developer"
__email__ = "developer@assistantteam.com"

from .main import (
    kickoff,
    kickoff_with_calendar_state,
    plot,
    CalendarState,
    CalendarFlow
)

__all__ = [
    "kickoff",
    "kickoff_with_calendar_state", 
    "plot",
    "CalendarState",
    "CalendarFlow",
]
