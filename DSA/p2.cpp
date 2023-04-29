#include<iostream>
using namespace std;

int main() {
    int n,i,k,item;
    cout<<"Enter the number of elements of array: ";
    cin>>n;
    int a[n+1];
    cout<<"Enter "<<n<<"elements: ";
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    cout<<"Enter 1 more element";
    cin>>item;
    cout<<"Enter the position";
    cin>>k;
    for (i=n;i>=k;i--)
    {
        a[n]=a[n+1]
    }

}
