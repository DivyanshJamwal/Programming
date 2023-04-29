#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int n,i,j;
    cout<<"How many elements: ";
    cin>>n;
    int a[n];
    cout<<"Enter array elements: ";
    
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    for(i=0;i<n-1;i++){
        for(j=0;j<n-1-i;j++){
            if(a[j]>a[j+1]){
                swap(a[j],a[j+1]);
            }
        }
    }
    cout<<"Array elements are: ";
    for(i=0;i<n;i++)
        cout<<a[i]<<" ";
}