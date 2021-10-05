
n,k = map(int,input().split())
a = 0
for i in range(n):
    x = int(input())
    if x%k==0:
        a=a+1
print(f"count = {a}")
