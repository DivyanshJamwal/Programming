#include <iostream>
using namespace std;
class rectangle
{
    int length,breadth;
    public:
    void input()
    {
        cout<<"\nEnter values of length and breadth:";
        cin>>length>>breadth;
    }
    void output()
    {
        cout<<"\nArea of rectangle is:"<<length*breadth;
    }
};
int main()
{
    rectangle obj1,obj2,obj3;
    obj1.input();
    obj1.output();
    obj2.input();
    obj2.output();
    obj3.input();
    obj3.output();
    return 0;
}
