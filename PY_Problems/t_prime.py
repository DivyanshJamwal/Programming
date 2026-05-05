import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def t_prime(n):
    if n < 4:
        return False
    root = int(math.sqrt(n))
    return root * root == n and is_prime(root)

n = int(input())
print(t_prime(n))
