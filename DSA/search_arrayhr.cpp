#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    int a[20],i,j,n,temp;
     cin>>n;
     if(n>0&&n<3)
     {
     cout<<"Not sufficient elements";
     }
     else if(n>=3 && n<=20)
     {
     for(int i=0;i<n;i++)
     {
     cin>>a[i];
     }


     for(int i=0;i<n-1;i++)
     { for( j=i+1;j<n;j++)

     {
     if(a[i]>a[j])
     {
     temp=a[i];
     a[i]=a[j];
     a[j]=temp;
     }
     }



     }
     cout<<a[i+2];
     }
     else
     {
     cout<<"Invalid array size";
     }
    return 0;
}
