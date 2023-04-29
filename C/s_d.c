#include<stdio.h>
int main()
{
    int d,t;
    float s;
    printf("Enter the value for distance");
    scanf("%d",&d);
    printf("Enter the value for time");
    scanf("%d",&t);
    s=d/t;
    printf("The speed of car:%f",s);
    return 0;
}
