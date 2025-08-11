#simple calculator
def add(a,b):
  return a + b
def substract(a, b):
  return a - b
def multiply(a,b):
  return a *  b
def divide(a , b):
  if b != 0:
    return a /b
 else :
      return "Error:Division by zero!"
   # Example usage
print("Addition:",add(5,3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("division:", divide(5, 3))
