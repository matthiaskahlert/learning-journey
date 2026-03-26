/* 
Entwickle ein Java-Programm, das eine grafische Benutzeroberfläche mit Swing erstellt. 
Die Anwendung soll ein einfaches Quiz-Spiel sein, bei dem Fragen gestellt und beantwortet werden können. 
Folgende Funktionen und Elemente sollen implementiert werden:

a) Erstelle eine Klasse QuizFenster, die von JFrame erbt und im Konstruktor ein BorderLayout verwendet. 
Die Größe des Fensters soll 600x400 Pixel betragen.

b) Füge ein JTextArea hinzu, das die Frage anzeigt. 
Platziere es im CENTER des BorderLayouts.

c) Erstelle eine Klasse Frage, die eine Frage als String und ein Array von möglichen Antworten speichert. 
Die Klasse soll eine Methode getRichtigeAntwort() haben, die die richtige Antwort zurückgibt.

d) Erstelle ein JPanel mit einem GridLayout, das für jede mögliche Antwort einen Button enthält. 
Platziere dieses Panel im PAGE_END Bereich des BorderLayouts. 
Jeder Button soll einen ActionListener haben, der überprüft, ob die gewählte Antwort korrekt ist.

e) Implementiere eine Methode naechsteFrage(), die eine neue Frage samt Antworten im Quiz-Fenster anzeigt.

f) Erstelle eine Hauptklasse mit der main-Methode, die ein QuizFenster-Objekt erzeugt und anzeigt.
*/

import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

// c) Frage-Klasse
class Frage {
    private final String frage;
    private final String[] antworten;
    private final String richtigeAntwort;

    public Frage(String frage, String[] antworten, String richtigeAntwort) {
        this.frage = frage;
        this.antworten = antworten;
        this.richtigeAntwort = richtigeAntwort;
    }

    public String getFrage() {
        return frage;
    }

    public String[] getAntworten() {
        return antworten;
    }

    public String getRichtigeAntwort() {
        return richtigeAntwort;
    }
}

// a) QuizFenster erbt von JFrame
class QuizFenster extends JFrame {

    private final JTextArea frageTextArea;
    private final JPanel antwortPanel;
    private final Frage[] fragen;
    private int aktuellerFrageIndex = 0;

    public QuizFenster(Frage[] fragen) {
        super("Quiz");
        this.fragen = fragen;

        // a) BorderLayout im Konstruktor
        setLayout(new BorderLayout());
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // b) JTextArea im CENTER
        frageTextArea = new JTextArea();
        frageTextArea.setEditable(false);
        frageTextArea.setLineWrap(true);
        frageTextArea.setWrapStyleWord(true);
        frageTextArea.setFont(frageTextArea.getFont().deriveFont(16f));
        add(frageTextArea, BorderLayout.CENTER);

        // d) JPanel mit GridLayout im PAGE_END
        antwortPanel = new JPanel();
        add(antwortPanel, BorderLayout.PAGE_END);

        // e) erste Frage anzeigen
        naechsteFrage();

        setVisible(true);
    }

    // e) naechsteFrage zeigt neue Frage samt Antwort-Buttons
    public void naechsteFrage() {
        if (aktuellerFrageIndex >= fragen.length) {
            frageTextArea.setText("Quiz beendet! Alle Fragen wurden beantwortet.");
            antwortPanel.removeAll();
            antwortPanel.revalidate();
            antwortPanel.repaint();
            return;
        }

        Frage aktFrage = fragen[aktuellerFrageIndex];
        aktuellerFrageIndex++;

        frageTextArea.setText(aktFrage.getFrage());

        // d) Buttons für jede Antwort neu erstellen
        antwortPanel.removeAll();
        String[] antworten = aktFrage.getAntworten();
        antwortPanel.setLayout(new GridLayout(1, antworten.length, 8, 8));

        for (String antwort : antworten) {
            JButton button = new JButton(antwort);
            button.addActionListener(e -> {
                if (antwort.equals(aktFrage.getRichtigeAntwort())) {
                    JOptionPane.showMessageDialog(this, "Richtig!", "Ergebnis", JOptionPane.INFORMATION_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(this,
                            "Falsch! Die richtige Antwort war: " + aktFrage.getRichtigeAntwort(),
                            "Ergebnis", JOptionPane.ERROR_MESSAGE);
                }
                naechsteFrage();
            });
            antwortPanel.add(button);
        }

        antwortPanel.revalidate();
        antwortPanel.repaint();
    }
}

// f) Hauptklasse mit main-Methode
public class Uebung_11_4_A_01 {

    public static void main(String[] args) {
        Frage[] fragen = {
                new Frage("Was ist die Hauptstadt von Deutschland?",
                        new String[] { "München", "Berlin", "Hamburg", "Frankfurt" },
                        "Berlin"),
                new Frage("Wie viele Bundesländer hat Deutschland?",
                        new String[] { "14", "15", "16", "17" },
                        "16"),
                new Frage("Was ist 7 × 8?",
                        new String[] { "54", "56", "58", "60" },
                        "56"),
                new Frage("Welche Programmiersprache läuft auf der JVM?",
                        new String[] { "Python", "JavaScript", "Java", "C++" },
                        "Java")
        };

        SwingUtilities.invokeLater(() -> new QuizFenster(fragen));
    }
}
