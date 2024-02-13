package Coding_Practice.Adv_java;
import java.util.stream.IntStream;
import java.util.*;

class Student{
    String name;
    int score;
    Student(String name,int score){
        this.name = name;
        this.score = score;
        }
        public String getname(){
            return this.name = name;
        }
        public int getscore(){
            return this.score = score;
        }
}

public class stream{
    public static void main(String[] args) {
        IntStream is = IntStream.rangeClosed(1,10);
        is.forEach(System.out.println());
    }
}
