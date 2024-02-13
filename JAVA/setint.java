package Coding_Practice.JAVA;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;
import java.util.LinkedList;
    
    public class setint {
    
        public static void main(String[] args) {
            HashSet<String> colors = new HashSet<>();

            colors.add("Red");
            colors.add("Green");
            colors.add("Blue");
            colors.add("Yellow");
            
            System.out.println("HashSet: " + colors);
            
            LinkedList<String> list = new LinkedList<>(colors);
            
            String firstElement = list.getFirst();
            System.out.println("First Element: " + firstElement);
            String lastElement = list.getLast();
            System.out.println("Last Element: " + lastElement);
            String remf = list.removeFirst();
            System.out.println("Remove First Element: " + remf);
            String reml = list.removeLast();
            System.out.println("Remove Last Element: " + reml);
            
            System.out.println("List: " + list);
            
            LinkedHashSet<String> cols = new LinkedHashSet<>();
            
            cols.add("Red");
            cols.add("Green");
            cols.add("Blue");
            cols.add("Yellow");
            
            System.out.println("LinkedHashSet: " + cols);
            
            TreeSet<String> clr = new TreeSet<>();
            
            clr.add("Red");
            clr.add("Green");
            clr.add("Blue");
            clr.add("Yellow");
            
            System.out.println("TreeSet: " + clr);
            

        }
    }
    

