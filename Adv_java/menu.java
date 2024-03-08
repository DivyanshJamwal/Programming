import javax.swing.*;
import java.awt.event.*;
class menu implements ActionListener
{
JFrame f;
JMenuBar mb;
JMenu file,edit,help;
JMenuItem cut,copy,paste,selectAll,save,print;
JTextArea ta;
menu()
{
f=new JFrame("Text Editor");
cut=new JMenuItem("cut");
copy=new JMenuItem("copy");
paste=new JMenuItem("paste");
selectAll=new JMenuItem("selectAll");
save=new JMenuItem("save");
print=new JMenuItem("print");

cut.addActionListener(this);
copy.addActionListener(this);
paste.addActionListener(this);
selectAll.addActionListener(this);

mb=new JMenuBar();
file=new JMenu("File");
edit=new JMenu("Edit");
help=new JMenu("Help");

edit.add(cut);
edit.add(copy);
edit.add(paste);
edit.add(selectAll);
file.add(save);
file.add(print);

mb.add(file);
mb.add(edit);
mb.add(help);

ta=new JTextArea();
ta.setBounds(5,5,400,300);
f.add(mb);
f.add(ta);

f.setJMenuBar(mb);
f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
f.setLayout(null);
f.setSize(500,500);
f.setLocationRelativeTo(null);
f.setResizable(false);
f.setVisible(true);
}
public void actionPerformed(ActionEvent e)
{
if(e.getSource()==cut)
{
ta.cut();
}

if(e.getSource()==copy)
{
ta.copy();
}

if(e.getSource()==paste)
{
ta.paste();
}

if(e.getSource()==selectAll)
{
ta.selectAll();
}

}

public static void main(String args[])
{
new menu();
}
}