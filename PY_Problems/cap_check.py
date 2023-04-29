a = input("Enter a character")
if a.isupper():
    print("The character {} is upper".format(a))
elif a.islower():
    print("The character {} is lower".format(a))
else:
    print("{} is not a character".format(a))