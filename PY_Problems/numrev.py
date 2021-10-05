t = int(input())

for i in range(t):
    x = input()
    a = ''
    for item in x:
        a = item+a
    print(int(a))
    