t = int(input("How many numbers: "))
sum = 0
for i in range(t):
    x = map(int, input().split())
    for item in range(x):
        sum += item
        print(sum)