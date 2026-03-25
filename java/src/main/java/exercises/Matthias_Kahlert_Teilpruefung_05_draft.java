/* 
Aufgabe
Entwickle ein Java-Programm, das eine grafische Benutzeroberfläche mit einem GridLayout verwendet, 
um Daten in eine Datenbanktabelle einzugeben. 
Die Tabelle soll "Kunden" heißen und die Spalten "Vorname", "Nachname", "Adresse", "PLZ" und "Kundennummer" enthalten. 
Jede Spalte soll einen entsprechenden Datentyp haben: VARCHAR(255) für Textfelder und INT für die Kundennummer. 
Dein Programm soll folgende Funktionen haben:

a) Erstelle eine Klasse mit einer Methode, die eine Verbindung zu einer lokalen Datenbank herstellt
und die Tabelle "Kunden" erstellt, falls sie noch nicht existiert. 
Verwende dabei die in der Derby-Datenbank enthaltene JDBC-Schnittstelle.

b) Implementiere eine grafische Benutzeroberfläche mit Textfeldern für die Eingabe der Kundendaten 
und einem Button zum Speichern der Daten in der Datenbank. 
Die Oberfläche soll mit einem GridLayout organisiert sein, 
sodass für jede Spalte ein Label und ein Textfeld angeordnet sind.

c) Füge einen ActionListener zum Button hinzu, der die eingegebenen Daten aus den Textfeldern ausliest 
und mit einem INSERT INTO-Befehl in die Tabelle "Kunden" einfügt. 
Achte darauf, dass die Eingaben vor dem Einfügen auf Gültigkeit überprüft werden 
(z.B. keine leeren Felder, korrekte Nummernformate).

d) Implementiere eine Funktion, die alle Einträge aus der Tabelle "Kunden" ausliest 
und in der Konsole ausgibt. Nutze dazu eine SELECT-Abfrage.

Hinweis: Benenne dein Projekt als java-tpl-[nr]-[vorname]-[nachname] und stelle sicher, 
dass du den gesamten src-Ordner als .zip-Datei komprimierst und über das Prüfungsportal hochlädst. 
Zum Beispiel: java-tpl-1-john-doe.zip
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class Matthias_Kahlert_Teilpruefung_05_draft {
    private static final String DB_URL = "jdbc:derby:Datenbanken/KundenDB;create=true";

    public static void main(String[] args) {
        // GUI-Setup: GridLayout für übersichtliche Anordnung der Felder
        JFrame frame = new JFrame("Kundenverwaltung");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new BorderLayout());

        // Panel für Abstand zum Rand
        JPanel outerPanel = new JPanel(new BorderLayout());
        outerPanel.setBorder(BorderFactory.createEmptyBorder(20, 30, 20, 30));

        JPanel panel = new JPanel(new GridLayout(6, 2, 10, 10));
        JLabel lblVorname = new JLabel("Vorname:");
        JTextField tfVorname = new JTextField();
        JLabel lblNachname = new JLabel("Nachname:");
        JTextField tfNachname = new JTextField();
        JLabel lblAdresse = new JLabel("Adresse:");
        JTextField tfAdresse = new JTextField();
        JLabel lblPLZ = new JLabel("PLZ:");
        JTextField tfPLZ = new JTextField();
        JLabel lblKundennummer = new JLabel("Kundennummer:");
        JTextField tfKundennummer = new JTextField();
        JButton btnSpeichern = new JButton("Speichern");
        JButton btnAlleAnzeigen = new JButton("Alle anzeigen (Konsole)");

        // Labels rechtsbündig, Felder linksbündig (optional, für schöneres Layout)
        lblVorname.setHorizontalAlignment(SwingConstants.RIGHT);
        lblNachname.setHorizontalAlignment(SwingConstants.RIGHT);
        lblAdresse.setHorizontalAlignment(SwingConstants.RIGHT);
        lblPLZ.setHorizontalAlignment(SwingConstants.RIGHT);
        lblKundennummer.setHorizontalAlignment(SwingConstants.RIGHT);

        panel.add(lblVorname);
        panel.add(tfVorname);
        panel.add(lblNachname);
        panel.add(tfNachname);
        panel.add(lblAdresse);
        panel.add(tfAdresse);
        panel.add(lblPLZ);
        panel.add(tfPLZ);
        panel.add(lblKundennummer);
        panel.add(tfKundennummer);
        panel.add(btnSpeichern);
        panel.add(btnAlleAnzeigen);

        outerPanel.add(panel, BorderLayout.CENTER);
        frame.add(outerPanel, BorderLayout.CENTER);
        frame.setVisible(true);

        // Datenbank und Tabelle anlegen
        // Tabelle wird nur erstellt, falls sie noch nicht existiert.
        // Exception beim Erstellen wird abgefangen, falls die Tabelle schon existiert.
        createTableIfNotExists();

        // Speichern-Button Action
        btnSpeichern.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String vorname = tfVorname.getText().trim();
                String nachname = tfNachname.getText().trim();
                String adresse = tfAdresse.getText().trim();
                String plz = tfPLZ.getText().trim();
                String kundennummerStr = tfKundennummer.getText().trim();

                // Input validation: Keine leeren Felder, Kundennummer muss Zahl sein
                if (vorname.isEmpty() || nachname.isEmpty() || adresse.isEmpty() || plz.isEmpty()
                        || kundennummerStr.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Bitte alle Felder ausfüllen.");
                    return;
                }
                int kundennummer;
                try {
                    kundennummer = Integer.parseInt(kundennummerStr);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Kundennummer muss eine Zahl sein.");
                    return;
                }
                // Daten speichern (siehe insertKunde)
                insertKunde(vorname, nachname, adresse, plz, kundennummer);
                JOptionPane.showMessageDialog(frame, "Kunde gespeichert!");
                // Felder zurücksetzen
                tfVorname.setText("");
                tfNachname.setText("");
                tfAdresse.setText("");
                tfPLZ.setText("");
                tfKundennummer.setText("");
            }
        });

        // Alle anzeigen Button
        btnAlleAnzeigen.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                printAllKunden();
            }
        });
    }

    private static void createTableIfNotExists() {
        // try-with-resources: Connection und Statement werden automatisch geschlossen
        // Tabelle wird immer versucht zu erstellen. Falls sie schon existiert, wird die
        // Exception ignoriert.
        // Zwecks Eindeutigkeit habe ich die Kundennummer mit INT PRIMARY KEY gesetzt
        // Dadurch wird sichergestellt, dass keine doppelten Kundennummern in der
        // Tabelle gesetzt werden können.

        try (Connection conn = DriverManager.getConnection(DB_URL); Statement stmt = conn.createStatement()) {
            stmt.executeUpdate(
                    "CREATE TABLE Kunden (Vorname VARCHAR(255), Nachname VARCHAR(255), Adresse VARCHAR(255), PLZ VARCHAR(255), Kundennummer INT PRIMARY KEY)");
        } catch (SQLException e) {
            // Tabelle existiert evtl. schon
        }
    }

    /**
     * Speichert einen Kunden in die Datenbank.
     *
     * Verwendet PreparedStatement (schützt vor SQL-Injection und ist Best
     * Practice).
     * try-with-resources sorgt dafür, dass Connection und PreparedStatement sauber
     * geschlossen werden.
     */
    private static void insertKunde(String vorname, String nachname, String adresse, String plz, int kundennummer) {
        String sql = "INSERT INTO Kunden (Vorname, Nachname, Adresse, PLZ, Kundennummer) VALUES (?, ?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(DB_URL);
                PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, vorname);
            pstmt.setString(2, nachname);
            pstmt.setString(3, adresse);
            pstmt.setString(4, plz);
            pstmt.setInt(5, kundennummer);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "Fehler beim Speichern: " + e.getMessage());
        }
    }

    /**
     * Liest alle Kunden aus der Datenbank und gibt sie in der Konsole aus.
     *
     * try-with-resources sorgt für automatisches Schließen von Connection,
     * Statement und ResultSet.
     */
    private static void printAllKunden() {
        String sql = "SELECT * FROM Kunden";
        try (Connection conn = DriverManager.getConnection(DB_URL);
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {
            System.out.println("--- Alle Kunden ---");
            while (rs.next()) {
                System.out.println(
                        "Vorname: " + rs.getString("Vorname") + ", Nachname: " + rs.getString("Nachname") +
                                ", Adresse: " + rs.getString("Adresse") + ", PLZ: " + rs.getString("PLZ") +
                                ", Kundennummer: " + rs.getInt("Kundennummer"));
            }
        } catch (SQLException e) {
            System.out.println("Fehler beim Auslesen: " + e.getMessage());
        }
    }
}
