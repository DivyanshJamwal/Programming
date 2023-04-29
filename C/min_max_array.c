#include <stdio.h>

int maximum(int a[], int id, int len);
int minimum(int a[], int id, int len);


int main()
{
    int a[100], n, max, min;
    int i;

    printf("Enter size of the array: ");
    scanf("%d", &n);
    printf("Enter %d elements in array: ", n);
    for(i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
    }

    max = maximum(a, 0, n);
    min = minimum(a, 0, n);

    printf("Minimum element in array = %d\n", min);
    printf("Maximum element in array = %d\n", max);

    return 0;
}

int maximum(int a[], int id, int len)
{
    int max;
    if(id >= len-2)
    {
        if(a[id] > a[id + 1])
            return a[id];
        else
            return a[id + 1];
    }

    max = maximum(a, id + 1, len);
    if(a[id] > max)
        return a[id];
    else
        return max;
}

int minimum(int a[], int id, int len)
{
    int min;

    if(id >= len-2)
    {
        if(a[id] < a[id + 1])
            return a[id];
        else
            return a[id + 1];
    }

    min = minimum(a, id + 1, len);

    if(a[id] < min)
        return a[id];
    else
        return min;
}
