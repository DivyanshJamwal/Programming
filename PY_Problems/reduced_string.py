def super_reduced_string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    reduced_string = ''.join(stack)
    return reduced_string if reduced_string else "Empty String"

if __name__ == "__main__":
    s = input().strip()
    result = super_reduced_string(s)
    print(result)