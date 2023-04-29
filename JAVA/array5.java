import java.util.*;
public class array5 {
    public static void main(String[] args) {
    
    // int[][] marks = {{56,67},{56,78,34},{23},{78,45,90,67}};
    int marks[][] = new int[4][];
    Scanner sc = new Scanner(System.in);
    int c;
    
    for (int i = 0; i < 4; i++) {
    System.out.println("how many subjects have student " + (i + 1) + " studied");
    c = sc.nextInt();
    int s1[] = new int[c];
    marks[i] = s1;
    
    System.out.println("Enter marks " + (i + 1) + " have scored");
    for (int j = 0; j < c; j++)
    s1[j] = sc.nextInt();
    }
    for (int i = 0; i < 4; i++) {
    for (int j = 0; j < marks[i].length; j++) {
    System.out.print(marks[i][j] + " ");
    }
    System.out.println();
    sc.close();
    }
    }
    }