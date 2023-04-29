#include <iostream>
using namespace std;
int reverse(int);//Function declaration
int main()
{
    int a;
    cout<<"\nEnter number:";
    cin>>a;
    cout<<"\nReverse is:"<<reverse(a);//Actual argument
    return 0;
}
//Function definition
int reverse(int x)//Function header(Formal argument)
{
    //Function body
    int rev=0,rem;
    while(x!=0)
    {
        rem=x%10;
        rev=rev*10+rem;
        x=x/10;
    }
    return rev;
}