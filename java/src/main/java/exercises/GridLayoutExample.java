import javax.swing.*;
import java.awt.*;

public class GridLayoutExample {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setSize(300, 200);
        f.setLayout(new GridLayout(3, 2));

        JButton button1 = new JButton("B1");
        f.add(button1);

        JButton button2 = new JButton("B2");
        f.add(button2);

        JButton button3 = new JButton("B3");
        f.add(button3);

        JButton button4 = new JButton("B4");
        f.add(button4);

        JButton button5 = new JButton("B5");
        f.add(button5);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
