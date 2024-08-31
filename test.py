def process_input(value):
    try:
        # Check if the input is a string representation of an integer
        num = int(value)
        
        # Raise ValueError if the number is negative
        if num < 0:
            raise ValueError("Negative value encountered")
        
        # Raise ZeroDivisionError if the number is zero (as an example)
        if num == 0:
            raise ZeroDivisionError("Division by zero error")
        
        # Simulate another condition for raising a custom error
        if num > 100:
            raise OverflowError("Value exceeds maximum limit")
        
        # If no errors, return the processed value (for example, squared)
        return num ** 2

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except OverflowError as oe:
        print(f"OverflowError: {oe}")

# Example usage
inputs = ["50", "-10", "0", "150", "abc"]

for value in inputs:
    print(f"Processing input: {value}")
    result = process_input(value)
    if result is not None:
        print(f"Processed result: {result}")
    print("-" * 30)
