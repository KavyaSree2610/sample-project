"""
Sample Package - A demonstration package for PyPI publishing.

This package provides basic calculator functionality, data processing utilities,
and string manipulation tools.
"""

__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import main classes for easy access
from .calculator import Calculator
from .data_processor import DataProcessor

# Import utility functions
from .utils.helpers import (
    validate_email,
    format_currency,
    truncate_string,
    find_common_elements,
    parse_version,
    is_palindrome
)

from .utils.string_utils import (
    to_snake_case,
    to_camel_case,
    to_title_case,
    remove_punctuation,
    count_words,
    extract_numbers
)

# Define what gets imported with "from sample_package import *"
__all__ = [
    'Calculator',
    'DataProcessor',
    'validate_email',
    'format_currency',
    'truncate_string',
    'find_common_elements',
    'parse_version',
    'is_palindrome',
    'to_snake_case',
    'to_camel_case',
    'to_title_case',
    'remove_punctuation',
    'count_words',
    'extract_numbers'
]