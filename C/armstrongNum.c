#include<stdio.h>
#include<math.h>

int main(){
   int a, b, r, n = 0;
   float result = 0;

   printf("Enter an integer: ");
   scanf("%d", &a);

   b = a;

   for(b = a; b != 0; ++n){
       b /= 10;
   }

   for (b = a; b != 0; b /= 10) {
       r = b % 10;

      result += pow(r, n);
   }

   if ((int)result == a)
    printf("%d is an Armstrong number.", a);
   else
    printf("%d is not an Armstrong number.", a);
   return 0;
}
