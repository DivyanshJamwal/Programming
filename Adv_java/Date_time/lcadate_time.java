package Date_time;

import java.time.LocalDateTime;
import java.time.format.*;
public class lcadate_time 
{
public static void main(String args[])
{
LocalDateTime now=LocalDateTime.now();
System.out.println("Showing current date and time:- "+ now);
System.out.println(now.plusDays(100));
System.out.println(now.minusDays(10));
DateTimeFormatter format=DateTimeFormatter.ofPattern("dd-MM-yyyy mm:HH:ss");
String formatDateTime=now.format(format);
System.out.println("After formatting:- " +formatDateTime);
}
}
