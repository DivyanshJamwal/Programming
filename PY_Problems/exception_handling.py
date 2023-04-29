try:
    #a = b #NameError condition
    a=12
    b='s'
    c=3
    #d=a+b #TypeError condition
    #print(d)
    #print(a/0) #error handling by exception
except NameError:
    print('Variable not defined')
except TypeError:
    print('Use similar types')
except Exception as ex:
    print(ex)

else:
    print(a+c)
finally:
    print('The code is successfully executed')
