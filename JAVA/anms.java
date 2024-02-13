package Coding_Practice.JAVA;

abstract class bike{
    abstract void run();
    void repair(){
        System.out.println("Repairing a Bike");
    }
}

public class anms {
    public static void main(String[] args) {
        bike b = new bike() {
            void run(){
                System.out.println("Bike is running");
            }
            // void applybrakes(){

            // }
            // bike b = () -> {
                
            // };
        };
        b.run();

    }
}
