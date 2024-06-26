package threads;

class sleepmtd extends Thread{
    public void run(){
        for(int i = 1;i<10;i++){
            try{
                Thread.sleep(500);
            }
            catch(Exception e){
                System.out.println(e);
            }
            System.out.println(i);
        }
    }
    public static void main(String[] args) {
        sleepmtd t1 = new sleepmtd();
        sleepmtd t2 = new sleepmtd();

        t1.start();
        t2.start();
    }
}
