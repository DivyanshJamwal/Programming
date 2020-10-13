#include <stdio.h>

int main()
{
    int n,c;
    printf("*****Welcome to the star pattern generator*****\n \n");
    printf("Enter the type (1-upward pointing, 2- downward pointing) \n");
    scanf("%d", &c);
    printf("Enter the number \n");
    scanf("%d", &n);
    switch (c)
    {
    case 1:
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i + 1; j++)
            {
                printf("*");
            }
            printf("\n");
        }
        break;

    case 2:
        for (int i = 0; i < n; i++)
        {
            for (int j = n; j > i ; j--)
            {
                printf("*");
            }
            printf("\n");
        }
        break;
    
    default:
        printf("Invalid type!\n");
        break;
    }
    

    return 0;
}