"""
String manipulation utilities.
"""

import string
from typing import List


def to_snake_case(text: str) -> str:
    """
    Convert text to snake_case.
    
    Args:
        text: Text to convert
        
    Returns:
        Text in snake_case format
    """
    import re
    
    # Insert underscore before uppercase letters (except at start)
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text)
    
    # Replace spaces and hyphens with underscores, then clean up multiple underscores
    text = text.replace(' ', '_').replace('-', '_')
    text = re.sub(r'_+', '_', text)  # Replace multiple underscores with single
    
    return text.lower()


def to_camel_case(text: str) -> str:
    """
    Convert text to camelCase.
    
    Args:
        text: Text to convert
        
    Returns:
        Text in camelCase format
    """
    words = text.replace('_', ' ').replace('-', ' ').split()
    if not words:
        return text
    
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def to_title_case(text: str) -> str:
    """
    Convert text to Title Case.
    
    Args:
        text: Text to convert
        
    Returns:
        Text in Title Case format
    """
    return ' '.join(word.capitalize() for word in text.split())


def remove_punctuation(text: str) -> str:
    """
    Remove all punctuation from text.
    
    Args:
        text: Text to clean
        
    Returns:
        Text without punctuation
    """
    return text.translate(str.maketrans('', '', string.punctuation))


def count_words(text: str) -> int:
    """
    Count the number of words in text.
    
    Args:
        text: Text to count words in
        
    Returns:
        Number of words
    """
    return len(text.split())


def extract_numbers(text: str) -> List[float]:
    """
    Extract all numbers from a text string.
    
    Args:
        text: Text to extract numbers from
        
    Returns:
        List of numbers found in the text
    """
    import re
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches if match]