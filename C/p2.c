#include<stdio.h>

int main() {
    float pi = 3.14;
    int r, h;
    printf("Enter the radius of circle \n");
    scanf("%d", &r);
    printf("Enter the height \n");
    scanf("%d", &h);
    printf("The area of this circle is %f \n", pi*r*r);
    printf("The area of this cylinder is %f \n", pi*r*r*h);

    return 0;
}