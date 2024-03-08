import javax.swing.*;
import java.awt.Color;
import java.awt.event.*;


public class login {
    public static void main(String[] args) {
        JFrame f = new JFrame("Login Form");
        JLabel l = new JLabel("Username");
        l.setBounds(20, 20, 100, 30);
        l.setForeground(Color.yellow);
        JTextField tf = new JTextField();
        tf.setBounds(90, 20, 170, 30);
        f.add(l);
        
        JLabel l1 = new JLabel("Password");
        l1.setBounds(20, 70, 100, 30);
        l1.setForeground(Color.yellow);
        JPasswordField pf = new JPasswordField();
        pf.setBounds(90, 70, 170, 30);
        f.add(l1);
        f.add(tf);
        f.add(pf);
        
        JLabel l2 = new JLabel("Enter details to log in");
        l2.setBounds(20, 130, 270, 30);
        l2.setForeground(Color.yellow);
        f.add(l2);
        
        JButton b = new JButton("Click");
        b.setBounds(130,170,70,30);
        b.setForeground(Color.blue);
        b.setBackground(Color.cyan);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                l2.setText("Welcome Divyansh! You are now Logged in.");
            }
        });
        f.add(b);
        f.setSize(400, 400);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().setBackground(Color.red);
        f.setLayout(null);
        f.setVisible(true);
    }
}