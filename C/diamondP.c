#include <stdio.h>
int main()
{
  int n, a, b;

  printf("Enter number of rows\n");
  scanf("%d", &n);

  for (b = 1; b <= n; b++)
  {
    for (a = 1; a <= n-b; a++)
      printf(" ");

    for (a = 1; a <= 2*b-1; a++)
      printf("*");

    printf("\n");
  }

  for (b = 1; b <= n - 1; b++)
  {
    for (a = 1; a <= b; a++)
      printf(" ");

    for (a = 1 ; a <= 2*(n-b)-1; a++)
      printf("*");

    printf("\n");
  }

  return 0;
}
