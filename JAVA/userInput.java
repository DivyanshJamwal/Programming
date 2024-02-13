package Coding_Practice.JAVA;



public class userInput {

    public static void main(String[] args) {
        
        int principal = 5000;
        float rate = 13.4f;
        int time = 12;

        float simpleInterest = principal * rate * time / 100;

        System.out.println("the simple interest is " + simpleInterest);
    }


}