/*
Enter the shape
Enter the meaurement type
Enter sides
you will recieve the result
*/

import java.util.Scanner;

public class geometry {
    
    public static void main(String[] args) {
        
        Scanner ai = new Scanner(System.in);
        System.out.println("Enter the shape (0-circle, 1-triangle, 2-square, 3-rectangle, 4-parallelogram, 5-trapezium, 6-rhombus)");
        int shape = ai.nextInt();
        
        switch(shape){
            case 0:
                System.out.println("Enter the dimension (1-Perimeter , 2-Area , 3-Volume)");
                int a = ai.nextInt();
                if(a==1){
                    System.out.println("Enter the radius");
                    double r = ai.nextDouble();
                    System.out.println("Perimeter of your circle is " + (2*3.14*r));
                }
                else if(a==2){
                    System.out.println("Enter the radius");
                    double R = ai.nextDouble();
                    System.out.println("Area of your circle is " + (3.14*R*R));
                }
                else if(a==3){
                    System.out.println("Can't find volume");
                    System.out.println("Reason: Circle is a 2D shape");
                }
                else{
                    System.out.println("You have entered a wrong number");
                }
            break;
            case 1:
                System.out.println("Enter the dimension (1-Perimeter , 2-Area , 3-Volume)");
                int b = ai.nextInt();
                if(b==1){
                    System.out.println("Enter the side1 ");
                    double ps1 = ai.nextDouble();
                    System.out.println("Enter the side2 ");
                    double ps2 = ai.nextDouble();
                    System.out.println("Enter the side3 ");
                    double ps3 = ai.nextDouble();

                    System.out.println("Perimeter of your triangle is " + (ps1+ps2+ps3));
                }
                else if(b==2){
                    System.out.println("Enter the base ");
                    double ab = ai.nextDouble();
                    System.out.println("Enter the height ");
                    double ah = ai.nextDouble();
                    
                    System.out.println("Area of your triangle is " + (ab*ah/2));
                }
                else if(b==3){
                    System.out.println("Can't find volume");
                    System.out.println("Reason: Triangle is a 2D shape");
                }
                else{
                    System.out.println("You have entered a wrong number");
                }
            break;
            case 2:
                System.out.println("Enter the dimension (1-Perimeter , 2-Area , 3-Volume)");
                int c = ai.nextInt();
                if(c==1){
                    System.out.println("Enter the side ");
                    double psq = ai.nextDouble();

                    System.out.println("Perimeter of your square is " + (4*psq));
                }
                else if(c==2){
                    System.out.println("Enter the side ");
                    double asq = ai.nextDouble();
                    
                    System.out.println("Area of your square is " + (asq*asq));
                }
                else if(c==3){
                    System.out.println("Can't find volume");
                    System.out.println("Reason: square is a 2D shape");
                }
                else{
                    System.out.println("You have entered a wrong number");
                }
                ai.close();
                break;
         
        }
    }
}