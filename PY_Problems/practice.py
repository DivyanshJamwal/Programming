#reverse a number
'''a = input()
x = ''
for i in a:
    x = i + x
print(x)'''

#balanced string check

def bal(s1,s2):
    return set(s1)==set(s2)
a = input()
b = input()

print(bal(a,b))



#indices
'''def find(str , ch):
        for ltr in str:
            if ltr == ch:
                  return [i for i, ltr in enumerate(str) if ltr == ch]
            
a = input()
b = input()

print(find(a,b))'''

#separation
'''a = input()
l = []
for i in a:
    l.append(i)
s = ","
s = s.join(l)
print(s + ",")'''
