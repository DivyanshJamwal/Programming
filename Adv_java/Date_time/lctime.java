package Date_time;

import java.time.LocalTime;
import java.time.*;
class lctime
{
public static void main(String args[]) {
LocalTime time=LocalTime.of(4,19,48);
System.out.println(time);
LocalTime time1=LocalTime.now();
System.out.println("Current time is:- "+time1);
System.out.println(time1.getHour());
System.out.println(time1.getMinute());
System.out.println(time1.getSecond());
System.out.println(time1.getNano());
LocalTime time3=time1.minusHours(2);
System.out.println("Changes in Hours:- "+time3);
LocalTime time4=time1.minusMinutes(10);
System.out.println("changes in minutes:- "+time4);
System.out.println(time4.plusHours(4));
System.out.println(time4.plusMinutes(10));
ZoneId zone=ZoneId.of("Asia/Kolkata");
LocalTime lt=LocalTime.now(zone);
System.out.println("Time in zone specific:- "+lt);
}
}
