"""
Test cases for utility functions.
"""

import pytest
from sample_package.utils.helpers import (
    validate_email,
    format_currency,
    truncate_string,
    find_common_elements,
    parse_version,
    is_palindrome
)
from sample_package.utils.string_utils import (
    to_snake_case,
    to_camel_case,
    to_title_case,
    remove_punctuation,
    count_words,
    extract_numbers
)


class TestHelpers:
    
    def test_validate_email(self):
        """Test email validation."""
        assert validate_email("test@example.com") is True
        assert validate_email("user.name+tag@domain.co.uk") is True
        assert validate_email("invalid.email") is False
        assert validate_email("@domain.com") is False
        assert validate_email("user@") is False
    
    def test_format_currency(self):
        """Test currency formatting."""
        assert format_currency(1234.56) == "USD 1,234.56"
        assert format_currency(1000, "EUR") == "EUR 1,000.00"
        assert format_currency(0.99, "GBP") == "GBP 0.99"
    
    def test_truncate_string(self):
        """Test string truncation."""
        text = "This is a long string that needs truncation"
        
        assert truncate_string(text, 20) == "This is a long st..."
        assert truncate_string(text, 50) == text  # No truncation needed
        assert truncate_string(text, 15, ">>>") == "This is a lo>>>"
    
    def test_find_common_elements(self):
        """Test finding common elements."""
        list1 = [1, 2, 3, 4, 5]
        list2 = [3, 4, 5, 6, 7]
        
        common = find_common_elements(list1, list2)
        assert sorted(common) == [3, 4, 5]
        
        # No common elements
        list3 = [1, 2, 3]
        list4 = [4, 5, 6]
        assert find_common_elements(list3, list4) == []
    
    def test_parse_version(self):
        """Test version parsing."""
        assert parse_version("1.2.3") == (1, 2, 3)
        assert parse_version("2.0.0") == (2, 0, 0)
        assert parse_version("1.0") == (1, 0)
        assert parse_version("invalid") is None
        assert parse_version("1.2.a") is None
    
    def test_is_palindrome(self):
        """Test palindrome detection."""
        assert is_palindrome("racecar") is True
        assert is_palindrome("A man a plan a canal Panama") is True
        assert is_palindrome("race a car") is False
        assert is_palindrome("hello") is False
        assert is_palindrome("Madam") is True


class TestStringUtils:
    
    def test_to_snake_case(self):
        """Test snake_case conversion."""
        assert to_snake_case("HelloWorld") == "hello_world"
        assert to_snake_case("hello world") == "hello_world"
        assert to_snake_case("hello-world") == "hello_world"
        assert to_snake_case("already_snake") == "already_snake"
    
    def test_to_camel_case(self):
        """Test camelCase conversion."""
        assert to_camel_case("hello_world") == "helloWorld"
        assert to_camel_case("hello world") == "helloWorld"
        assert to_camel_case("hello-world") == "helloWorld"
        assert to_camel_case("HelloWorld") == "helloworld"
    
    def test_to_title_case(self):
        """Test Title Case conversion."""
        assert to_title_case("hello world") == "Hello World"
        assert to_title_case("python programming") == "Python Programming"
        assert to_title_case("UPPERCASE") == "Uppercase"
    
    def test_remove_punctuation(self):
        """Test punctuation removal."""
        text = "Hello, world! How are you?"
        expected = "Hello world How are you"
        assert remove_punctuation(text) == expected
    
    def test_count_words(self):
        """Test word counting."""
        assert count_words("Hello world") == 2
        assert count_words("This is a test sentence") == 5
        assert count_words("") == 0
        assert count_words("OneWord") == 1
    
    def test_extract_numbers(self):
        """Test number extraction."""
        text = "I have 5 apples and 3.5 oranges, spent $25.99"
        numbers = extract_numbers(text)
        assert numbers == [5.0, 3.5, 25.99]
        
        text = "No numbers here!"
        assert extract_numbers(text) == []