package Coding_Practice.JAVA;

public class array6 {
    void calAverage(int x[]){
        int sum = 0;
        for(int i = 0;i<x.length;i++){
        sum = x[i];
        System.out.println("Average is "+ (sum/x.length));
        }
    }
    public static void main(String[] args) {
        int a[] = {34,56,78};
        array6 n = new array6();
        n.calAverage(a);
    }
}
