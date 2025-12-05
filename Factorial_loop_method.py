n = int(input("Enter the number to calculate factorial:"))
def factorial(n):
    # fact = 1
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact
print(f"Factorial of the number n is:{factorial(n)}")
