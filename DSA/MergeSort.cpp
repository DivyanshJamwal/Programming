#include <iostream>
using namespace std;

void merge(int a[],int p,int mid, int r){
    int n1 = mid-p+1;
    int n2 = r-mid;
    int L[n1], R[n2];
    for(int i = 0;i<n1;i++){
        L[i] = a[i+p];
    }
    for(int i = 0;i<n2;i++){
        R[i] = a[i+mid+1];
    }
    int i = 0;
    int j = 0;
    int k = p;
    while(i<n1 && j< n2){
        if(L[i]<=R[j]){
            a[k]=L[i];
            i++;
        }
        else{
            a[k]=R[j];
            j++;
        }
        k++;
    }
    while(i<n1){
        a[k]=L[i];
        i++;
        k++;
    }
    while(j<n2){
        a[k]=R[j];
        j++;
        k++;
    }
}

void mergeSort(int a[], int p, int r){
    if(p<r){
        int mid = (p+r)/2;
        mergeSort(a,p,mid);
        mergeSort(a,mid+1,r);
        merge(a,p,mid,r);
    }
}

int main()
{
    int a[] = {34,12,56,22,78,11,13,23};
    mergeSort(a,0,7);
    for(int i = 0;i <= 7;i++){
        cout<<a[i]<<" ";
    }
}