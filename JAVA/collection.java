import java.util.ArrayList;
import java.util.Collections;

public class collection {
    public static void main(String[] args) {
        String s = "Hello";
        String s1 = "Hello";
        System.out.println(s.equals(s1));

        ArrayList<String> colors = new ArrayList<>();
        colors.add("Red");
        colors.add("Purple");
        colors.add("Cyan");
        colors.add("Black");
        colors.add("Blue");
        colors.add("Yellow");
        
        ArrayList<Integer> num = new ArrayList<>();
        num.add(1);
        num.add(2);
        num.add(7);
        num.add(5);
        num.add(3);
        num.add(6);
        System.out.println(colors);
        Collections.sort(num);
        System.out.println(num);
    }
}
