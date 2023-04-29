#include<stdio.h>
#include<math.h>
int main()
{
    float a,b;
    printf("Enter values for a and b:");
    scanf("%f %f",&a,&b);
    printf("Ceil function:%f", ceil(a));
    printf("floor function:%f",floor(b));
    printf("sqrt function:%f",sqrt(a));
    return 0;
}
