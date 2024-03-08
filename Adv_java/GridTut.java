import javax.swing.*;

import java.awt.*;


class GridTut {
    JFrame f;
    GridTut(){
        f = new JFrame("Grid Layout");
        JButton b1 = new JButton("1");
        b1.setBounds(10, 15, 40, 30);
        JButton b2 = new JButton("2");
        b1.setBounds(15, 15, 40, 30);
        JButton b3 = new JButton("3");
        b1.setBounds(20, 15, 40, 30);
        JButton b4 = new JButton("4");
        b1.setBounds(25, 15, 40, 30);
        JButton b5 = new JButton("5");
        b1.setBounds(30, 15, 40, 30);
        JButton b6 = new JButton("6");
        b1.setBounds(35, 15, 40, 30);
        JButton b7 = new JButton("7");
        b1.setBounds(40, 15, 40, 30);
        JButton b8 = new JButton("8");
        b1.setBounds(45, 15, 40, 30);
        JButton b9 = new JButton("9");
        b1.setBounds(50, 15, 40, 30);
        JButton b10 = new JButton("10");
        b1.setBounds(55, 15, 40, 30);
        f.add(b1);
        f.add(b2);
        f.add(b3);
        f.add(b4);
        f.add(b5);
        f.add(b6);
        f.add(b7);
        f.add(b8);
        f.add(b9);
        f.add(b10);

        f.setSize(400,400);
        f.getContentPane().setBackground(Color.blue);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setLayout((new GridLayout(3,3,10,20)));
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
    public static void main(String[] args) {
       new GridTut();
    }
}
