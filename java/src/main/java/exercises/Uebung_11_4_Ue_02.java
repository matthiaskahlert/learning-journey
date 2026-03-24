/* 
Erstelle ein Java-Programm, das ein grafisches Fenster mit dem Titel "Mein Notizbuch" öffnet. 
In diesem Fenster sollen ein Textfeld, ein Speichern-Button und ein Löschen-Button angezeigt werden. 
Das Textfeld soll für die Eingabe von Notizen dienen. 
Beim Klicken auf den Speichern-Button soll der Inhalt des Textfelds in einem Array von Strings gespeichert werden.
Der Löschen-Button soll den Inhalt des Textfelds leeren. 
Verwende das BorderLayout für die Anordnung der Elemente, wobei das Textfeld im Zentrum, 
der Speichern-Button am unteren Rand und der Löschen-Button am oberen Rand des Fensters platziert sein sollen. 
Achte darauf, dass das Programm beim Schließen des Fensters beendet wird. 
Implementiere zusätzlich eine einfache Vererbungsstruktur, indem du eine Basisklasse Notizbuch erstellst, 
von der eine Klasse DigitalesNotizbuch erbt, welche die GUI-Elemente und die Funktionalitäten enthält.
*/

import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

// Basisklasse Notizbuch
class Notizbuch {
    protected String[] notizen;
    protected int notizCount;

    public Notizbuch(int kapazitaet) {
        notizen = new String[kapazitaet];
        notizCount = 0;
    }

    public void speichereNotiz(String notiz) {
        if (notizCount < notizen.length) {
            notizen[notizCount] = notiz;
            notizCount++;
        }
    }

    public String[] getAlleNotizen() {
        String[] result = new String[notizCount];
        System.arraycopy(notizen, 0, result, 0, notizCount);
        return result;
    }
}

// DigitalesNotizbuch erbt von Notizbuch
class DigitalesNotizbuch extends Notizbuch {
    private JFrame frame;
    private JTextArea textArea;

    public DigitalesNotizbuch() {
        super(100);
    }

    public void erstelleGUI() {
        frame = new JFrame("Mein Notizbuch");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);
        frame.setLayout(new BorderLayout());

        // Textfeld im CENTER
        textArea = new JTextArea();
        textArea.setLineWrap(true);
        textArea.setWrapStyleWord(true);
        frame.add(textArea, BorderLayout.CENTER);

        // Panel für Buttons
        JPanel topPanel = new JPanel();
        JButton loeschenButton = new JButton("Löschen");
        loeschenButton.addActionListener(e -> textArea.setText(""));
        topPanel.add(loeschenButton);
        frame.add(topPanel, BorderLayout.PAGE_START);

        JPanel bottomPanel = new JPanel();
        JButton speichernButton = new JButton("Speichern");
        speichernButton.addActionListener(e -> {
            String text = textArea.getText();
            if (!text.isEmpty()) {
                speichereNotiz(text);
                textArea.setText("");
                System.out.println("Notiz gespeichert! Gesamt: " + notizCount);
            }
        });
        bottomPanel.add(speichernButton);
        frame.add(bottomPanel, BorderLayout.PAGE_END);

        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}

public class Uebung_11_4_Ue_02 {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            DigitalesNotizbuch notizbuch = new DigitalesNotizbuch();
            notizbuch.erstelleGUI();
        });
    }
}
