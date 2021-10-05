t = int(input())

for i in range(t):
    x = int(input())
    a = 0
    while(x>0):
        r = x%10
        if(r == 4):
            a = a+1
        x=x//10

    print(a)
    
