# Sample Package

A demonstration Python package for testing PyPI publishing workflows.

## Overview

This package provides a collection of utilities including:

- **Calculator**: Basic arithmetic operations with history tracking
- **Data Processor**: Data manipulation and statistics calculation
- **String Utils**: Text processing and manipulation utilities
- **Helper Functions**: Common utility functions for validation and formatting

## Installation

```bash
pip install sample-package-kkaitepalli
```

## Quick Start

### Using the Calculator

```python
from sample_package import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # 8

# View calculation history
print(calc.get_history())
```

### Processing Data

```python
from sample_package import DataProcessor

processor = DataProcessor()
numbers = [1, -2, 3, -4, 5, 0]

# Get statistics
stats = processor.calculate_statistics(numbers)
print(stats)

# Filter numbers
filtered = processor.filter_numbers(numbers)
print(filtered)
```

### String Utilities

```python
from sample_package import to_snake_case, validate_email

# Convert to snake_case
result = to_snake_case("Hello World")
print(result)  # "hello_world"

# Validate email
is_valid = validate_email("test@example.com")
print(is_valid)  # True
```

### Command Line Interface

The package also provides a CLI tool:

```bash
# Calculator operations
sample-cli calc add 5 3

# Data processing
sample-cli data --numbers 1 2 3 4 5 --stats --filter
```

## API Reference

### Calculator Class

- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract b from a
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide a by b
- `power(base, exponent)`: Raise base to power of exponent
- `get_history()`: Get calculation history
- `clear_history()`: Clear calculation history

### DataProcessor Class

- `store_data(key, data)`: Store data with a key
- `get_data(key)`: Retrieve data by key
- `filter_numbers(numbers)`: Filter numbers into positive, negative, zero
- `calculate_statistics(numbers)`: Calculate basic statistics
- `export_to_json(filepath)`: Export data to JSON file
- `import_from_json(filepath)`: Import data from JSON file

### Utility Functions

#### helpers module
- `validate_email(email)`: Validate email format
- `format_currency(amount, currency)`: Format number as currency
- `truncate_string(text, max_length)`: Truncate string to max length
- `find_common_elements(list1, list2)`: Find common elements
- `parse_version(version_string)`: Parse version string to tuple
- `is_palindrome(text)`: Check if text is palindrome

#### string_utils module
- `to_snake_case(text)`: Convert to snake_case
- `to_camel_case(text)`: Convert to camelCase
- `to_title_case(text)`: Convert to Title Case
- `remove_punctuation(text)`: Remove punctuation
- `count_words(text)`: Count words in text
- `extract_numbers(text)`: Extract numbers from text

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/yourusername/sample-package.git
cd sample-package

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/

# Lint code
flake8 src/
```

### Building and Publishing

```bash
# Build the package
python -m build

# Upload to PyPI (test)
python -m twine upload --repository testpypi dist/*

# Upload to PyPI (production)
python -m twine upload dist/*
```

## Requirements

- Python >= 3.8
- requests >= 2.25.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for your changes
5. Run the test suite
6. Submit a pull request

## Changelog

### Version 0.1.0
- Initial release
- Basic calculator functionality
- Data processing utilities
- String manipulation tools
- Command-line interface