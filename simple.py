# simple.py
# A simple Python program

def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers and return the result"""
    return a + b

def main():
    # Greet the user
    print(greet("World"))
    
    # Perform simple addition
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    # Simple loop example
    print("\nCounting to 5:")
    for i in range(1, 6):
        print(f"Number: {i}")

if __name__ == "__main__":
    main()
