def solve():
    n, m = map(int, input().split())
    s = input().strip()
    p = list(map(int, input().split()))

    freq = [0] * 26

    prefix = [0] * (n + 1)

    for pos in p:
        prefix[0] += 1
        if pos < n:
            prefix[pos] -= 1

    for i in range(1, n):
        prefix[i] += prefix[i - 1]

    for i in range(n):
        freq[ord(s[i]) - ord('a')] += prefix[i]

    for char in s:
        freq[ord(char) - ord('a')] += 1

    print(' '.join(map(str, freq)))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()