package Date_time;

import java.time.*;
import java.time.temporal.*;
public class lcdTemp {
    public static void main(String[] args) {
        Period period = Period.ofDays(10);
        Temporal temp = period.addTo(LocalDate.now());
        System.out.println(temp);
        Period p = Period.of(2024, 6, 15);
        System.out.println(p.toString());
        Period p1 = Period.ofMonths(9);
        Period p2 = p1.minus(Period.ofMonths(6));
        System.out.println(p2);
        Period p3 = p1.plus(Period.ofMonths(3));
        System.out.println(p3);

    }
}
