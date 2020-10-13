#include<stdio.h>

int main(){
    int c,f;
    printf("Enter the temperature in celsius \n");
    scanf("%d", &c);
    f=9/5*c+32;
    printf("The given temperature in fahrenheit is %d\n",f);
    return 0;
}