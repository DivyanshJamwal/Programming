#include<stdio.h>
int i,l;
int search(int ,int *,int);
int main(){
   int n,m;
   printf("Enter the size of array:");
   scanf("%d",&n);
   int a[n];
   printf("Enter the elements:\n");
   for(i=0;i<n;i++){
      scanf("%d",&a[i]);
   }
   printf("Enter the element to be searched:");
   scanf("%d",&m);
   search(n,a,m);
   return 0;
}
int search(int n,int *a,int m){
   for(i=0;i<n;i++){
      if(m==a[i]){
         l=1;
         break;
      }
   }
   if(l==1){
      printf("%d is present",m);
   } else {
      printf("%d is absent",m);
   }
}
