class Error(Exception):
    pass
class dob_ex(Error):
    pass

a = int(input("Enter the current year: "))
b = int(input("Enter the year of birth: "))

age = a-b
try:
    if age<=30 & age>20:
        print("Your age is valid, you can apply for exams")
    else:
        raise dob_ex
except dob_ex:
    print("Your age is not within range")
