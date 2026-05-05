a = input("Enter the Word: ")

def is_palindrome(a):
    return a == a[::-1]

if is_palindrome(a):
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")
    