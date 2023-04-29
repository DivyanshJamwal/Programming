#include<iostream>
using namespace std;
class test
{
int reg;
static int count;
public:
void setcode()
{
reg= ++count;
}
void showcode()
{
cout<<"Code: "<<reg<<endl;
}
static void showcount()
{
cout<<"Count: "<<count<<endl;
}
};
int test :: count=2000;
int main()
{
test t[5];
for (int i=0; i<5; i++)
{
t[i].setcode();
}
test :: showcount();

for (int i=0; i<5; i++)
{
t[i].showcode();
}
return 0;
}