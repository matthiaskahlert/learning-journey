
/* 
Erstelle ein einfaches Java-Programm mit einer grafischen Benutzerschnittstelle, 
die ein Hauptfenster mit einem GridLayout aufweist. 
Das GridLayout soll 3 Reihen und 2 Spalten haben. 
In jeder Zelle des Grids soll ein Button mit einer eindeutigen Beschriftung von "B1" bis "B6" platziert werden. 
Jeder Button soll einen ActionListener haben, 
der bei Betätigung des Buttons eine Nachricht in der Konsole ausgibt, 
welche den Text des Buttons und die Nachricht "wurde gedrückt" enthält. 
Zusätzlich soll das Fenster beim Schließen des Hauptfensters die Anwendung beenden. 
Kommentiere deinen Code angemessen, um die Funktionen der einzelnen Komponenten und Aktionen zu erklären.
*/
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Uebung_11_4_Ue_01 {
    public static void main(String[] args) {
        // Swing-Oberflächen sollten auf dem Event-Dispatch-Thread erzeugt werden.
        SwingUtilities.invokeLater(Uebung_11_4_Ue_01::createAndShowUi);
    }

    private static void createAndShowUi() {
        JFrame frame = new JFrame("GridLayout Buttons");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(3, 2, 8, 8));

        // Erzeugt sechs Buttons (B1 bis B6) und verknüpft jeweils einen Listener.
        for (int i = 1; i <= 6; i++) {
            String buttonText = "B" + i;
            JButton button = new JButton(buttonText);
            button.addActionListener(e -> System.out.println(buttonText + " wurde gedrückt"));
            frame.add(button);
        }

        frame.setSize(400, 300);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
