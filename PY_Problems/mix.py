for i in range(int(input())):
    x,y = map(int, input().split())
    if x > 0:
        if y > 0:
            print("Solution")
        else:
            print("Solid")
    else:
        if y > 0:
            print("Liquid")
    