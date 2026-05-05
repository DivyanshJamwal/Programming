def pylons(k, arr):
    n = len(arr)
    count = 0
    i = 0
    last_plant = -1

    while i < n:
        # Find the rightmost plant that can cover position i
        loc = min(i + k - 1, n - 1)
        while loc >= i - k + 1 and loc >= 0 and arr[loc] == 0:
            loc -= 1
        if loc < i - k + 1 or loc < 0:
            return -1
        count += 1
        i = loc + k
    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(pylons(k, arr))