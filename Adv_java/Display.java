import javax.swing.JFrame;
import java.awt.*;
import java.awt.Graphics;
import java.awt.Canvas;
class Display extends Canvas
{
public void paint(Graphics g)
{
Font f =new Font("Dialog",Font.BOLD,20);
g.setFont(f);
g.drawString("Leo",20,20);
setForeground(Color.blue);
g.drawString("K21BP section",40,30);
setBackground(Color.yellow);
g.fillRect(50,50,100,100);
g.fillOval(100,100,100,100);
g.fillArc(200,150,100,100,40,60);
}
public static void main(String args[])
{
Display dg=new Display();
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