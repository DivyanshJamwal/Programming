package Coding_Practice.JAVA;

import java.util.*;
public class array2 {
    public static void main(String[] args) {
        int temp[] = new int[6];
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter temperature");
        for(int i = 0;i<5;i++){
            temp[i] = sc.nextInt();
        }
        System.out.println("Enter temperature");
        int t = sc.nextInt();
        System.out.println("Enter index");
        int idx = sc.nextInt();
        for(int i=4;i<idx;i--){
            temp[i+1]=temp[i];
        }
        temp[idx]=t;
        System.out.println(temp);
        sc.close();
    }
}
