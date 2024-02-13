package Coding_Practice.JAVA;

import java.util.*;
import java.io.File;
public class usfile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the ID: ");
        int id = sc.nextInt();
        String dirname = id + " ";
        File f = new File(dirname);
        f.mkdir();
        System.out.println("Enter the no. of family members: ");
        int n = sc.nextInt();
        int age;
        String name, eligibleText="",not_eligible="";
        for(int i=0;i<n;i++){
            System.out.println("Enter age: ");
            age = sc.nextInt();
            System.out.println("Enter name: ");
            name = sc.nextLine();
            if(age>18){
                eligibleText += (age+":"+name+ "\n");
                System.out.println(eligibleText);
            }
            else{
                not_eligible += (age+":"+name+"\n");
                System.out.println(not_eligible);
            }
        }

        sc.close();
        
    }
}
