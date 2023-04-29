#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int m,n,i,temp;
    cout<<"How many elements: ";
    cin>>n;
    int a[n];
    cout<<"Enter array elements: ";
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    cout<<"How many elements in A2: ";
    cin>>m;
    int b[m];
    cout<<"Enter array elements: ";
    for(i=0;i<m;i++){
        cin>>b[i];
    }
    cout<<"Merged array is: ";
    for(i=0;i<(m+n);i++){
        if(i<m){
            temp[i]=a[i];
        }
        else{
            temp[i]=b[i-m];
        }
        cout<<temp[i]<<" ";
    }
}