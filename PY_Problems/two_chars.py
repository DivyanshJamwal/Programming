def is_valid(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            filtered = [c for c in s if c == unique_chars[i] or c == unique_chars[j]]
            if is_valid(filtered):
                max_length = max(max_length, len(filtered))

    return max_length

if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = alternate(s)
    print(result)