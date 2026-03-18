package personenverwaltung;

import com.formdev.flatlaf.FlatDarkLaf;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.AbstractTableModel;
import java.awt.*;
import java.io.File;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONObject;

public class PersonenverwaltungModernLight {

    private static List<Person> personenListe = new ArrayList<>();
    private static PersonenTableModel tableModel;

    public static void main(String[] args) {

        // Modernes Look & Feel
        FlatDarkLaf.setup();

        JFrame f = new JFrame("Personenverwaltung");
        f.setSize(1000, 700);
        f.setLayout(new BorderLayout());
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // ---------- TOP PANEL ----------
        JPanel topPanel = new JPanel(new BorderLayout());
        topPanel.setBorder(new EmptyBorder(10, 15, 10, 15));

        JLabel title = new JLabel("👥 Personenverwaltung");
        title.setFont(new Font("Segoe UI", Font.BOLD, 18));

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));

        JButton loadButton = new JButton("Laden");
        JButton saveButton = new JButton("Speichern");
        JButton newButton = new JButton("Neu");

        buttonPanel.add(loadButton);
        buttonPanel.add(saveButton);
        buttonPanel.add(newButton);

        topPanel.add(title, BorderLayout.WEST);
        topPanel.add(buttonPanel, BorderLayout.EAST);

        f.add(topPanel, BorderLayout.NORTH);

        // ---------- TABLE ----------
        tableModel = new PersonenTableModel(personenListe);
        JTable table = new JTable(tableModel);
        table.setRowHeight(32);
        table.setFillsViewportHeight(true);

        JScrollPane scrollPane = new JScrollPane(table);
        scrollPane.setBorder(new EmptyBorder(10, 15, 10, 15));

        f.add(scrollPane, BorderLayout.CENTER);

        // ---------- FILECHOOSER ----------
        File defaultDir = new File(System.getProperty("user.home"),
                "repositories/learning-journey/java/src/main/java/exercises/personenverwaltung");
        JFileChooser fc = new JFileChooser(defaultDir);

        // ---------- BUTTON ACTIONS ----------

        loadButton.addActionListener(e -> {
            int result = fc.showOpenDialog(f);

            if (result == JFileChooser.APPROVE_OPTION) {
                try {
                    String text = new String(
                            Files.readAllBytes(fc.getSelectedFile().toPath()),
                            StandardCharsets.UTF_8);

                    JSONObject json = new JSONObject(text);
                    JSONArray arr = json.getJSONArray("personen");

                    personenListe.clear();

                    for (int i = 0; i < arr.length(); i++) {
                        JSONObject p = arr.getJSONObject(i);
                        JSONObject adr = p.getJSONObject("adresse");

                        personenListe.add(new Person(
                                p.getString("vorname"),
                                p.getString("nachname"),
                                adr.getString("strasse"),
                                adr.getInt("hausnummer"),
                                adr.getString("plz"),
                                adr.getString("ort")));
                    }

                    tableModel.fireTableDataChanged();
                    JOptionPane.showMessageDialog(f, "Daten erfolgreich geladen!");

                } catch (Exception ex) {
                    ex.printStackTrace();
                    JOptionPane.showMessageDialog(f, "Fehler beim Laden: " + ex.getMessage());
                }
            }
        });

        saveButton.addActionListener(e -> {
            int result = fc.showSaveDialog(f);

            if (result == JFileChooser.APPROVE_OPTION) {

                if (fc.getSelectedFile().exists()) {
                    int confirm = JOptionPane.showConfirmDialog(
                            f,
                            "Datei existiert bereits. Überschreiben?",
                            "Bestätigung",
                            JOptionPane.YES_NO_OPTION);

                    if (confirm != JOptionPane.YES_OPTION)
                        return;
                }

                try {
                    JSONArray arr = new JSONArray();

                    for (Person p : personenListe) {
                        JSONObject obj = new JSONObject();
                        obj.put("vorname", p.getVorname());
                        obj.put("nachname", p.getNachname());

                        JSONObject adr = new JSONObject();
                        adr.put("strasse", p.getStrasse());
                        adr.put("hausnummer", p.getHausnummer());
                        adr.put("plz", p.getPlz());
                        adr.put("ort", p.getOrt());

                        obj.put("adresse", adr);
                        arr.put(obj);
                    }

                    JSONObject root = new JSONObject();
                    root.put("personen", arr);

                    Files.write(
                            fc.getSelectedFile().toPath(),
                            root.toString(4).getBytes(StandardCharsets.UTF_8));
                    JOptionPane.showMessageDialog(f, "Erfolgreich gespeichert!");
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(f, "Fehler beim Speichern");
                }
            }
        });

        newButton.addActionListener(e -> {
            // Leeres Person-Objekt zur Liste hinzufügen
            personenListe.add(new Person("", "nachname", "", 0, "", ""));
            tableModel.fireTableDataChanged(); // Tabelle aktualisieren
        });

        f.setVisible(true);
    }

    // ---------- MODEL ----------
    static class Person {
        private String vorname, nachname, strasse, plz, ort;
        private int hausnummer;

        public Person(String v, String n, String s, int h, String p, String o) {
            vorname = v;
            nachname = n;
            strasse = s;
            hausnummer = h;
            plz = p;
            ort = o;
        }

        public String getVorname() {
            return vorname;
        }

        public void setVorname(String v) {
            vorname = v;
        }

        public String getNachname() {
            return nachname;
        }

        public void setNachname(String n) {
            nachname = n;
        }

        public String getStrasse() {
            return strasse;
        }

        public void setStrasse(String s) {
            strasse = s;
        }

        public int getHausnummer() {
            return hausnummer;
        }

        public void setHausnummer(int h) {
            hausnummer = h;
        }

        public String getPlz() {
            return plz;
        }

        public void setPlz(String p) {
            plz = p;
        }

        public String getOrt() {
            return ort;
        }

        public void setOrt(String o) {
            ort = o;
        }
    }

    // ---------- TABLE MODEL ----------
    static class PersonenTableModel extends AbstractTableModel {

        private final List<Person> liste;
        private final String[] cols = { "Vorname", "Nachname", "Straße", "Nr.", "PLZ", "Ort" };

        public PersonenTableModel(List<Person> l) {
            this.liste = l;
        }

        public int getRowCount() {
            return liste.size();
        }

        public int getColumnCount() {
            return cols.length;
        }

        public String getColumnName(int c) {
            return cols[c];
        }

        public boolean isCellEditable(int r, int c) {
            return true;
        }

        public Object getValueAt(int r, int c) {
            Person p = liste.get(r);
            return switch (c) {
                case 0 -> p.getVorname();
                case 1 -> p.getNachname();
                case 2 -> p.getStrasse();
                case 3 -> p.getHausnummer();
                case 4 -> p.getPlz();
                case 5 -> p.getOrt();
                default -> null;
            };
        }

        public void setValueAt(Object val, int r, int c) {
            Person p = liste.get(r);
            switch (c) {
                case 0 -> p.setVorname(val.toString());
                case 1 -> p.setNachname(val.toString());
                case 2 -> p.setStrasse(val.toString());
                case 3 -> p.setHausnummer(Integer.parseInt(val.toString()));
                case 4 -> p.setPlz(val.toString());
                case 5 -> p.setOrt(val.toString());
            }
            fireTableCellUpdated(r, c);
        }
    }
}