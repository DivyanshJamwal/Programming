import math

def extra_long_factorials(n):
    # Calculate factorial using math.factorial
    result = math.factorial(n)
    # Print the result
    print(result)

if __name__ == "__main__":
    n = int(input().strip())
    extra_long_factorials(n)