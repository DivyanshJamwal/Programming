#include<stdio.h>
int main()
{
   int a;
   printf("Enter the number of nodes:");
   scanf("%d", &a);
   switch(a){
     case 0:
      printf("\nNo Geometry");
     break;
     case 1:
      printf("\nA point");
     break;
     case 2:
      printf("\nA line");
     break;
     case 3:
      printf("\nA triangle");
     break;
     case 4:
      printf("\nA rectangle");
     break;
     case 5:
      printf("\nA pentagon");
     break;
    default:
     printf("Invalid input");
     break;
    }
return 0;
}
