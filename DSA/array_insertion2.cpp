#include <iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    if(n>=0 && n<=50)
    {
        int a[n];
        int e;
        cin>>e;
        for(int i=0; i<n; i++)
        {
            if(i<e)
            {
                cin>>a[i];
            }
            else{
                a[i]=0;
            }
        }
        int x;
        cin>>x;
        int rem;
        if(x>=n)
        {
            rem=x%n;
        }
        else{
            rem=n%x;
        }
        for(int i=n-1; i>=0; i--)
        {
            a[i]=a[i-1];
            if(i==rem-1)
            {
                a[i]=x;
                break;
            }
        }
        for(int i=0; i<n; i++)
        {
            cout<<a[i]<<" ";
        }
    }
    return 0;
}