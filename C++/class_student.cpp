//create a class student with
/*name,regn no., roll nubmber //private
memebr functions - void input,display
working with three students
*/



#include <iostream>
using namespace std;


class student
{
char name[100];
int regno,rollno;
public:
void input()
{
cout << "Enter your Name: ";
cin>>name;
cout<<"\nEnter your registration no: ";
cin >> regno;
cout << "Enter your roll no.: ";
cin >> rollno;
}
void display()
{
cout<<"\n\nYour name is:"<<name<<"\nRegistration no. is: "<<regno<<"\nRoll no. is: "<<rollno;
}
};

int main()
{
student obj1,obj2,obj3;

obj1.input();
obj1.display();

obj2.input();
obj2.display();

obj3.input();
obj3.display();

return 0;
}