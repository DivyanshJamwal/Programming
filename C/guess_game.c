#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int n, g, ng = 1;
    srand(time(0));
    n = rand() % 100 + 1;
    do
    {
        printf("Guess the number between 1-100\n");
        scanf("%d", &g);
        if (g > n)
        {
            printf("Your guess is high! \n");
        }
        else if (g < n)
        {
            printf("Your guess is low! \n");
        }
        else
        {
            printf("Your guessed it correct in %d attempts! \n", ng);
        }
        ng++;

    } while (g != n);
    printf("Thanks for playing this game");
    return 0;
}