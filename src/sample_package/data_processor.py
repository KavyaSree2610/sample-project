"""
A simple data processor class for handling basic data operations.
"""

from typing import List, Dict, Any, Union
import json


class DataProcessor:
    """A class for processing and manipulating data."""
    
    def __init__(self):
        """Initialize the data processor."""
        self.data_store = {}
    
    def store_data(self, key: str, data: Any) -> None:
        """Store data with a given key."""
        self.data_store[key] = data
    
    def get_data(self, key: str) -> Any:
        """Retrieve data by key."""
        return self.data_store.get(key)
    
    def list_keys(self) -> List[str]:
        """Return a list of all stored keys."""
        return list(self.data_store.keys())
    
    def filter_numbers(self, numbers: List[Union[int, float]]) -> Dict[str, List]:
        """Filter a list of numbers into positive, negative, and zero."""
        result = {
            'positive': [],
            'negative': [],
            'zero': []
        }
        
        for num in numbers:
            if num > 0:
                result['positive'].append(num)
            elif num < 0:
                result['negative'].append(num)
            else:
                result['zero'].append(num)
        
        return result
    
    def calculate_statistics(self, numbers: List[Union[int, float]]) -> Dict[str, float]:
        """Calculate basic statistics for a list of numbers."""
        if not numbers:
            return {}
        
        return {
            'count': len(numbers),
            'sum': sum(numbers),
            'mean': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers)
        }
    
    def export_to_json(self, filepath: str) -> None:
        """Export stored data to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.data_store, f, indent=2)
    
    def import_from_json(self, filepath: str) -> None:
        """Import data from a JSON file."""
        with open(filepath, 'r') as f:
            self.data_store = json.load(f)
    
    def clear_data(self) -> None:
        """Clear all stored data."""
        self.data_store.clear()