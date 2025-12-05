def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    else:
        if n <= 1: #Factorial of 1 and 0 is 1
            return 1
        return n*factorial(n-1)


n = int(input("Enter a number: "))
print(f"Factorial of {n} is: {factorial(n)}")