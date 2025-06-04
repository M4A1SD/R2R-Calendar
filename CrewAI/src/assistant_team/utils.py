#!/usr/bin/env python
"""
Utility functions for the Assistant Team calendar management system.

This module provides helper functions for date handling and JSON parsing
from AI model responses.

Author: Assistant Team Developer
License: MIT
"""

import re
import json
from datetime import datetime
from typing import Union, Dict, List, Any, Optional


def get_current_date() -> str:
    """
    Get the current date and time in a formatted string.
    
    Returns:
        str: Current date and time in format "day: X, month: Y, year: Z, time: HH:MM AM/PM"
        
    Example:
        >>> get_current_date()
        'day: 15, month: 3, year: 2024, time: 02:30 PM'
    """
    try:
        now = datetime.now()
        return f"day: {now.day}, month: {now.month}, year: {now.year}, time: {now.strftime('%I:%M %p')}"
    except Exception as e:
        # Fallback to ISO format if formatting fails
        print(f"⚠️ Warning: Error formatting date, using ISO format: {e}")
        return datetime.now().isoformat()


def extract_json_from_text(text: str) -> Optional[Union[Dict[str, Any], List[Dict[str, Any]]]]:
    """
    Extract and parse JSON data from text that may contain code blocks or raw JSON.
    
    This function handles various formats:
    - JSON wrapped in ```json code blocks
    - Raw JSON strings
    - JSON arrays and objects
    - Malformed JSON with trailing characters
    
    Args:
        text (str): Text that may contain JSON data
        
    Returns:
        Union[Dict, List, None]: Parsed JSON object/array if successful, None otherwise
        
    Example:
        >>> extract_json_from_text('```json\\n[{"event": "meeting"}]\\n```')
        [{'event': 'meeting'}]
        
        >>> extract_json_from_text('[{"event": "meeting"}]')
        [{'event': 'meeting'}]
    """
    if not text or not isinstance(text, str):
        print("⚠️ Warning: Invalid input text for JSON extraction")
        return None
    
    # Clean up the text
    text = text.strip()
    
    # Try different extraction strategies
    extraction_strategies = [
        _extract_from_code_block,
        _extract_from_json_array,
        _extract_from_json_object,
        _extract_raw_json
    ]
    
    for strategy in extraction_strategies:
        try:
            result = strategy(text)
            if result is not None:
                return result
        except Exception as e:
            continue  # Try next strategy
    
    print("❌ extract_json_from_text(): Failed to parse JSON with all strategies")
    return None


def _extract_from_code_block(text: str) -> Optional[Union[Dict[str, Any], List[Dict[str, Any]]]]:
    """Extract JSON from markdown code blocks."""
    # Try to find JSON in code blocks
    patterns = [
        r'```json\s*\n(.*?)\n\s*```',  # Standard JSON code block
        r'```\s*\n(.*?)\n\s*```',      # Generic code block
        r'`([^`]+)`'                    # Inline code
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            json_str = match.group(1).strip()
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                continue
    
    return None


def _extract_from_json_array(text: str) -> Optional[List[Dict[str, Any]]]:
    """Extract JSON array starting with [."""
    if text.startswith('['):
        # Clean trailing characters
        text = text.rstrip('`').rstrip()
        try:
            result = json.loads(text)
            if isinstance(result, list):
                return result
        except json.JSONDecodeError:
            pass
    
    return None


def _extract_from_json_object(text: str) -> Optional[Dict[str, Any]]:
    """Extract JSON object starting with {."""
    if text.startswith('{'):
        # Clean trailing characters
        text = text.rstrip('`').rstrip()
        try:
            result = json.loads(text)
            if isinstance(result, dict):
                return result
        except json.JSONDecodeError:
            pass
    
    return None


def _extract_raw_json(text: str) -> Optional[Union[Dict[str, Any], List[Dict[str, Any]]]]:
    """Try to parse the entire text as JSON."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to find JSON-like content with regex
        json_pattern = r'(\[.*?\]|\{.*?\})'
        matches = re.findall(json_pattern, text, re.DOTALL)
        
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    
    return None


def validate_calendar_event(event: Dict[str, Any]) -> bool:
    """
    Validate that a calendar event has the required fields.
    
    Args:
        event: Dictionary representing a calendar event
        
    Returns:
        bool: True if event is valid, False otherwise
    """
    required_fields = ['summary', 'start', 'end', 'location', 'description']
    
    if not isinstance(event, dict):
        return False
    
    # Check if all required fields are present
    for field in required_fields:
        if field not in event:
            print(f"❌ Missing required field: {field}")
            return False
    
    # Validate start and end datetime structure
    for time_field in ['start', 'end']:
        time_data = event[time_field]
        if not isinstance(time_data, dict) or 'dateTime' not in time_data:
            print(f"❌ Invalid {time_field} format")
            return False
    
    return True


def format_events_summary(events: List[Dict[str, Any]]) -> str:
    """
    Format a list of events into a readable summary.
    
    Args:
        events: List of calendar event dictionaries
        
    Returns:
        str: Formatted summary of events
    """
    if not events:
        return "No events found."
    
    summary_lines = [f"📅 Found {len(events)} event(s):"]
    
    for i, event in enumerate(events, 1):
        try:
            title = event.get('summary', 'Untitled Event')
            start_time = event.get('start', {}).get('dateTime', 'Unknown time')
            location = event.get('location', 'No location')
            
            summary_lines.append(
                f"{i}. {title} - {start_time} at {location}"
            )
        except Exception as e:
            summary_lines.append(f"{i}. Error formatting event: {e}")
    
    return '\n'.join(summary_lines)
    
