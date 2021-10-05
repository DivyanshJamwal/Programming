for i in range(int(input())):
    a,b,c = map(int, input().split())
    if a > b:
        if a < c:
            print(a)
        elif a > c:
            if b > c:
                print(b)
            else:
                print(c)
    elif a > c:
        print(a)
    elif b > c:
        print(c)
    else:
        print(b)