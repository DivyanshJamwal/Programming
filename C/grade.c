#include <stdio.h>
int main()
{
    int counter, grade, total;
    float average;
    total = 0;
    counter = 0;
    printf("%s", "Enter grade, -1 to end:");
    scanf("%d", &grade);
    while ( grade != -1 )
    {
        total = total + grade;
        counter = counter + 1;
        printf( "%s", "Enter grade, -1 to end: " );
        scanf("%d", &grade);
    }
    if (counter != 0)
    {
        average = (float) total/counter;  //type conversion
        printf("Class average is %.2f\n", average);
    }
    else
    {
        puts("No grades were entered");
    }
}
