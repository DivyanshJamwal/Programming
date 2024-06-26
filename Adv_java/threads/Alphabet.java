package MultiThreadingEx;

class Alphabets implements Runnable {
    public void run(){
        for(int i=65;i<92;i++){
            System.out.println((char)i);
            try {
                Thread.sleep(700);
            }catch (Exception e){
                e.getMessage();
            }
        }
        System.out.println("Alphabets class ended");
    }
}

class Number implements Runnable{
    public void run(){
        for(int i=1;i<20;i++){
            System.out.println(i);
            try {
                Thread.sleep(700);
            }catch (Exception e){
                System.out.println(e);
            }
        }
        System.out.println("Number class ended");
    }
}

class AlphabetsNumber{
    public static void main(String[] args) {
        Alphabets a = new Alphabets();
        Number n = new Number();
        Thread t1 = new Thread(a);
        Thread t2 = new Thread(n);
        t1.start();
        t2.start();
    }
}