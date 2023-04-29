# create a multilevel inheritance by using class
# create a method in a class which is used to print biodata of one student.
# create a method in b class of hobbies

class A:
    def bio(self):
        print("Biodata")
class B(A):
    def hobbies(self):
        print("Hobbies")
class C(B):
    def marks(self):
        print("Marks")

ob = C()
print(ob.bio())
print(ob.hobbies())
print(ob.marks())

# Write a class name threeD, having attributes x,y,z.
# Define a member function dist to calculate Euclidian distance of two 3D points
# distance = ((x1-x2)**2+(y1-y2)**2)**(1/2)
# distance = (pow(x1-x2,2)+pow(y1-y2,2))**0.5
