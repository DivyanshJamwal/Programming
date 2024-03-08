import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
class mousel extends Frame implements MouseListener{
    mousel(){
        addMouseListener(this);
        setSize(400,400);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(null);
        setVisible(true);
    }
    public void mouseClicked(MouseEvent e){
        Graphics g = getGraphics();
        g.setColor(Color.BLUE);
        g.fillOval(e.getX(),e.getY(),40,40);
    }
    public void mousePressed(MouseEvent e){
        Graphics g = getGraphics();
        g.setColor(Color.red);
        g.fillOval(e.getX(),e.getY(),40,40);
    }
    public void mouseReleased(MouseEvent e){
        Graphics g = getGraphics();
        g.setColor(Color.green);
        g.fillOval(e.getX(),e.getY(),40,40);
    }
    public void mouseEntered(MouseEvent e){

    }
    public void mouseExited(MouseEvent e){

    }
    public static void main(String[] args) {
        new mousel();
    }
}


