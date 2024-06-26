package Date_time;

import java.time.LocalDate;

class intro
{
public static void main(String args[])
{

LocalDate date=LocalDate.now();
System.out.println("Today is:- "+date);
LocalDate yesterday=date.minusDays(1);
System.out.println("Yesterday was:- "+yesterday);
LocalDate tommorow=date.plusDays(1);
System.out.println("Tommorow's date:- "+tommorow);
System.out.println(date.getYear());
System.out.println(date.getMonth());
System.out.println(date.getMonthValue());
System.out.println(date.isLeapYear());

System.out.println(date.getDayOfMonth());
System.out.println(date.plusMonths(2));

LocalDate date1=LocalDate.of(2015,5,14);
System.out.println(date1.getDayOfWeek());
System.out.println(date1.lengthOfYear());
System.out.println(date1.lengthOfMonth());
System.out.println(date1.getDayOfYear());

String str="2014-10-14";
LocalDate date2=LocalDate.parse(str);
System.out.println("Showing date using parse method:- "+ date2);
}
}


