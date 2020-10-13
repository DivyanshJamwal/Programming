import java.util.Scanner;

public class Interest {

    public static void main(String[] args) {
        
        Scanner interest = new Scanner(System.in);
        
        System.out.println("Enter principle value");
        
        int p = interest.nextInt();
        
        System.out.println("Enter rate");
        
        float r = interest.nextFloat();
        
        System.out.println("Enter time");
        
        int t = interest.nextInt();

        interest.close();

        float SimpleInterest = p*t*r/100;
        
        System.out.println("Your Simple Interest is " + SimpleInterest);
        
    }

}