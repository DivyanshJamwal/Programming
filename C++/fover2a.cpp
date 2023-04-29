//Function overloading with class and object
#include<iostream>
using namespace std;
class overloading
{
public:
int volume(int side)
{
        return (side*side*side);
}
int volume(int length,int width,int height)
{
        return (length*width*height);
}
float volume(float radius,float height)
{
        return (3.14*radius*radius*height);
}
};
int main()
{
        overloading obj;
        cout<<"\n Volume of cube is:"<<obj.volume(5);
        cout<<"\n Volume of cuboid is:"<<obj.volume(3,4,2);
        cout<<"\n Volume of cylinder is:"<<obj.volume(12.3f,4.3f);
        return 0;
}

