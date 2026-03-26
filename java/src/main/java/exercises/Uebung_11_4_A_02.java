/* 
Aufgabe: Grafische Benutzerschnittstelle, Textdateien

Entwickle eine Java-Anwendung mit einer grafischen Benutzeroberfläche (GUI) unter Verwendung von Swing, 
die ein einfaches Notizbuch darstellt. Die Anwendung soll es ermöglichen, Notizen in einer Textbox zu schreiben, 
diese zu speichern und aus einer Textdatei zu laden. 
Die GUI soll mit einem GridLayout organisiert sein und mindestens einen Button zum Speichern 
und einen Button zum Laden der Notizen enthalten. 
Beachte dabei, dass die Anwendung objektorientiert aufgebaut sein soll und Vererbung verwendet, 
um Code-Wiederverwendung zu fördern.

a) Erstelle eine Klasse Notizbuch, die eine Liste von Notizen verwaltet. 
Jede Notiz soll aus einem Text bestehen und ein Erstellungsdatum haben. 
Implementiere Methoden zum Hinzufügen einer neuen Notiz, zum Speichern aller Notizen in einer Textdatei 
und zum Laden von Notizen aus einer Textdatei.

b) Entwickle eine Klasse NotizbuchGUI, die von JFrame erbt 
und die grafische Benutzeroberfläche für das Notizbuch bereitstellt. 
Die GUI soll ein JTextArea für die Texteingabe, zwei JButton-Objekte zum Speichern und Laden 
sowie ein GridLayout verwenden, um die Komponenten anzuordnen.

c) Implementiere die Funktionalität, 
dass beim Klicken auf den Speicher-Button die aktuelle Notiz zur Liste hinzugefügt, 
und alle Notizen in eine Textdatei gespeichert werden. 
Beim Klicken auf den Lade-Button sollen die Notizen aus der Textdatei geladen und im JTextArea angezeigt werden.
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

// a) Notizbuch-Kernklassen
class Notiz {
    private String text;
    private String datum;

    public Notiz(String text) {
        this.text = text;
        this.datum = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
    }

    public Notiz(String text, String datum) {
        this.text = text;
        this.datum = datum;
    }

    public String getText() {
        return text;
    }

    public String getDatum() {
        return datum;
    }

    @Override
    public String toString() {
        return datum + ": " + text;
    }
}

class U11A2Notizbuch {
    protected List<Notiz> notizen = new ArrayList<>();

    public void notizHinzufuegen(String text) {
        if (text != null && !text.trim().isEmpty()) {
            notizen.add(new Notiz(text));
        }
    }

    public void speichereInDatei(String dateiname) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(dateiname))) {
            for (Notiz n : notizen) {
                writer.write(n.getDatum() + "|" + n.getText());
                writer.newLine();
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Fehler beim Speichern: " + e.getMessage());
        }
    }

    public void ladeAusDatei(String dateiname) {
        notizen.clear();
        try (BufferedReader reader = new BufferedReader(new FileReader(dateiname))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split("\\|", 2);
                if (parts.length == 2) {
                    notizen.add(new Notiz(parts[1], parts[0]));
                }
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Fehler beim Laden: " + e.getMessage());
        }
    }

    public String alleNotizenAlsText() {
        StringBuilder sb = new StringBuilder();
        for (Notiz n : notizen) {
            sb.append(n.toString()).append("\n");
        }
        return sb.toString();
    }
}

// b) GUI mit Vererbung von JFrame
class NotizbuchGUI extends JFrame {
    private U11A2Notizbuch notizbuch;
    private JTextArea textArea;
    private JButton speichernButton, ladenButton;
    private static final String DATEINAME = "notizen.txt";

    public NotizbuchGUI() {
        super("Notizbuch");
        notizbuch = new U11A2Notizbuch();
        setSize(500, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setLayout(new GridLayout(2, 1));
        textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane);

        JPanel buttonPanel = new JPanel();
        speichernButton = new JButton("Speichern");
        ladenButton = new JButton("Laden");
        buttonPanel.add(speichernButton);
        buttonPanel.add(ladenButton);
        add(buttonPanel);

        // c) Button-Logik
        speichernButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = textArea.getText();
                notizbuch.notizHinzufuegen(text);
                notizbuch.speichereInDatei(DATEINAME);
                textArea.setText("");
                JOptionPane.showMessageDialog(NotizbuchGUI.this, "Notiz gespeichert.");
            }
        });

        ladenButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                notizbuch.ladeAusDatei(DATEINAME);
                textArea.setText(notizbuch.alleNotizenAlsText());
            }
        });
    }
}

public class Uebung_11_4_A_02 {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new NotizbuchGUI().setVisible(true);
        });
    }
}
