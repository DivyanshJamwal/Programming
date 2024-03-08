import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;

public class list implements MouseMotionListener {
    JFrame f;
    list(){
        f = new JFrame("JList Application");
        JLabel l = new JLabel();
        l.setBounds(150, 200, 190, 30);
        l.setForeground(Color.orange);
        DefaultListModel<String> df = new DefaultListModel<>();
        df.addElement("India");
        df.addElement("America");
        df.addElement("Australia");
        df.addElement("France");
        df.addElement("Europe");
        df.addElement("Italy");
        df.addElement("Japan");
        df.addElement("South Korea");
        df.addElement("Spain");
        df.addElement("Russia");
        df.addElement("Germany");
        JList<String> ls = new JList<>(df);
        ls.setBounds(40, 30, 100, 200);
        ls.addMouseMotionListener(this); // Add this line
        JButton b = new JButton("Select");
        b.setBounds(150, 150, 90, 30);
        b.setForeground(Color.blue);
        b.setBackground(Color.cyan);
        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                String data=new String();
                if(ls.getSelectedIndex()!=-1){
                    data="Selected Country "+ls.getSelectedValue();
                }
                l.setText(data);
            }
        });
        f.add(l);
        f.add(ls);
        f.add(b);
        f.setSize(400, 400);
        f.setResizable(false);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLocationRelativeTo(null);
        f.setLayout(null);
        f.setVisible(true);
    }
    public static void main(String[] args) {
        new list();
    }

    // Implement the MouseMotionListener methods
    @Override
    public void mouseMoved(MouseEvent e) {
        @SuppressWarnings("unchecked")
        JList<String> ls = (JList<String>) e.getSource();
        int index = ls.locationToIndex(e.getPoint());
        if (index != -1) {
            ls.setSelectedIndex(index);
        }
    }

    @Override
    public void mouseDragged(MouseEvent e) {
        // Do nothing
    }
}