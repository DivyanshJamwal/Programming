#include <iostream>
using namespace std;
class example;
class A
{
public:
void taskA(example);
};
class B
{
public:
int taskB(example);
};
class example
{
int p,q;
public:
void input()
{
cout<<"\nEnter P and Q: ";
cin>>p>>q;
}
friend void A::taskA(example);
friend int B::taskB(example);
};
void A::taskA(example obj)
{
int max = obj.p;
if (obj.q > max)
{
max = obj.q;
}
cout <<endl<<max<<" is greater!"<<endl;
}
int B::taskB(example obj)
{
return obj.p+obj.q;
}

int main()
{
A A1;
B B1;
example C1;
C1.input();
A1.taskA(C1);
cout << B1.taskB(C1);
return 0;
}

