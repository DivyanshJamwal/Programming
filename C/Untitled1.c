#include<stdio.h>
#include<math.h>
int main()
{
    int days,years,weeks,a=365,b=7;
    printf("Enter the number of Days: ");
    scanf("%d",&days);
    years = days/a;
    weeks = days/b;
    printf("Days : %d\n",days);
    printf("Weeks : %d\n",weeks);
    printf("Years : %d\n",years);
}
