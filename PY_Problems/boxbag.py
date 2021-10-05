while True:
    try:
        t = int(input())
        if(1<=t<=100):
            break;
    except ValueError:
        continue

for i in range(t):
    
        
            
    while True:
        try:
            a,b,c,d = map(int, input().split())
            if(1<=a<=b<=c<=d<=100):
                break;
        except ValueError:
            continue
    

    r = a+b+c
    ans = d//r
    if(r<=d):
        print(int(ans))
    elif(r>d):
        if(r%d==0):
            if(a+b<=d):
                print(int('2'))
            elif(a+b>d):
                print(int('3'))
        else:
            print(int(r/d)+1)
