#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int n,i,j,mini;
    cout<<"How many elements: ";
    cin>>n;
    int a[n];
    int min=a[0];
    cout<<"Enter array elements: ";
    
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    for(j=0;j<n-1;j++){
        min =a[j];
        for(i=j;i<n;i++){
            if(a[i]<min){
                min = a[i];
                mini = i;
            }
        }
        swap(a[j],a[mini]);
    }
    

    cout<<"Array elements are: ";
    for(i=0;i<n;i++)
        cout<<a[i]<<" ";
}