def solve(n):
    operations = []
    current = n
    for i in range(n - 1, 0, -1):
        operations.append((current, i))
        current = (current + i + 1) // 2
    print(current)
    for op in operations:
        print(op[0], op[1])

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
        print()

if __name__ == "__main__":
    main()

