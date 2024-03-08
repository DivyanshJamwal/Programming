import javax.swing.*;
import java.awt.Color;
import java.awt.event.*;


public class Event {
    public static void main(String[] args) {
        JFrame f = new JFrame("Event ");
        JLabel l = new JLabel("Press button to show ");
        l.setBounds(30, 60, 170, 30);
        l.setForeground(Color.yellow);
        f.add(l);

        JButton b = new JButton("Click");
        b.setBounds(20,20,70,30);
        b.setForeground(Color.blue);
        b.setBackground(Color.cyan);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                l.setText("Welcome!");
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
