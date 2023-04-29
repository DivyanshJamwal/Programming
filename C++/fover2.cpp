//Function overloading with class and object
#include<iostream>
using namespace std;
class overloading
{
public:
int area(int side)
{
        return (side*side);
}
int area(int length,int breadth)
{
        return (length*breadth);
}
float area(float radius)
{
        return (3.14*radius*radius);
}
};
int main()
{
        overloading obj;
        cout<<"\n Area of square is:"<<obj.area(5);
        cout<<"\n Area of rectangle is:"<<obj.area(3,4);
        cout<<"\n Area of circle is:"<<obj.area(3.4f);
        return 0;
}

