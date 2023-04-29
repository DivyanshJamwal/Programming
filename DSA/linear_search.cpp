#include <iostream>
using namespace std;

int main()
{
    int arr[10];
    int count=0,flag=0,x;
    for(int i=0;i<10;i++)
    {
        cin>>arr[i];
    }
    cin>>x;
    for(int i=0;i<10;i++)
    {
        if(x==arr[i])
        {
            flag=1;
            count++;
            break;
        }
        else
            count++;
    }
    if(flag==1)
        cout<<count;
    else
        cout<<"ELEMENT NOT FOUND";
}