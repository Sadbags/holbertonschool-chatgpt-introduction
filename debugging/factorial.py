#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if len(sys.argv) != 2:
    print("Usage: python3 script_name.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(factorial(number))
except ValueError:
    print("Invalid input. Please provide a valid integer.")
