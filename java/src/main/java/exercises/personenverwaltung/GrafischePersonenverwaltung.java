package personenverwaltung;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONArray;
import org.json.JSONObject;
import javax.swing.table.AbstractTableModel;
import java.io.File;

public class GrafischePersonenverwaltung {

    private static List<Person> personenListe = new ArrayList<>();

    private static PersonenTableModel tableModel;

    public static void main(String[] args) {
        JFrame f = new JFrame("Personenverwaltung");
        f.setSize(1024, 768);
        f.setLayout(new BorderLayout());

        // Standardverzeichnis für Dateioperationen definieren
        File defaultDir = new File(System.getProperty("user.home"),
                "repositories/learning-journey/java/src/main/java/exercises/personenverwaltung");

        // Eine einzige JFileChooser-Instanz für Lade- und Speicheraktionen verwenden
        final JFileChooser fc = new JFileChooser(defaultDir);

        JButton loadButton = new JButton("Laden");
        loadButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int returnVal = fc.showOpenDialog(f);
                if (returnVal == JFileChooser.APPROVE_OPTION) {
                    try {
                        String text = new String(Files.readAllBytes(fc.getSelectedFile().toPath()),
                                StandardCharsets.UTF_8);
                        JSONObject json = new JSONObject(text);
                        JSONArray personen = json.getJSONArray("personen");

                        personenListe.clear();
                        for (int i = 0; i < personen.length(); i++) {
                            JSONObject person = personen.getJSONObject(i);
                            JSONObject adresse = person.getJSONObject("adresse");

                            personenListe.add(new Person(
                                    person.getString("vorname"),
                                    person.getString("nachname"),
                                    adresse.getString("strasse"),
                                    adresse.getInt("hausnummer"),
                                    adresse.getString("plz"),
                                    adresse.getString("ort")));
                        }

                        tableModel.fireTableDataChanged();
                        JOptionPane.showMessageDialog(f, "Daten erfolgreich geladen!", "Erfolg",
                                JOptionPane.INFORMATION_MESSAGE);
                    } catch (IOException exception) {
                        exception.printStackTrace();
                        JOptionPane.showMessageDialog(f, "Fehler beim Laden der Datei!", "Fehler",
                                JOptionPane.ERROR_MESSAGE);
                    }
                }
            }
        });

        JButton saveButton = new JButton("Speichern");
        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int returnVal = fc.showSaveDialog(f);
                if (returnVal == JFileChooser.APPROVE_OPTION) {
                    // prüfen, ob die Datei bereits existiert, Bestätigung zum Überschreiben
                    if (fc.getSelectedFile().exists()) {
                        int result = JOptionPane.showConfirmDialog(
                                f,
                                "Datei existiert bereits. Überschreiben?",
                                "Bestätigung",
                                JOptionPane.YES_NO_OPTION);
                        if (result != JOptionPane.YES_OPTION)
                            return;
                    }

                    try {
                        JSONArray personen = new JSONArray();
                        for (Person person : personenListe) {
                            JSONObject personJson = new JSONObject();
                            personJson.put("vorname", person.getVorname());
                            personJson.put("nachname", person.getNachname());

                            JSONObject adresseJson = new JSONObject();
                            adresseJson.put("strasse", person.getStrasse());
                            adresseJson.put("hausnummer", person.getHausnummer());
                            adresseJson.put("plz", person.getPlz());
                            adresseJson.put("ort", person.getOrt());

                            personJson.put("adresse", adresseJson);
                            personen.put(personJson);
                        }

                        JSONObject root = new JSONObject();
                        root.put("personen", personen);

                        Files.write(fc.getSelectedFile().toPath(), root.toString(4).getBytes(StandardCharsets.UTF_8));
                        JOptionPane.showMessageDialog(f, "Daten erfolgreich gespeichert!", "Erfolg",
                                JOptionPane.INFORMATION_MESSAGE);
                    } catch (IOException exception) {
                        exception.printStackTrace();
                        JOptionPane.showMessageDialog(f, "Fehler beim Speichern der Datei!", "Fehler",
                                JOptionPane.ERROR_MESSAGE);
                    }
                }
            }
        });

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(loadButton);
        buttonPanel.add(saveButton);

        f.add(buttonPanel, BorderLayout.PAGE_START);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        tableModel = new PersonenTableModel(personenListe);
        JTable table = new JTable(tableModel);
        JScrollPane scrollPane = new JScrollPane(table);
        f.add(scrollPane, BorderLayout.CENTER);
        f.setVisible(true);
    }

    static class Person {
        private String vorname;
        private String nachname;
        private String strasse;
        private int hausnummer;
        private String plz;
        private String ort;

        public Person(String vorname, String nachname, String strasse, int hausnummer, String plz, String ort) {
            this.vorname = vorname;
            this.nachname = nachname;
            this.strasse = strasse;
            this.hausnummer = hausnummer;
            this.plz = plz;
            this.ort = ort;
        }

        // Setter methoden für die Bearbeitung der Felder in der Tabelle
        public void setVorname(String vorname) {
            this.vorname = vorname;
        }

        public void setNachname(String nachname) {
            this.nachname = nachname;
        }

        public void setStrasse(String strasse) {
            this.strasse = strasse;
        }

        public void setHausnummer(int hausnummer) {
            this.hausnummer = hausnummer;
        }

        public void setPlz(String plz) {
            this.plz = plz;
        }

        public void setOrt(String ort) {
            this.ort = ort;
        }

        // Getter methoden zum Zugriff auf die Felder
        public String getVorname() {
            return vorname;
        }

        public String getNachname() {
            return nachname;
        }

        public String getStrasse() {
            return strasse;
        }

        public int getHausnummer() {
            return hausnummer;
        }

        public String getPlz() {
            return plz;
        }

        public String getOrt() {
            return ort;
        }
    }

    static class PersonenTableModel extends AbstractTableModel {
        private final List<Person> personenListe;

        public PersonenTableModel(List<Person> personenListe) {
            this.personenListe = personenListe;
        }

        @Override
        public int getColumnCount() {
            return 6;
        }

        @Override
        public int getRowCount() {
            return personenListe.size();
        }

        @Override
        public Object getValueAt(int row, int col) {
            Person p = personenListe.get(row);
            switch (col) {
                case 0:
                    return p.getVorname();
                case 1:
                    return p.getNachname();
                case 2:
                    return p.getStrasse();
                case 3:
                    return p.getHausnummer();
                case 4:
                    return p.getPlz();
                case 5:
                    return p.getOrt();
                default:
                    return null;
            }
        }

        @Override
        public void setValueAt(Object value, int row, int col) {
            Person p = personenListe.get(row);
            switch (col) {
                case 0:
                    p.setVorname(value.toString());
                    break;
                case 1:
                    p.setNachname(value.toString());
                    break;
                case 2:
                    p.setStrasse(value.toString());
                    break;
                case 3:
                    p.setHausnummer(Integer.parseInt(value.toString()));
                    break;
                case 4:
                    p.setPlz(value.toString());
                    break;
                case 5:
                    p.setOrt(value.toString());
                    break;
            }
            fireTableCellUpdated(row, col);
        }

        @Override
        public boolean isCellEditable(int row, int col) {
            return true; // Alle Zellen bearbeitbar machen
        }

        @Override
        public String getColumnName(int col) {
            switch (col) {
                case 0:
                    return "Vorname";
                case 1:
                    return "Nachname";
                case 2:
                    return "Straße";
                case 3:
                    return "Hausnummer";
                case 4:
                    return "PLZ";
                case 5:
                    return "Ort";
                default:
                    return null;
            }
        }
    }
}
