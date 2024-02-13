package Coding_Practice.JAVA;

import java.util.*;
public class array4 {
    public static void main(String[] args) {
      int[][] marks = new int[4][5];
      Scanner sc = new Scanner(System.in);

      for(int i = 0;i<4;i++){
        System.out.println("Enter marks for Student "+ (i+1));
        for(int j = 0;j<5;j++){
            marks[i][j] = sc.nextInt();
            if(marks[i][j]<40 && marks[i][j]>35){
                marks[i][j] = 40;
            }
        }
      }
      for(int i = 0;i<4;i++){
        System.out.print("Updated marks for Student "+ (i+1) +": ");
        for(int j = 0;j<5;j++){
            System.out.print(marks[i][j]+ " ");
        }
        System.out.println();
    }
      sc.close();
    }
}
