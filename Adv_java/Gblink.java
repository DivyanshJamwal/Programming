import javax.swing.JFrame;
import java.awt.*;
import java.awt.Graphics;
import java.awt.Canvas;
class Gblink extends Canvas
{
public void paint(Graphics g)
{
Font f =new Font("Dialog",Font.BOLD,20);
g.setFont(f);
g.drawString("Blink",20,20);
setForeground(Color.red);
setBackground(Color.orange);
g.fillRect(50,50,100,100);
repaint();
}
public static void main(String args[])
{
Gblink dg=new Gblink();
JFrame f=new JFrame("Graphics application");
f.setSize(400,400);
f.add(dg);
f.setResizable(false);
f.setLocationRelativeTo(null);
f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//f.setLayout();
f.setVisible(true);
}
}