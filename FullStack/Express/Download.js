import java.util.*;
import java.time.*;

public class Calendar {
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

        LocalDate date = LocalDate.of(yr, mn, 1);

        int count = date.getDayOfWeek().getValue();
        int TotalDays = date.lengthOfMonth();

        while (count > 7) {
            count -= 7;
        }

        for (int i = 1; i <= count; i++) {
            System.out.print("\t");
        }

        for (int i = 1; i <= TotalDays; i++) {
            System.out.print(i + "\t");
            count++;

            if (count % 7 == 1) {
                System.out.println();
            }
        }
    }
}

component is responsible for ui
Component is a function which is 