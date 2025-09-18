"""
Utility functions for the sample package.
"""

import re
from typing import List, Optional


def validate_email(email: str) -> bool:
    """
    Validate if an email address is in a valid format.
    
    Args:
        email: The email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def format_currency(amount: float, currency: str = "USD") -> str:
    """
    Format a number as currency.
    
    Args:
        amount: The amount to format
        currency: The currency code (default: USD)
        
    Returns:
        Formatted currency string
    """
    return f"{currency} {amount:,.2f}"


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length.
    
    Args:
        text: The text to truncate
        max_length: Maximum length of the result
        suffix: Suffix to add when truncating (default: "...")
        
    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def find_common_elements(list1: List, list2: List) -> List:
    """
    Find common elements between two lists.
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        List of common elements
    """
    return list(set(list1) & set(list2))


def parse_version(version_string: str) -> Optional[tuple]:
    """
    Parse a version string into a tuple of integers.
    
    Args:
        version_string: Version string like "1.2.3"
        
    Returns:
        Tuple of integers or None if invalid
    """
    try:
        parts = version_string.split('.')
        return tuple(int(part) for part in parts)
    except ValueError:
        return None


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome (ignoring case and spaces).
    
    Args:
        text: Text to check
        
    Returns:
        True if palindrome, False otherwise
    """
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]