package Date_time;

import java.util.*;
public class LangArray {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Locale[] loc = {
            new Locale("en","US"),
            new Locale("fr","FR"),
            new Locale("sv","SE"),
            new Locale("it","IT"),
            new Locale("es","ES"),
            new Locale("no","NO"),
        };
        for(int i=0;i<loc.length;i++){
            String displayLang = loc[i].getDisplayLanguage(loc[i]);
            System.out.println(loc[i].toString()+": "+displayLang);
        }
    }
}
