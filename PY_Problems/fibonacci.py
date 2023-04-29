a = 0
b = 1
n = int(input("Enter the length of series: "))
if n==1:
    print(a)
else:
    print(a)
    print(b)
for i in range(n-2):
    fib = a+b
    print(fib)
    a,b = b,fib