import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import java.awt.*;

public class table {
    JFrame f;
    table(){
        f = new JFrame("Table and ScrollPane");
        String data[][] = {{"100","Rohan","25000"},
        {"100","Rahul","27000"},
        {"101","Ravi","45000"},
        {"102","Shruti","56000"},
        {"103","Sumit","19000"},
        {"104","Piyush","29000"},
        {"105","Kartik","74000"},
        {"106","Ajay","62000"},
        {"107","Karan","33000"},
        {"108","Jay","37000"}};
        String col[]={"Empid","Empname","Empsal"};
        JTable tb=new JTable(data,col);
        JScrollPane sp=new JScrollPane(tb);
        sp.setBounds(30,40,200,100);
        f.add(sp);
        f.setSize(500,500);
        f.setResizable(false);
        f.setLayout(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.getContentPane().setBackground(Color.blue);
        f.setVisible(true);
    }
public static void main(String[] args) {
    new table();
}}
