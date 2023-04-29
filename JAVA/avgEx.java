import java.util.Scanner;
public class avgEx {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
            System.out.println("Enter 1st number: ");
            int num1 = s.nextInt();

            System.out.println("Enter last number: ");
            int num2 = s.nextInt();
            s.close();
        int i = 0;
        int sum = 0;
        int count = 0; 
        for(i=num1;i<num2;i++){
            sum=i+sum;
            count = count+1;
        }
        System.out.println(sum/count);
        
        
    }
}
