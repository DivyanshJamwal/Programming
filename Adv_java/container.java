import javax.swing.*;
import java.awt.Color;
class container
{
	public static void main(String[] args)
	{
		JFrame f  = new JFrame("My first application");

		JPanel p = new JPanel();
		p.setBounds(10,10,150,150);
		p.setBackground(Color.yellow);

		JButton b = new JButton("Click");
        
		b.setBounds(30,30,100,30);
		b.setForeground(Color.blue);
		p.add(b);

		JPanel p1= new JPanel();
		p1.setBounds(170,170,150,150);
		p1.setBackground(Color.green);

		JLabel l = new JLabel("Name:-");
		l.setBounds(40,40,50,30);
		l.setForeground(Color.red);


		JTextField tf = new JTextField("TextField");
		tf.setBounds(80,40,50,30);
		tf.setForeground(Color.red);
		p1.add(tf);
		f.setSize(400,400);
		f.setResizable(false);
		f.setLayout(null);
		f.setLocationRelativeTo(null);
		f.getContentPane().setBackground(new Color(124,120,132));
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setVisible(true);
		f.add(p);
		f.add(p1);
	}
}