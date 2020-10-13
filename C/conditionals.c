#include<stdio.h>

int main(){
    int age;
    printf("Enter your age: \n");
    scanf("%d", &age);
    if(age>=18 && age<30){
        printf("You are eligible for license.\n");
    }
    else if(age==0){
        printf("Nikal, pehli fursat me nikal\n");
    }
    else if(age<=5){
        printf("Pehle apne pajame se to bahar aaja!\n");
    }
    else if(age<=10){
        printf("Bacha hai, bacha banke reh!\n");
    }
    else if(age<18){
        printf("You are not eligible for license.\n");
    }
    else if(age>=30 && age<70){
        printf("You have a license, Aur kitne chahiye\n");
    }
    else if(age>=70 && age<100){
        printf("License banane ke din gaye. Driving chodo Rest kro\n");
    }
    else if(age>=100 && age<120){
        printf("Sir abhi tak zinda ho, takai krke baith jao. \n");
    }
    else if(age>=120 && age<130){
        printf("Respect gayi bhaadh ma, tu pehle bata ki tu zinda bach kaise gaya\n");
    }
    else if(age>130){
        printf("Mazaak chal rha hai kya\n");
    }
    return 0;
}