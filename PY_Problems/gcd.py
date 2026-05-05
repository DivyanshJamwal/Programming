a = int(input())
b = int(input())

if a < b:
    c = a
else:
    c = b

gcd = 1
i = 1

while(i <= c):
    if(a % i == 0 and b % i == 0):
        gcd = i

    i = i + 1

print(gcd)