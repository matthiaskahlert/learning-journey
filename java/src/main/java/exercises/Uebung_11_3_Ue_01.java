/* 
Entwickle ein Java-Programm, das ein grafisches Fenster mit den folgenden Komponenten erstellt: 
Ein Hauptfenster, ein Textfeld und zwei Buttons. 
Das Textfeld soll dabei für die Eingabe von Nutzernamen verwendet werden. 
Der erste Button soll "Anmelden" heißen und bei einem Klick eine Willkommensnachricht mit dem eingegebenen Nutzernamen 
in der Konsole ausgeben. Der zweite Button soll "Löschen" heißen und bei einem Klick das Textfeld leeren. 
Achte darauf, dass du für die Buttons entsprechende ActionListener implementierst. 
Die Größe des Fensters soll 400x300 Pixel betragen. 

a) Erstelle die Klasse AnmeldeFenster mit der main-Methode, in der das Fenster und die Komponenten initialisiert werden.

b) Füge dem Fenster ein JTextField hinzu und setze die Größe so, dass es sichtbar ist.

c) Implementiere zwei JButton-Objekte und füge sie dem Fenster hinzu.

d) Erstelle für jeden Button einen ActionListener, der die entsprechende Funktionalität umsetzt.

e) Setze das Verhalten des Fensters so, dass das Programm beendet wird, wenn das Fenster geschlossen wird.
*/

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;

public class Uebung_11_3_Ue_01 {
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(Uebung_11_3_Ue_01::createAndShowUi);
    }

    private static void createAndShowUi() {
        JFrame frame = new JFrame("AnmeldeFenster");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        JTextField textField = new JTextField(20);
        frame.add(textField);

        JButton anmeldenButton = new JButton("Anmelden");
        JButton loeschenButton = new JButton("Löschen");

        frame.add(anmeldenButton);
        frame.add(loeschenButton);

        anmeldenButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = textField.getText();
                System.out.println("Willkommen, " + name + "!");
            }
        });

        loeschenButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textField.setText("");
            }
        });

        frame.setVisible(true);
    }
}
