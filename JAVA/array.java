import java.util.*;
public class array {
    public static void main(String[] args) {
        float marks[] = new float[5];
        float sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter marks of 5 subjects");
        for(int i = 0;i<5;i++){
            marks[i] = sc.nextFloat();
        }
        marks[2] = marks[2]+2;
        sc.close();
        for(int i = 0;i<5;i++){
            sum = sum + marks[i];
        }
        float avg = sum/5;
        System.out.println("Average is: "+ avg);
    }
}
