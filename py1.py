def add(a: int, b: int):
    return a + b

def multiply(a: int, b: int):
    return a * b    

def divide(a: int, b: int):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def subtract(a: int, b: int):
    return a - b

def power(a: int, b: int):
    return a ** b


print("This is a simple calculator module.")
print("Available functions: add, multiply, divide, subtract, power")
print("You can import this module and use these functions.")


# Example usage
if __name__ == "__main__":
    print("Sum of 5 and 3:", add(5, 3))
    print("Multiply 5 and 3:", multiply(5, 3))
    print("Divide 5 by 0:", divide(5, 0))
    print("Subtract 3 from 5:", subtract(5, 3))
    print("5 to the power of 3:", power(5, 3))
