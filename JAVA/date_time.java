package Coding_Practice.JAVA;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Month;
import java.time.ZoneId;

class date_time {
public static void main(String[] args) {


//LocalDate d = LocalDate.now();
//LocalDate d = LocalDate.of(1994,Month.FEBRUARY,29);

LocalDate d = LocalDate.now(ZoneId.of("America/Argentina/Rio_Gallegos"));
LocalTime t = LocalTime.now(ZoneId.of("America/Argentina/Rio_Gallegos"));
//System.out.println(ZoneId.getAvailableZoneIds());

System.out.println(d);
System.out.println(t);
int year = d.getYear();
int monthv = d.getMonthValue();
Month month = d.getMonth();
int dayofmonth = d.getDayOfMonth();
int dayofyear = d.getDayOfYear();
DayOfWeek dayofweek = d.getDayOfWeek();
Boolean leap = d.isLeapYear();

System.out.println("The year is: " + year);
System.out.println("The month value is: " + monthv);
System.out.println("The month is: " + month);
System.out.println("The Day of month is: " + dayofmonth);
System.out.println("The Day of year is: " + dayofyear);
System.out.println("The Day of week is: " + dayofweek);
System.out.println("Is " + year + " a Leap Year?: " + leap);


}
}
