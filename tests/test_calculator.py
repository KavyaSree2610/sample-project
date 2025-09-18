"""
Test cases for the Calculator class.
"""

import pytest
from sample_package.calculator import Calculator


class TestCalculator:
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        result = self.calculator.add(5, 3)
        assert result == 8
        
        result = self.calculator.add(-2, 7)
        assert result == 5
        
        result = self.calculator.add(0, 0)
        assert result == 0
    
    def test_subtract(self):
        """Test subtraction operation."""
        result = self.calculator.subtract(10, 3)
        assert result == 7
        
        result = self.calculator.subtract(-5, -2)
        assert result == -3
        
        result = self.calculator.subtract(0, 5)
        assert result == -5
    
    def test_multiply(self):
        """Test multiplication operation."""
        result = self.calculator.multiply(4, 5)
        assert result == 20
        
        result = self.calculator.multiply(-3, 4)
        assert result == -12
        
        result = self.calculator.multiply(0, 100)
        assert result == 0
    
    def test_divide(self):
        """Test division operation."""
        result = self.calculator.divide(15, 3)
        assert result == 5
        
        result = self.calculator.divide(-10, 2)
        assert result == -5
        
        result = self.calculator.divide(7, 2)
        assert result == 3.5
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        result = self.calculator.power(2, 3)
        assert result == 8
        
        result = self.calculator.power(5, 0)
        assert result == 1
        
        result = self.calculator.power(4, 0.5)
        assert result == 2
    
    def test_history(self):
        """Test calculation history functionality."""
        # Initially empty
        assert self.calculator.get_history() == []
        
        # Perform some operations
        self.calculator.add(5, 3)
        self.calculator.multiply(2, 4)
        
        history = self.calculator.get_history()
        assert len(history) == 2
        assert "5 + 3 = 8" in history
        assert "2 * 4 = 8" in history
        
        # Clear history
        self.calculator.clear_history()
        assert self.calculator.get_history() == []