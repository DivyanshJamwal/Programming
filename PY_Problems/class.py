# class show:
#     print("Hello in Python class")

# ob1 = show()



# class show:
#     x=10
#     def s(self):
#         y = 20
#         print("Local variable",y)
#         print("Instance variable",self.x)


# ob1 = show()
# ob1.s()



# class students:
#     def __init__(self,i,n,r,p):
#         self.RegistrationNo=i
#         self.Name=n
#         self.RollNo=r
#         self.Percentage=p

# student1 = students(1211,'Ajay',1,92)
# student2 = students(1210,'Rahul',2,89)
# student3 = students(1226,'Rohan',3,97)
# student4 = students(1271,'Mohit',4,74)
        
#print(student1.Name)

# class employee:
#     def __int__(self,n,s,a):
#         self.name = n
#         self.salary = s
#         self.age = a
#     def disp(self):
#         print("Name: ",self.name)
#         print("Salary: ",self.salary)
#         print("Age: ",self.age)

# empn = int(input("How many employees: "))
# for i in range(empn):
#     n,s,a = input("Enter Name,Salary,Age").split()

# take 2 classes parent and child.
# Input roll no of a student in parent class and print its complete details in derived class.
# The name of method in parent and child class should be same.

class A:
    def std(self,r):
        self.RollNo = r

class B(A):
    def std(self,i,n,p):
        self.ID = i
        self.Name = n
        self.Percentage = p


