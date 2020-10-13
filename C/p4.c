#include<stdio.h>
#include<math.h>

int main(){
    int m,c,p,e,o;
    printf("Enter the marks obtained in Maths \n");
    scanf("%d", &m);
    printf("Enter the marks obtained in Physics \n");
    scanf("%d", &p);
    printf("Enter the marks obtained in Chemistry \n");
    scanf("%d", &c);
    printf("Enter the marks obtained in English \n");
    scanf("%d", &e);
    printf("Enter the marks obtained in Optional subject(IP,PHE,Painting) \n" );
    scanf("%d", &o);
    printf("Total marks obtained is %d\n", m+c+p+e+o);
    printf("Your percentage is %.1f %\n", (m+c+p+e+o)/5.0);
    printf("Thanks for using this percentage calculator... \n Come back soon... \n ");
    return 0;
}