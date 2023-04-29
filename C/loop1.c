#include<stdio.h>
int main()
{
    int no,sum=0,n;
    printf("enter the no");
    scanf("%d",&no);
    while(no!=0)
    {
        n=no%10;
        sum=sum+n;
        no=no/10;
    }
    printf("the sum of digits=%d",sum);
}

