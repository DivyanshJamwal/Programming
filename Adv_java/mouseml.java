import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;
class mouseml extends Frame implements MouseMotionListener{
    mouseml(){
        addMouseMotionListener(this);
        setSize(400,400);
        setLocationRelativeTo(null);
        setResizable(false);
        setLayout(null);
        setVisible(true);
    }
    public void mouseDragged(MouseEvent e){
        Graphics g = getGraphics();
        g.setColor(Color.yellow);
        g.fillOval(e.getX(),e.getY(),30,30);
    }
    public void mouseMoved(MouseEvent e){
        Graphics g = getGraphics();
        g.setColor(Color.red);
        g.fillOval(e.getX(),e.getY(),30,30);
    }
    public static void main(String[] args) {
        new mouseml();
    }
}


