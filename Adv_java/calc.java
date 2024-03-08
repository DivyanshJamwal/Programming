import javax.swing.*;
import java.awt.Color;
import java.awt.event.*;


public class calc {
    public static void main(String[] args) {
        JFrame f = new JFrame("Calculator ");
        JLabel l = new JLabel("First no.");
        l.setBounds(20, 20, 100, 30);
        l.setForeground(Color.yellow);
        JTextField tf = new JTextField();
        tf.setBounds(90, 20, 170, 30);
        f.add(l);

        JLabel l1 = new JLabel("Second no.");
        l1.setBounds(20, 70, 100, 30);
        l1.setForeground(Color.yellow);
        JTextField pf = new JTextField();
        pf.setBounds(90, 70, 170, 30);
        f.add(l1);
        f.add(tf);
        f.add(pf);

        JLabel l3 = new JLabel("Result");
        l3.setBounds(20, 200, 100, 30);
        l3.setForeground(Color.yellow);
        JTextField tf2 = new JTextField();
        tf2.setBounds(90, 110, 170, 30);
        tf2.setEditable(false);
        f.add(l1);
        f.add(tf);
        f.add(tf2);
        f.add(pf);

        JLabel l2 = new JLabel("Press Button to perform operation");
        l2.setBounds(20, 130, 270, 30);
        l2.setForeground(Color.yellow);
        f.add(l2);

        JButton bt = new JButton("Click");
        bt.setBounds(130,170,70,30);
        bt.setForeground(Color.blue);
        bt.setBackground(Color.cyan);
        bt.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                l2.setText("Welcome Divyansh! You are now Logged in.");
                String s1 = tf.getText();
                String s2 = pf.getText();
                int a = Integer.parseInt(s1);
                int b = Integer.parseInt(s2);
                int c = 0;
                if(e.getSource()==bt)
                {
                c=a+b;
                }
                String result=String.valueOf(c);
                tf2.setText(result);

            }
        });
        f.add(bt);
        f.setSize(400, 400);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().setBackground(Color.red);
        f.setLayout(null);
        f.setVisible(true);
    }
}