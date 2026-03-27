/* 
Case Study

Du arbeitest für ein Unternehmen, das eine Software für die Verwaltung von Büchereiinventar entwickelt. 
Deine Aufgabe ist es, ein Java-Programm zu schreiben, das Bücher in einer CSV-Datei speichert 
und diese auch wieder einlesen kann. Jedes Buch hat eine ISBN, einen Titel, einen Autor und ein Erscheinungsjahr. 
Die Bücher sollen in einer Klasse Buch verwaltet werden, die von einer abstrakten Klasse Medium erbt. 
Zusätzlich soll eine Klasse Buecherei erstellt werden, die eine Liste von Büchern verwaltet 
und die Funktionalität bietet, Bücher hinzuzufügen und alle Bücher auszugeben. 
Die grafische Benutzeroberfläche soll mit Swing umgesetzt werden und mindestens die Möglichkeit bieten, 
ein neues Buch hinzuzufügen und die Liste der Bücher anzuzeigen.

a) Entwickle die Klassenstruktur mit Medium als abstrakte Basisklasse und Buch als abgeleitete Klasse. 
Implementiere die notwendigen Attribute, Konstruktoren und Methoden.

b) Implementiere die Klasse Buecherei, die eine Liste von Medium-Objekten verwaltet.
 Füge Methoden zum Hinzufügen eines neuen Buches und zum Ausgeben aller Bücher hinzu.

c) Schreibe Methoden zum Speichern der Bücherliste in einer CSV-Datei und zum Einlesen dieser Datei.

d) Erstelle eine einfache Swing-Oberfläche mit einem Formular zum Hinzufügen neuer Bücher 
und einer Ausgabeliste für die vorhandenen Bücher.
*/

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Uebung_11_4_C_01 {
    // a) Abstrakte Basisklasse Medium
    abstract static class Medium {
        protected String titel;
        protected String autor;
        protected int erscheinungsjahr;

        public Medium(String titel, String autor, int erscheinungsjahr) {
            this.titel = titel;
            this.autor = autor;
            this.erscheinungsjahr = erscheinungsjahr;
        }

        // Abstrakte Methode
        public abstract String getInformationen();

        public String getTitel() {
            return titel;
        }

        public String getAutor() {
            return autor;
        }

        public int getErscheinungsjahr() {
            return erscheinungsjahr;
        }
    }

    // a) Buch als abgeleitete Klasse von Medium
    static class Buch extends Medium {
        private String isbn;

        public Buch(String isbn, String titel, String autor, int erscheinungsjahr) {
            super(titel, autor, erscheinungsjahr);
            this.isbn = isbn;
        }

        public String getISBN() {
            return isbn;
        }

        @Override
        public String getInformationen() {
            return isbn + "|" + titel + "|" + autor + "|" + erscheinungsjahr;
        }

        @Override
        public String toString() {
            return "ISBN: " + isbn + " | Titel: " + titel + " | Autor: " + autor + " | Jahr: " + erscheinungsjahr;
        }
    }

    // b) Klasse Buecherei verwaltet eine Liste von Medium-Objekten
    static class Buecherei {
        private List<Medium> medienListe;

        public Buecherei() {
            this.medienListe = new ArrayList<>();
        }

        public void buchHinzufuegen(Buch buch) {
            medienListe.add(buch);
        }

        public List<Medium> getAlleMedien() {
            return medienListe;
        }

        public void alleAusgeben() {
            System.out.println("=== Alle Bücher in der Bücherei ===");
            for (Medium medium : medienListe) {
                System.out.println(medium.toString());
            }
        }

        // c) Speichern in CSV-Datei
        public void speichereInCSV(String dateiname) {
            try (FileWriter writer = new FileWriter(dateiname)) {
                writer.write("ISBN,Titel,Autor,Erscheinungsjahr\n");
                for (Medium medium : medienListe) {
                    if (medium instanceof Buch) {
                        Buch buch = (Buch) medium;
                        writer.write(buch.getInformationen() + "\n");
                    }
                }
                System.out.println("Daten erfolgreich in " + dateiname + " gespeichert.");
            } catch (IOException e) {
                System.out.println("Fehler beim Speichern: " + e.getMessage());
            }
        }

        // c) Laden aus CSV-Datei
        public void ladeAusCSV(String dateiname) {
            try (BufferedReader reader = new BufferedReader(new FileReader(dateiname))) {
                String zeile;
                boolean istErsteZeile = true;
                medienListe.clear();

                while ((zeile = reader.readLine()) != null) {
                    if (istErsteZeile) {
                        istErsteZeile = false;
                        continue;
                    }
                    String[] teile = zeile.split("\\|");
                    if (teile.length == 4) {
                        String isbn = teile[0];
                        String titel = teile[1];
                        String autor = teile[2];
                        int jahr = Integer.parseInt(teile[3]);
                        medienListe.add(new Buch(isbn, titel, autor, jahr));
                    }
                }
                System.out.println("Daten erfolgreich aus " + dateiname + " geladen.");
            } catch (IOException e) {
                System.out.println("Fehler beim Laden: " + e.getMessage());
            } catch (NumberFormatException e) {
                System.out.println("Fehler beim Formatieren des Jahres: " + e.getMessage());
            }
        }
    }

    // d) Swing-Oberfläche
    static class BuechereiGUI extends JFrame {
        private Buecherei buecherei;
        private JTextField isbnField;
        private JTextField titelField;
        private JTextField autorField;
        private JTextField jahrField;
        private JTable tabelle;
        private DefaultTableModel tableModel;
        private static final String CSV_DATEI = "buecherei.csv";

        public BuechereiGUI() {
            super("Büchereiverwaltung");
            buecherei = new Buecherei();

            setSize(800, 600);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            setLocationRelativeTo(null);
            setLayout(new BorderLayout());

            // Oberes Panel: Eingabeformular
            JPanel formPanel = new JPanel(new GridLayout(5, 2, 5, 5));
            formPanel.setBorder(BorderFactory.createTitledBorder("Neues Buch hinzufügen"));

            formPanel.add(new JLabel("ISBN:"));
            isbnField = new JTextField();
            formPanel.add(isbnField);

            formPanel.add(new JLabel("Titel:"));
            titelField = new JTextField();
            formPanel.add(titelField);

            formPanel.add(new JLabel("Autor:"));
            autorField = new JTextField();
            formPanel.add(autorField);

            formPanel.add(new JLabel("Erscheinungsjahr:"));
            jahrField = new JTextField();
            formPanel.add(jahrField);

            JButton addButton = new JButton("Buch hinzufügen");
            addButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    buchHinzufuegenAction();
                }
            });
            formPanel.add(addButton);

            JButton clearButton = new JButton("Formular leeren");
            clearButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    formularLeeren();
                }
            });
            formPanel.add(clearButton);

            add(formPanel, BorderLayout.NORTH);

            // Mittleres Panel: Tabelle
            String[] spalten = { "ISBN", "Titel", "Autor", "Jahr" };
            tableModel = new DefaultTableModel(spalten, 0);
            tabelle = new JTable(tableModel);
            JScrollPane scrollPane = new JScrollPane(tabelle);
            add(scrollPane, BorderLayout.CENTER);

            // Unteres Panel: Buttons
            JPanel buttonPanel = new JPanel(new FlowLayout());

            JButton speichernButton = new JButton("Speichern");
            speichernButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    buecherei.speichereInCSV(CSV_DATEI);
                    JOptionPane.showMessageDialog(BuechereiGUI.this, "Daten gespeichert!");
                }
            });
            buttonPanel.add(speichernButton);

            JButton ladenButton = new JButton("Laden");
            ladenButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    buecherei.ladeAusCSV(CSV_DATEI);
                    tabelleAktualisieren();
                    JOptionPane.showMessageDialog(BuechereiGUI.this, "Daten geladen!");
                }
            });
            buttonPanel.add(ladenButton);

            add(buttonPanel, BorderLayout.SOUTH);

            setVisible(true);
        }

        private void buchHinzufuegenAction() {
            try {
                String isbn = isbnField.getText();
                String titel = titelField.getText();
                String autor = autorField.getText();
                int jahr = Integer.parseInt(jahrField.getText());

                if (isbn.isEmpty() || titel.isEmpty() || autor.isEmpty()) {
                    JOptionPane.showMessageDialog(this, "Bitte alle Felder füllen!");
                    return;
                }

                Buch buch = new Buch(isbn, titel, autor, jahr);
                buecherei.buchHinzufuegen(buch);
                tabelleAktualisieren();
                formularLeeren();
                JOptionPane.showMessageDialog(this, "Buch erfolgreich hinzugefügt!");
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(this, "Bitte geben Sie ein gültiges Jahr ein!");
            }
        }

        private void tabelleAktualisieren() {
            tableModel.setRowCount(0);
            for (Medium medium : buecherei.getAlleMedien()) {
                if (medium instanceof Buch) {
                    Buch buch = (Buch) medium;
                    Object[] zeile = {
                            buch.getISBN(),
                            buch.getTitel(),
                            buch.getAutor(),
                            buch.getErscheinungsjahr()
                    };
                    tableModel.addRow(zeile);
                }
            }
        }

        private void formularLeeren() {
            isbnField.setText("");
            titelField.setText("");
            autorField.setText("");
            jahrField.setText("");
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new BuechereiGUI();
            }
        });
    }
}
