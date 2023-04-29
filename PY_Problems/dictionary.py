# create a dict. min 3 items you can take keys as roll no and values as names
# update it and enter three more items using input functions,
# do testing to remove duplicacy
# apply setitems method on it, apply pop item and pop on dictionary

#a = {'01':"Aditya",'02':"Ajay",'03':"Aman"}

d = {}
t = int(input("Enter the number of items: "))
if t>=3:
    print("Enter name and roll no.")
    for i in range(t):
        x,y = input().split()
        d[x] = y
    print(d)
else:
    print("Enter atleast 3 items")


#d.__setitem__() #-- args key,value
#d.popitem() #-- delete last item
#d.pop() #-- args key



