#include<stdio.h>
#include <stdlib.h>
int main()
{
    int *ptr, i, n, x;
    printf("Enter the size of array\n");
    scanf("%d", &n);
    ptr = (int *)calloc(n, sizeof(int));
    printf("Enter array elements:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&ptr[i]);
	}
	printf("Enter the modified size\n");
    scanf("%d", &x);
    ptr = (int *)realloc(ptr, x*sizeof(int));
    printf("size modified\n");
    printf("Enter array elements:");
    for(i=n;i<x;i++)
	{
		scanf("%d",&ptr[i]);
	}

    int count_odd =0, count_even = 0;
    for(int i = 0; i < x; i++)
    {
        if(ptr[i] % 2 == 1)
        count_odd++;
        else
        count_even++;
    }
    printf("Odd: %d",count_odd);
    printf("\nEven: %d",count_even);
    return 0;
}
