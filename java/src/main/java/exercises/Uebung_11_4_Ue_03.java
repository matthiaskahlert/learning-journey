/* 
Erstelle ein Java-Programm, das ein grafisches Fenster mit einem GridLayout für eine einfache Textverarbeitung erzeugt. In diesem Fenster sollen eine Textbox und zwei Buttons enthalten sein. Der erste Button soll den Text aus der Textbox in eine Textdatei speichern, der zweite Button soll den Inhalt aus einer Textdatei lesen und in der Textbox anzeigen. Verwende dabei die Swing-Bibliothek für die grafische Benutzerschnittstelle und die Klassen FileWriter und BufferedReader für das Schreiben und Lesen der Textdatei. Die Textdatei soll "textdata.txt" heißen und im Verzeichnis des Programms liegen.

a) Erstelle ein JFrame mit dem Titel "Textverarbeitung", setze die Größe auf 400x200 Pixel und sorge dafür, dass das Programm beendet wird, wenn das Fenster geschlossen wird.

b) Füge dem JFrame ein JPanel hinzu und setze das Layout auf ein neues GridLayout mit 2 Zeilen und 1 Spalte.

c) Erstelle eine JTextArea und füge sie als erstes Element des Gridlayouts hinzu.

d) Erstelle ein JPanel für die Buttons und füge dieses als zweites Element des Gridlayouts hinzu.

e) Erstelle zwei JButton-Objekte mit den Beschriftungen "Speichern" und "Laden" und füge sie dem Panel für die Buttons hinzu.

f) Implementiere einen ActionListener für den "Speichern"-Button, der den Text aus der JTextArea in die Datei "textdata.txt" schreibt.

g) Implementiere einen ActionListener für den "Laden"-Button, der den Text aus der Datei "textdata.txt" liest und in die JTextArea schreibt.

h) Zeige das JFrame an, indem du setVisible(true) aufrufst.
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class Uebung_11_4_Ue_03 {
    public static void main(String[] args) {
        // a) JFrame erstellen
        JFrame frame = new JFrame("Textverarbeitung");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // b) JPanel mit GridLayout (2 Zeilen, 1 Spalte)
        JPanel mainPanel = new JPanel(new GridLayout(2, 1));

        // c) JTextArea hinzufügen
        JTextArea textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        mainPanel.add(scrollPane);

        // d) Panel für Buttons
        JPanel buttonPanel = new JPanel();

        // e) Zwei Buttons erstellen
        JButton saveButton = new JButton("Speichern");
        JButton loadButton = new JButton("Laden");
        buttonPanel.add(saveButton);
        buttonPanel.add(loadButton);

        mainPanel.add(buttonPanel);
        frame.add(mainPanel);

        // f) ActionListener für Speichern
        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try (FileWriter writer = new FileWriter("java\\src\\main\\java\\exercises\\textdata.txt")) {
                    writer.write(textArea.getText());
                    JOptionPane.showMessageDialog(frame, "Text gespeichert.");
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(frame, "Fehler beim Speichern: " + ex.getMessage());
                }
            }
        });

        // g) ActionListener für Laden
        loadButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try (BufferedReader reader = new BufferedReader(
                        new FileReader("java\\src\\main\\java\\exercises\\textdata.txt"))) {
                    StringBuilder sb = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        sb.append(line).append("\n");
                    }
                    textArea.setText(sb.toString());
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(frame, "Fehler beim Laden: " + ex.getMessage());
                }
            }
        });

        // h) Fenster anzeigen
        frame.setVisible(true);
    }
}
