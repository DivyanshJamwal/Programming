//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
/* create database k21bp;
use k21bp;
create table emp(empid int,empname varchar(20),empsal int);*/

// import java.sql.*;
import javax.swing.*;
import java.awt.Color;
import java.awt.event.*;


public class Main {
    public static void main(String[] args) {
        JFrame f = new JFrame("Application Form ");
        JLabel l1 = new JLabel("StudentId ");
        l1.setBounds(30, 50, 170, 30);
        JLabel l2 = new JLabel("Name ");
        l2.setBounds(30, 90, 170, 30);
        JLabel l3 = new JLabel("Section");
        l3.setBounds(30, 130, 170, 30);
        JLabel l4 = new JLabel("Placement Status ");
        l4.setBounds(30, 170, 170, 30);
        JLabel l5 = new JLabel("Company");
        l5.setBounds(30, 210, 170, 30);
        JLabel l6 = new JLabel();
        l6.setBounds(30, 310, 170, 30);
        JTextField tf1 = new JTextField();
        tf1.setBounds(100, 50, 170, 30);
        JTextField tf2 = new JTextField();
        tf2.setBounds(100, 90, 170, 30);
        JTextField tf3 = new JTextField();
        tf3.setBounds(100, 130, 170, 30);
        JRadioButton r = new JRadioButton();
        r.setBounds(150, 170, 170, 30);
        JTextField tf4 = new JTextField();
        tf4.setBounds(100, 210, 170, 30);
        f.add(l1);
        f.add(l2);
        f.add(l3);
        f.add(l4);
        f.add(l5);
        f.add(l6);
        f.add(tf1);
        f.add(tf2);
        f.add(tf3);
        f.add(r);
        f.add(tf4);

        JButton b = new JButton("Insert");
        b.setBounds(20,270,70,30);
        JButton b2 = new JButton("Update");
        b2.setBounds(120,270,90,30);
        b.setForeground(Color.blue);
        b.setBackground(Color.cyan);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                if (r.isSelected()) {
                    l6.setText("Placed in company: ");
                }

            }
        });
        b2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                if (r.isSelected()) {
                    l6.setText("Values Updated");
                }
            }
        });
        f.add(b);
        f.add(b2);
        f.setSize(400, 400);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().setBackground(Color.red);
        f.setLayout(null);
        f.setVisible(true);
    }
}
