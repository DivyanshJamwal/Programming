for i in range(int(input())):
    x,y,z = map(int, input().split())
    r = (z*2)+x
    if r>=y:
        a = 'YES'
    else:
        a = 'NO'
    print(a)