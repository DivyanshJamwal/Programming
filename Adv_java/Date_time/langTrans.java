package Date_time;

import java.util.*;
public class langTrans {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Locale en = new Locale("en","US");
        Locale fr = new Locale("fr","FR");
        Locale sv = new Locale("sv","SE");
        Locale no = new Locale("no","NO");

        System.out.println("English language name is represented as: "+en.getDisplayLanguage());
        System.out.println("English language name is represented as: "+en.getDisplayLanguage(fr));
        System.out.println("English language name is represented as: "+en.getDisplayLanguage(sv));
        System.out.println("English language name is represented as: "+en.getDisplayLanguage(no));

    }
}
