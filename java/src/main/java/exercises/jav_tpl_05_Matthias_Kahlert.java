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

// import com.formdev.flatlaf.FlatDarkLaf;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class jav_tpl_05_Matthias_Kahlert {
    private static final String DB_URL = "jdbc:derby:Datenbanken/KundenDB;create=true";
    private static final String TABLE_NAME = "KUNDEN";

    public static void main(String[] args) {
        // FlatLaf aktivieren (muss vor allen Swing-Komponenten passieren)
        // FlatDarkLaf.setup();

        // GUI-Setup: GridLayout für übersichtliche Anordnung der Felder
        JFrame frame = new JFrame("Kundenverwaltung");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 320);
        frame.setLayout(new BorderLayout());

        // Panel für Abstand zum Rand und Gridlayout wie gefordert
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

        // Labels rechtsbündig fand ich schöner
        lblVorname.setHorizontalAlignment(SwingConstants.RIGHT);
        lblNachname.setHorizontalAlignment(SwingConstants.RIGHT);
        lblAdresse.setHorizontalAlignment(SwingConstants.RIGHT);
        lblPLZ.setHorizontalAlignment(SwingConstants.RIGHT);
        lblKundennummer.setHorizontalAlignment(SwingConstants.RIGHT);

        // für look and feel eine einheitliche Schrift
        Font font = new Font("Segoe UI", Font.PLAIN, 14);
        tfVorname.setFont(font);
        tfNachname.setFont(font);
        tfAdresse.setFont(font);
        tfPLZ.setFont(font);
        tfKundennummer.setFont(font);

        // Buttons etwas moderner machen
        btnSpeichern.setFocusPainted(false);
        btnAlleAnzeigen.setFocusPainted(false);

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

        // Optional: Titel oben
        JLabel title = new JLabel("Kundenverwaltung");
        title.setFont(new Font("Segoe UI", Font.BOLD, 18));
        title.setHorizontalAlignment(SwingConstants.CENTER);
        frame.add(title, BorderLayout.NORTH);

        frame.add(outerPanel, BorderLayout.CENTER);
        frame.setLocationRelativeTo(null); // Fenster zentrieren
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

                // Eingaben validieren: Keine leeren Felder, Kundennummer muss Zahl sein
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
        try (Connection conn = DriverManager.getConnection(DB_URL)) {
            if (!tableExists(conn, TABLE_NAME)) {
                try (Statement stmt = conn.createStatement()) {
                    stmt.executeUpdate(
                            "CREATE TABLE Kunden (Vorname VARCHAR(255), Nachname VARCHAR(255), Adresse VARCHAR(255), PLZ VARCHAR(255), Kundennummer INT PRIMARY KEY)");
                }
            }
        } catch (SQLException e) {
            System.out.println("Fehler beim Erstellen der Tabelle: " + e.getMessage());
        }
    }

    private static boolean tableExists(Connection conn, String tableName) throws SQLException {
        DatabaseMetaData metaData = conn.getMetaData();
        try (ResultSet rs = metaData.getTables(null, null, tableName.toUpperCase(), null)) {
            return rs.next();
        }
    }

    private static boolean columnExists(Connection conn, String tableName, String columnName) throws SQLException {
        DatabaseMetaData metaData = conn.getMetaData();
        try (ResultSet rs = metaData.getColumns(null, null, tableName.toUpperCase(), columnName.toUpperCase())) {
            return rs.next();
        }
    }

    /**
     * insertKunde nimmt den input aus der GUI und speichert ihn in der Datenbank.
     *
     * Verwendet PreparedStatement (schützt vor SQL-Injection und ist Best
     * Practice).
     * prepareStatement hilft mir, SQL-Befehle mit Platzhaltern vorzubereiten und
     * Werte sicher einzusetzen.
     * try-with-resources sorgt dafür, dass Connection und PreparedStatement sauber
     * geschlossen werden.
     */
    private static void insertKunde(String vorname, String nachname, String adresse, String plz, int kundennummer) {
        try (Connection conn = DriverManager.getConnection(DB_URL);
                PreparedStatement pstmt = conn.prepareStatement(resolveInsertSql(conn))) {
            pstmt.setString(1, vorname);
            pstmt.setString(2, nachname);
            pstmt.setString(3, adresse);
            pstmt.setString(4, plz);

            boolean hasKundennummer = columnExists(conn, TABLE_NAME, "KUNDENNUMMER");
            boolean hasOrt = columnExists(conn, TABLE_NAME, "ORT");

            if (hasKundennummer && hasOrt) {
                pstmt.setInt(5, kundennummer);
                pstmt.setString(6, "");
            } else if (hasKundennummer) {
                pstmt.setInt(5, kundennummer);
            } else if (hasOrt) {
                pstmt.setString(5, "");
            }

            pstmt.executeUpdate();
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "Fehler beim Speichern: " + e.getMessage());
        }
    }

    private static String resolveInsertSql(Connection conn) throws SQLException {
        boolean hasKundennummer = columnExists(conn, TABLE_NAME, "KUNDENNUMMER");
        boolean hasOrt = columnExists(conn, TABLE_NAME, "ORT");

        if (hasKundennummer && hasOrt) {
            return "INSERT INTO Kunden (Vorname, Nachname, Adresse, PLZ, Kundennummer, Ort) VALUES (?, ?, ?, ?, ?, ?)";
        }
        if (hasKundennummer) {
            return "INSERT INTO Kunden (Vorname, Nachname, Adresse, PLZ, Kundennummer) VALUES (?, ?, ?, ?, ?)";
        }
        if (hasOrt) {
            return "INSERT INTO Kunden (Vorname, Nachname, Adresse, PLZ, Ort) VALUES (?, ?, ?, ?, ?)";
        }
        return "INSERT INTO Kunden (Vorname, Nachname, Adresse, PLZ) VALUES (?, ?, ?, ?)";
    }

    /**
     * Liest alle Kunden aus der Datenbank und gibt sie in der Konsole aus.
     *
     * try-with-resources sorgt für automatisches Schließen von Connection,
     * Statement und ResultSet.
     */
    private static void printAllKunden() {
        String sql = "SELECT * FROM Kunden";
        try (Connection conn = DriverManager.getConnection(DB_URL); // Verbindung zur Datenbank herstellen
                Statement stmt = conn.createStatement(); // Das Statement bereitet die SQL Abfrage vor
                ResultSet rs = stmt.executeQuery(sql)) { // ResultSet liefert das Ergebnis der Abfrage
            System.out.println("--- Alle Kunden ---");
            while (rs.next()) { // rs.next geht zur nächsten zeile und gibt true zurück solange noch daten da
                                // sind
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
