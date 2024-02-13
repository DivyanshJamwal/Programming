package Coding_Practice.JAVA;

import java.util.Scanner;

public class AddTwoNumbers {

    public static void main(String[] args) {
       
        try (Scanner s = new Scanner(System.in)) {
            System.out.println("Enter 1st number: ");
            int num1 = s.nextInt();

            System.out.println("Enter 2nd number: ");
            int num2 = s.nextInt();
            
            int sum = num1 + num2;

            System.out.println("sum of these numbers: "+sum);
        }
    }
}