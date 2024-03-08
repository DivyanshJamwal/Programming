import javax.swing.JComboBox;
import javax.swing.JFrame;
import java.awt.Color;
import java.awt.event.*;

public class comboBox {
    JFrame f;
    comboBox(){
        f = new JFrame("ComboBox");
        String color[]={"red","blue","pink","purple","cyan"};
        @SuppressWarnings("rawtypes")
        JComboBox cb = new JComboBox<String>(color);
        cb.setBounds(30, 40, 100, 30);
        f.add(cb);
        f.setSize(400, 400);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setLayout(null);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        cb.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String selectedColor = (String) cb.getSelectedItem();
                if (selectedColor.equals("red")) {
                    f.getContentPane().setBackground(Color.red);
                } else if (selectedColor.equals("blue")) {
                    f.getContentPane().setBackground(Color.blue);
                } else if (selectedColor.equals("pink")) {
                    f.getContentPane().setBackground(Color.pink);
                } else if (selectedColor.equals("purple")) {
                    f.getContentPane().setBackground(Color.magenta);
                } else if (selectedColor.equals("cyan")) {
                    f.getContentPane().setBackground(Color.cyan);
                }
            }
        });
        f.setVisible(true);
    }
    public static void main(String[] args) {
        new comboBox();
    }
}
