#include <iostream>
using namespace std;
class XYZ;
class PQR;
class ABC
{
int x,y;
public:
void input()
{
cout<<"\nEnter The Values: ";
cin>>x>>y;
}
friend class XYZ;
friend class PQR;
};
class XYZ
{
public:
void taskXYZ(ABC obj)
{
if (obj.x % 2 == 0)
{
cout << "\nEven";
}
else
{
cout << "\nOdd";
}
}
};
class PQR
{
public:
void taskPQR(ABC obj)
{
if (obj.y % 5 == 0)
{
cout << "\ny is a multiple of 5";
}
else
{
cout << "\ny is not a Multiple of 5";
}
}

};
int main()
{
ABC obj1;
obj1.input();
XYZ obj2;
PQR obj3;
obj2.taskXYZ(obj1);
obj3.taskPQR(obj1);
return 0;
}