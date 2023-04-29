def add(num1,num2): #-- used to define func. with conditions to be used later
    print("The sum of {} and {} is".format(num1,num2),num1 + num2)

def info(Name,Age=29):
    print("{} is {} years old".format(Name,Age))

def even_odd(num):
    if num%2==0:
        print("The number {} is Even".format(num))
    else:
        print("The number {} is Odd".format(num))

def greet(name):
    print("Hello {}.Welcome to the community".format(name)) #-- string formatting

add(12,34)
#info('Rohan',23)

add=lambda num1,num2:num1+num2 #-- short code for single cmd def func.
#print(add(12,13))

#name = input('Please Enter your name: ') #-- Taking input from user.
#greet(name)

lst=[1,2,3,4,5,6,7,8,9,10]
#list1=list(map(even_odd,lst)) #-- map function -> combined result of func.

#list1=print(list(filter(lambda num:num%2==0,lst))) #-- Filter & Time complexity management

#list1=[i*i for i in lst if i%2==0] #-- list compression
#print(list1)

#list1 = iter(lst) #-- iterator
#print(next(list1)) 
