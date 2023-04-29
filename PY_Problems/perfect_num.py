a = int(input("Enter the number: "))
sum = 0
for i in range(1,a//2+1):
    if a%i==0:
        sum+=i 
if sum==a:
    print("Yes, {} is a perfect number.".format(a))
else:
    print("No, {} is not a perfect number.".format(a))