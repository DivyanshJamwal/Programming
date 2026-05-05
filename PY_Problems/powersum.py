def power_sum(X, N, num=1):
    # Calculate the power of the current number
    power = num ** N
    
    # Base case: if power equals X, we found a valid combination
    if power == X:
        return 1
    # If power exceeds X, no valid combination is possible
    elif power > X:
        return 0
    
    # Recursive case: include the current number or skip it
    return power_sum(X - power, N, num + 1) + power_sum(X, N, num + 1)

if __name__ == "__main__":
    X = int(input("Enter the value of X: "))
    N = int(input("Enter the value of N: "))
    print(power_sum(X, N))