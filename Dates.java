// dumb program to get all the dates between June 7th and October 17th for a personal project of mine
// uh nothing important or notable really

import java.util.*;

public class Dates {
    public static void main(String[] args) {
        for (Date date : getDaysBetweenDates(new Date(2021, Calendar.JUNE, 7), new Date(2021, Calendar.OCTOBER, 17))) {
            String[] dateString = date.toString().split(" ");
            System.out.println(dateString[1] + " " + dateString[2] + " - ");
        }
    }

    public static List<Date> getDaysBetweenDates(Date startdate, Date enddate)
    {
        List<Date> dates = new ArrayList<Date>();
        Calendar calendar = new GregorianCalendar();
        calendar.setTime(startdate);

        while (calendar.getTime().before(enddate))
        {
            Date result = calendar.getTime();
            dates.add(result);
            calendar.add(Calendar.DATE, 1);
        }
        return dates;
    }
}
