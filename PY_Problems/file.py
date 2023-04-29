# f = open("C:\\Users\\Devil\\Documents\\New.txt","w")
# f.write("Hello")
# f.close()


# f = open("C:\\Users\\Devil\\Documents\\New.txt","r")
# print(f.read())


# f = open("C:\\Users\\Devil\\Documents\\New.txt","a")
# f.write("World")
# f.close()


# f = open("C:\\Users\\Devil\\Documents\\New.txt","r")
# print(f.read())


# with open("C:\\Users\\Devil\\Documents\\New.txt") as old:
#     with open("C:\\Users\\Devil\\Documents\\Pyt.txt","w") as new:
#         for x in old:
#             new.write(x)
# print("File New.txt copied to Pyt.txt")


# f = open("C:\\Users\\Devil\\Documents\\Pyt.txt")
# print(f.read())

# a = 500
# f = open("C:\\Users\\Devil\\Documents\\New.txt","w")
# f.write(str(a))
# f.close()
# f = open("C:\\Users\\Devil\\Documents\\New.txt")
# print(f.read())

# x = 99
# l = [1,2,3]
# f = open("C:\\Users\\Devil\\Documents\\MR.txt","w")
# f.write(str(x))
# f.write(str(57.6))
# f.write(str(l))
# f.close()
# f = open("C:\\Users\\Devil\\Documents\\MR.txt")
# print(f.read())

import random
randNo = random.randint(1,500)
print(randNo)