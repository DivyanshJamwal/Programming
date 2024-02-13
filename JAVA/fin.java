package Coding_Practice.JAVA;

public class fin {
    public static void main(String[] args) {
        System.out.println("Welcome to our code");
        try{
            int age = Integer.parseInt(args[0]);
            if(age>18){
                System.out.println("Eligible to vote");
            }
        }
        
        
        finally{
        System.out.println("Thanks for using our code");
        }
    }
}
