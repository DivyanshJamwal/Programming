package Coding_Practice.JAVA;

import java.util.Scanner;

public class prac {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.println("Enter your number");
        int number = input.nextInt();
        System.out.println(input);

        switch(number){
            case 1:
                System.out.println("The day is Monday");
                break;
            case 2:
                System.out.println("The day is Tuesday");
                break;
            case 3:
                System.out.println("The day is Wednesday");
                break;
            case 4:
                System.out.println("The day is Thursday");
                break;
            case 5:
                System.out.println("The day is Friday");
                break;
            case 6:
                System.out.println("The day is Saturday");
                break;
            case 7:
                System.out.println("The day is Sunday");
                break;
            default:
                System.out.println("You have entered an invalid number");
        


        }
    }
    
}