import javax.swing.*;
import java.awt.*;

class Flow {
    Flow(){
        JFrame f = new JFrame("Flow Layout");
        JButton b1= new JButton("1");
        b1.setBounds(20, 25, 80, 90);
        JButton b2= new JButton("2");
        b2.setBounds(25, 25, 80, 90);
        JButton b3= new JButton("3");
        b3.setBounds(30, 25, 80, 90);
        JButton b4= new JButton("4");
        b4.setBounds(35, 25, 80, 90);

        f.add(b1);
        f.add(b2);
        f.add(b3);
        f.add(b4);
        f.setSize(500,600);
        f.getContentPane().setBackground(Color.blue);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setLayout(new FlowLayout(FlowLayout.RIGHT,100,120));
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
    public static void main(String[] args) {
       new Flow();
    }
}
