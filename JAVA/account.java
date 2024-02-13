package Coding_Practice.JAVA;

import java.util.Scanner;
public class account {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Initial balance");
        int bal = sc.nextInt();
        System.out.println("Enter your choice");
        int choice = sc.nextInt();

        switch(choice){
            case 1:
            System.out.println("Enter the amount to be deposited");
            int amt = sc.nextInt();
            bal = bal+amt;
            break;
            case 2:
            System.out.println("Enter the amount to be withdrawn");
            int amnt = sc.nextInt();
            bal = bal-amnt;
            break;
            case 3:
            System.out.println("Your current balance is: "+bal);
            break;
            default:
                System.out.println("You have entered an invalid choice");
        }
        sc.close();
    }
}
