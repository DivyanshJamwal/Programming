#include<stdio.h>
int main()
{
	int a[100],n,i,sum=0;
	printf("\n Enter number of elements:");
	scanf("%d",&n);
	printf("\n Enter array elements:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		sum=sum+a[i];
	}
	printf("\n Sum of array elements is:%d",sum);
	return 0;
}
