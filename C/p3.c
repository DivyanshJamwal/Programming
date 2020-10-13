#include <stdio.h>

int main()
{
    int p, r, t;
    printf("Enter Principal amount \n");
    scanf("%d", &p);
    printf("Enter Time \n");
    scanf("%d", &t);
    printf("Enter Rate \n");
    scanf("%d", &r);
    printf("Your Simple Interest is %d \n", p * t * r / 100);
    printf("Thanks for using... \n");
    return 0;
}