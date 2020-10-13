import java.util.Scanner;

public class calculator {

    public static void main(String[] args) {

        Scanner cal = new Scanner(System.in);
       
        System.out.println("Enter first number");
       
        double first = cal.nextDouble();
       
        System.out.println("Enter second number");
       
        double second = cal.nextDouble();
       
        System.out.println("Enter the operator");
        
        char operator = cal.next().charAt(0);

        System.out.println(cal);

        switch(operator){

            case '+':
                System.out.println("The sum of " + first + "+" + second + "=" + (first + second));
                System.out.println("Thanks for using this calculator");
            break;
            case '-':
                System.out.println("The difference of " + first + "+" + second + "=" + (first - second));
                System.out.println("Thanks for using this calculator");
            break;
            case '*':
                System.out.println("The product of " + first + "+" + second + "=" + (first * second));
                System.out.println("Thanks for using this calculator");
            break;
            case '/':
                System.out.println("The quotient of " + first + "+" + second + "=" + (first / second));
                System.out.println("Thanks for using this calculator");
            break;
            case '%':
                System.out.println("The remainder of " + first + "+" + second + "=" + (first % second));
                System.out.println("Thanks for using this calculator");
            break;
            default:
                System.out.println("You have entered an invalid operator");
            return;

            






        }
        
    }
    
}