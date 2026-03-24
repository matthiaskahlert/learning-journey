/* 
Entwickle ein Java-Programm, das ein grafisches Fenster mit einer einfachen Benutzeroberfläche erstellt. 
Das Fenster soll ein Grid-Layout verwenden, in dem mehrere Komponenten angeordnet werden: ein Textfeld, 
zwei Buttons und ein Label, das die Anzahl der Klicks auf den ersten Button zählt. 
Der zweite Button soll das Programm beenden. 

a) Erstelle ein JFrame-Objekt und setze die Größe auf 400x400 Pixel. 

b) Setze das Layout des JFrame-Objekts auf ein neues GridLayout mit 2 Zeilen und 2 Spalten.

c) Erstelle ein JTextArea-Objekt und füge es in die erste Zelle des Grids ein.

d) Erstelle ein JLabel-Objekt, initialisiere es mit "0 Klicks" und füge es in die zweite Zelle des Grids ein.

e) Erstelle einen JButton mit der Beschriftung "Klick mich" und füge ihn in die dritte Zelle des Grids ein. 
Implementiere einen ActionListener für diesen Button, der bei jedem Klick den Zähler im JLabel um eins erhöht.

f) Erstelle einen weiteren JButton mit der Beschriftung "Beenden" und füge ihn in die vierte Zelle des Grids ein. 
Implementiere einen ActionListener, der das Programm beendet, wenn dieser Button gedrückt wird.

g) Setze die Standard-Close-Operation des JFrame-Objekts auf EXIT_ON_CLOSE und mache das Fenster sichtbar.
*/

import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

public class Matthias_Kahlert_Teilpruefung_04 {

    public static void main(String[] args) {
        // SwingUtilities sorgt dafür, dass die Methode createAndShowUI später im
        // richtigen GUI-Thread von Swing ausgeführt wird
        SwingUtilities.invokeLater(Matthias_Kahlert_Teilpruefung_04::createAndShowUI);
    }

    private static void createAndShowUI() {
        // a) Erstelle JFrame und setze Größe
        JFrame frame = new JFrame("Grid-Layout GUI");
        frame.setSize(400, 400);
        // location null für center des Bildschirms
        frame.setLocationRelativeTo(null);

        // b) Setze GridLayout mit 2x2
        frame.setLayout(new GridLayout(2, 2, 10, 10));

        // c) Erstelle JTextArea
        JTextArea textArea = new JTextArea();
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        frame.add(textArea);

        // d) Erstelle JLabel mit Klick-Zähler
        JLabel clickLabel = new JLabel("0 Klicks");
        clickLabel.setHorizontalAlignment(JLabel.CENTER);
        frame.add(clickLabel);

        // e) Erstelle "Klick mich" Button mit ActionListener
        JButton clickButton = new JButton("Klick mich");
        final int[] clickCount = { 0 };
        // Lambdafunktion, e ist das click event, der clickcount erhöht sich bei click
        // und das Label wird aktualisiert
        clickButton.addActionListener(e -> {
            clickCount[0]++;
            clickLabel.setText(clickCount[0] + " Klicks");
        });
        frame.add(clickButton);

        // f) Erstelle "Beenden" Button
        JButton exitButton = new JButton("Beenden");
        // beende das programm bei buttonclick
        exitButton.addActionListener(e -> System.exit(0));
        frame.add(exitButton);

        // g) Wenn Fenster geschlossen wird, soll die Anwendung beendet werden
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Mache Fenster sichtbar
        frame.setVisible(true);
    }
}
