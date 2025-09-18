"""
Command-line interface for the sample package.
"""

import argparse
import sys
from .calculator import Calculator
from .data_processor import DataProcessor


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Sample Package CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Calculator commands
    calc_parser = subparsers.add_parser('calc', help='Calculator operations')
    calc_parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'])
    calc_parser.add_argument('a', type=float, help='First number')
    calc_parser.add_argument('b', type=float, help='Second number')
    
    # Data processor commands
    data_parser = subparsers.add_parser('data', help='Data processing operations')
    data_parser.add_argument('--numbers', nargs='+', type=float, help='List of numbers to process')
    data_parser.add_argument('--stats', action='store_true', help='Calculate statistics')
    data_parser.add_argument('--filter', action='store_true', help='Filter numbers')
    
    args = parser.parse_args()
    
    if args.command == 'calc':
        calculator = Calculator()
        
        if args.operation == 'add':
            result = calculator.add(args.a, args.b)
        elif args.operation == 'subtract':
            result = calculator.subtract(args.a, args.b)
        elif args.operation == 'multiply':
            result = calculator.multiply(args.a, args.b)
        elif args.operation == 'divide':
            try:
                result = calculator.divide(args.a, args.b)
            except ValueError as e:
                print(f"Error: {e}")
                sys.exit(1)
        
        print(f"Result: {result}")
    
    elif args.command == 'data':
        if not args.numbers:
            print("Error: Please provide numbers using --numbers")
            sys.exit(1)
        
        processor = DataProcessor()
        
        if args.stats:
            stats = processor.calculate_statistics(args.numbers)
            print("Statistics:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
        
        if args.filter:
            filtered = processor.filter_numbers(args.numbers)
            print("Filtered numbers:")
            for category, numbers in filtered.items():
                print(f"  {category}: {numbers}")
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()