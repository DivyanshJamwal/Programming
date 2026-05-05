a = int(input("Enter the number: "))
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

date = months[a-1]
print(date)

if date == 0 or 2 or 4 or 6 or 7 or 9 or 11 :
    print("No of days are 31")

elif date==1:
    print("No of days are 28")

else:
    print("No of days are 30")