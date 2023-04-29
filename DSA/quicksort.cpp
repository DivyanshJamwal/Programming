#include <iostream>
using namespace std;

int partition(int a[], int p, int r){
    int i = p-1;
    int j = p;
    int pivot = a[r];
    for(j = p;j<r;j++){
        if (a[j]<=pivot){
            i++;
            swap(a[j],a[i]);
        }
    }
    i++;
    swap(a[i],a[r]);
    return i;
}

void quicksort(int a[], int p, int r){
    if(p<r){
        int pivotIndex = partition(a,p,r);
        quicksort(a,p,pivotIndex-1);
        quicksort(a,pivotIndex+1,r);
    }
}

int main()
{
    int a[] = {17,21,87,67,45,23,11,25};
    quicksort(a,0,7);
    for(int i = 0; i<=7; i++){
        cout<<a[i]<<" ";
    }
}