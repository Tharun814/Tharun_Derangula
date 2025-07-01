
class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, op):
        if op == "add":
            return self.a + self.b
        elif op == "subtract":
            return self.a - self.b
        elif op == "multiply":
            return self.a * self.b
        elif op == "divide":
            return self.a / self.b if self.b != 0 else "Division by zero error"
        else:
            return "Invalid operation"

# Example
calc = Calculator(10, 5)
print(calc.operate("add"))       # Output: 15.0
print(calc.operate("multiply"))  # Output: 50.0
