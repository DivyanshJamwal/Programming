#include<stdio.h>
int main()
{
    int x,y,z;
    printf("Enter the values for x,y,z:");
    scanf("%d %d %d",&x,&y,&z);
    printf("Values of x,y,z:%d %d %d\n",x,y,z);
    if(x>y)
    {
        if(x>z)
        printf("x=%d\n",x);
        else
        printf("z=%d\n",z);
        }
        else
        {
            if(z>y)
            printf("z=%d\n",z);
            else
            printf("\ny=%d\n",y);
            }
    return 0;
}
