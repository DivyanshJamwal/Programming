package Coding_Practice.JAVA;

public class getch {
    public static void main(String[] args) {
        String a = "java programming";
        char[]ch = new char[30];
        a.getChars(5,16,ch,0);
        System.out.println(ch);
    }
}
