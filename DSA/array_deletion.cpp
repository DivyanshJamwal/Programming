//removal of one odd element from three consecutive odd elements
#include <iostream>
using namespace std;

int main() 
{
    int n,s=0;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
    for(int k=0;k<n;k++)
    {
        for(int i=0;i<n-2-s;i++)
        {
            if(a[i]%2!=0)
            {
                if(a[i+1]%2!=0)
                {
                    if(a[i+2]%2!=0)
                    {
                        s++;
                        for(int j=i;j<n-1;j++)
                        {
                            a[j]=a[j+1];
                        }
                    }
                }
            }
        }
    }
    for(int i=0;i<n-s;i++)
    {
        cout<<a[i]<<" ";
    }
    return 0;
}