print("Welcome to the basic calculator!")
print("Available operators are (+, -, /, *, %, <, >, =, avg(@), pow(^)) ! ")
a = int(input("Enter your number : "))
op = input("Enter the arithmatic operator : ")
b = int(input("Enter the secondary number : "))


if(op == "+"):
    print(f"The sum of {a} + {b} is {a+b}")
elif(op == "-"):
    print(f"The difference of {a} - {b} is {a-b}")
elif(op == "*"):
    print(f"The product of {a} * {b} is {a*b}")
elif(op == "/"):
    print(f"The result of {a} / {b} is {a/b}")
elif(op == "%"):
    print(f"The remainder of {a} % {b} is {a%b}")
elif(op == ">"):
    if (a > b):
        print(f"True! {a} is greater than {b}")
    else:
        print(f"False! {a} is lesser than {b}")
elif(op == "<"):
    if (a < b):
        print(f"True! {a} is lesser than {b}")
    else:
        print(f"False! {a} is greater than {b}")
elif(op == "="):
    if (a == b):
        print(f"True! {a} is equals to {b}")
    else:
        print(f"False! {a} is not equals to {b}")
elif(op == "@"):
    print(f"The average of {a} & {b} is {(a+b)/2}")
elif(op == "^"):
    print(f"The result of {a} ^ {b} is {a**b}")

else:
    print("Recheck the operator entered!")

print("Thanks for using this calculator!")


