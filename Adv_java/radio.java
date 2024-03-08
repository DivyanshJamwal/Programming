import javax.swing.*;
import java.awt.event.*;
import java.awt.Color;

class radio {
    public static void main(String[] args) {
        JFrame f = new JFrame("Radio Button");
        JRadioButton rb1 = new JRadioButton("Married");
        rb1.setBounds(30,40, 100, 30);
        JRadioButton rb2 = new JRadioButton("UnMarried");
        rb2.setBounds(30,80, 100, 30);
        ButtonGroup bg = new ButtonGroup();
        bg.add(rb1);
        bg.add(rb2);
        JLabel lb = new JLabel();
        lb.setBounds(30, 150, 250, 30);
        JButton b = new JButton("Marital Status");
        b.setBounds(30, 200, 130, 30);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                if(rb1.isSelected()){
                    lb.setText("Marital Status of employee is married");
                }
                if(rb2.isSelected()){
                    lb.setText("Marital Status of employee is Un-married");
                }
            }
        });
        f.add(b);
        f.add(lb);
        f.add(rb1);
        f.add(rb2);
        f.setSize(400, 400);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setLayout(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().setBackground(Color.blue);
        f.setVisible(true);
    }
}
