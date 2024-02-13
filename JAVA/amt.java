package Coding_Practice.JAVA;

class Bank{
    int time;
    class Loan{
        int Interest;

        void calAmount(int  Interest){
            this.Interest = Interest;
        }
    }

}

public class amt {
    public static void main(String[] args) {
        Bank b = new Bank();
        Bank.Loan ob1 = b.new Loan();
        Bank.Loan ob2 = b.new Loan();
        Bank.Loan ob3 = b.new Loan();
        ob1.calAmount(5);
        ob2.calAmount(7);
        ob3.calAmount(9);
    }
}
