#include<stdio.h>

int main(){
    int l, b, r, s;

    printf("Enter the radius of circle \n");
    scanf("%d" , &r);

    printf("The area of this circle is %d \n", 3.14*r*r);

    printf("Enter the side of square \n");
    scanf("%d" , &s);

    printf("The area of this square is %d \n", s*s);

    printf("Enter the length of rectangle \n");
    scanf("%d" , &l);

    printf("Enter the breadth of rectangle \n");
    scanf("%d" , &b);

    printf("The area of this rectangle is %d \n", l*b);
    return 0;
}
