import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

public class Fensterprogramm {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setSize(400, 500);
        f.setLayout(null); // Absolute Positionierung aktivieren

        JTextArea textArea = new JTextArea();
        textArea.setBounds(50, 50, 300, 300); // Position und Größe des Textbereichs setzen
        textArea.setBackground(Color.BLUE);
        textArea.setForeground(Color.WHITE);
        textArea.setFont(new Font("Serif", Font.ITALIC, 26));
        f.add(textArea);

        JButton button = new JButton("Klick mich!");
        button.setBounds(150, 400, 100, 30); // Position und Größe des Buttons setzen
        f.add(button);
        button.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                textArea.setText("Hallo Welt!");
            }
        });
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);        
    }
}