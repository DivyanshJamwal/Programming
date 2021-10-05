  
t = int(input())

l = 0
s1 = 0
s2 = 0
w = 0

for i in range(t):
    x, y = list(map(int, input().split()))
    s1 += x
    s2 += y
    if s1 >= s2 and s1 - s2 >= l:
        w = 1
        l = s1 - s2
    elif s1 < s2 and s2 - s1 >= l:
        w = 2
        l = s2 - s1
print(w, l)