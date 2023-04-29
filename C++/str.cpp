#include <iostream>
#pragma pack(1)//It is used to stop bit padding
using namespace std;
struct example 
{
    int a;
    float b;
    double c;
    char d[13];
    void input()
    {
        cout<<"\nEnter value of a:";
        cin>>a;
        cout<<"\nEnter value of b:";
        cin>>b;
    }
    void message()
    {
        cout<<endl<<a<<" "<<b;
    }
};
int main()
{
    example e1;
    cout<<sizeof(e1);
    e1.input();
    cout<<"\nAccessing in main()"<<e1.a<<" "<<e1.b;
    e1.message();
    return 0;
}