package Date_time;

import java.time.*;
import java.time.zone.*;
import java.util.*;

@SuppressWarnings("unused")
public class Zone {
    public static void main(String[] args) {
        Set<String>str = ZoneId.getAvailableZoneIds();
        int i = 1;
        for(String s: str)
        {
            ZoneId z = ZoneId.of(s);
            LocalDate d = LocalDate.now(z);
            LocalTime t = LocalTime.now(z);
            System.out.println(i+"\t"+z+"\t"+d+"\t"+t);
            i++;
        }
    }
}
