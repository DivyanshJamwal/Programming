#include <iostream>
using namespace std;


int main() {
    int n,i,j;
    int max=0;
    int index=-1;
    cin>>n;
    int a[n+1];
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    cin>>j;
    for(i=0;i<n;i++){
        if(a[i]>max){
            max = a[i];
            index = i;
        }
    }
    for(i=n-1;i>=index;i--){
        a[i+1]=a[i];
    }
    a[index+1]=j;
    for(i=0;i<n+1;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}
