#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int n,i,j,temp;
    cout<<"How many elements: ";
    cin>>n;
    int a[n];
    cout<<"Enter array elements: ";
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    for(j=1;j<n;j++){
        temp=a[j];
        i=j-1;
        while(a[i]>temp && i>=0){
            a[i+1]=a[i];
            i--;
        }
    }
    cout<<" "<<a[i];
    a[i+1]=temp;
    
}