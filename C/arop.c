#include<stdio.h>

int add(int n1, int n2);
int sub(int n1, int n2);
int mul(int n1, int n2);
int div(int n1, int n2);

int main()
{
  int a, b;

  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);

  printf("%d + %d = %d\n", a, b, add(a, b));
  printf("%d - %d = %d\n", a, b, sub(a, b));
  printf("%d * %d = %d\n", a, b, mul(a, b));
  printf("%d / %d = %d\n", a, b, div(a, b));

  return 0;
}


int add(int n1, int n2)
{
  int result;
  result = n1 + n2;
  return result;
}


int sub(int n1, int n2)
{
  int result;
  result = n1 - n2;
  return result;
}


int mul(int n1, int n2)
{
  int result;
  result = n1 * n2;
  return result;
}


int div(int n1, int n2)
{
  int result;
  result = n1 / n2;
  return result;
}
