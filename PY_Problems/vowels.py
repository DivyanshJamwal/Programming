s = input("Enter the word: ")
vc = 0
vowels = 'aeiouAEIOU'

for a in s:
    if a in vowels:
        vc +=1

print("Number of vowels:", vc)