a = int(input("Enter the 1st side of Triangle: "))
b = int(input("Enter the 2nd side of Triangle: "))
c = int(input("Enter the 3rd side of Triangle: "))

if a==b:
    if b==c:
        print("Triangle is equilateral.")
    else:
        print("Triangle is Isosceles.")
elif b==c or a==c:
    print("Triangle is Isosceles.")
else:
    print("Triangle is scalene.")