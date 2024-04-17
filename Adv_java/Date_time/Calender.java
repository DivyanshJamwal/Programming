package Date_time;

import java.util.*;
import java.time.*;

public class Calender {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the year");
        int yr = sc.nextInt();
        System.out.println("Enter the month");
        int mn = sc.nextInt();

        System.out.print("Sun\t");
        System.out.print("Mon\t");
        System.out.print("Tue\t");
        System.out.print("Wed\t");
        System.out.print("Thu\t");
        System.out.print("Fri\t");
        System.out.println("Sat\t");

        LocalDate date = LocalDate.now();

        int count = 1;
        int TotalDays = date.lengthOfMonth();

        while (count<= TotalDays){
            System.out.print(count + "\t");
            count +=1;

            if(count%7==1){
                System.out.println();
            }
        }
    }
}
