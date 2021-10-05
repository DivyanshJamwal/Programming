for i in range(int(input())):
    x = int(input())
    if x==0:
        print(1)
    elif x==1:
        print(2)
    elif x==2:
        print(2)
    elif(x & (x-1)==0):
        print(x)
    else:
        a = 1
        while(2*a < x):
            a *= 2
        if(x==(2*a-1)):
            print(int(2*a-1))
        else:
            print(int(a))