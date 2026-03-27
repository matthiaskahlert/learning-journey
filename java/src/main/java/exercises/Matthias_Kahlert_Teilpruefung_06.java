
/* 
Aufgabe
Entwickle ein Java-Programm, das eine grafische Benutzeroberfläche mit einem GridLayout für eine einfache Kundenverwaltung bereitstellt. 
Das Programm soll es ermöglichen, Kundendaten in eine Datenbank einzutragen, anzuzeigen und zu aktualisieren. 
Verwende für die Datenbank die Apache Derby-Datenbank und für die GUI Java Swing-Komponenten. Gehe wie folgt vor:

a) Erstelle eine neue Datenbank mit dem Namen "KundenDB".

b) Innerhalb der Datenbank "KundenDB" soll eine Tabelle "Kunden" mit den Spalten "KundenID" (INT, Primary Key, Autoincrement), 
"Vorname" (VARCHAR(255)), "Nachname" (VARCHAR(255)), "Adresse" (VARCHAR(255)), "PLZ" (VARCHAR(5)) und "Ort" (VARCHAR(255)) erstellt werden.

c) Implementiere eine grafische Benutzeroberfläche mit einem GridLayout, die Textfelder für die Eingabe 
von Vorname, Nachname, Adresse, PLZ und Ort sowie Buttons zum Hinzufügen, Anzeigen und Aktualisieren von Kundendaten enthält.

d) Der Button "Hinzufügen" soll die eingegebenen Kundendaten in die Datenbanktabelle "Kunden" einfügen.

e) Der Button "Anzeigen" soll alle vorhandenen Kundendatensätze in der Konsole ausgeben.

f) Der Button "Aktualisieren" soll es ermöglichen, einen ausgewählten Kundendatensatz zu modifizieren 
und die Änderungen in der Datenbank zu speichern.


*/
// import com.formdev.flatlaf.FlatDarkLaf;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class Matthias_Kahlert_Teilpruefung_06 {

    private static final String DB_URL = DBConfig.getDBUrl("KundenDB");
    private static final String TABLE_NAME = "KUNDEN";

    public static void main(String[] args) {
        // FlatLaf aktivieren (muss vor allen Swing-Komponenten passieren)
        // FlatDarkLaf.setup();

        // GUI-Setup: GridLayout für übersichtliche Anordnung der Felder
        JFrame frame = new JFrame("Kundenverwaltung - Teilpruefung 06");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(520, 360);
        frame.setLayout(new BorderLayout());

        // Panel für Abstand zum Rand und Gridlayout wie gefordert
        JPanel outerPanel = new JPanel(new BorderLayout());
        outerPanel.setBorder(BorderFactory.createEmptyBorder(20, 30, 20, 30));

        JPanel panel = new JPanel(new GridLayout(8, 2, 8, 8));

        JLabel lblKundenId = new JLabel("KundenID (für Update):");
        JTextField tfKundenId = new JTextField();
        JLabel lblVorname = new JLabel("Vorname:");
        JTextField tfVorname = new JTextField();
        JLabel lblNachname = new JLabel("Nachname:");
        JTextField tfNachname = new JTextField();
        JLabel lblAdresse = new JLabel("Adresse:");
        JTextField tfAdresse = new JTextField();
        JLabel lblPlz = new JLabel("PLZ:");
        JTextField tfPlz = new JTextField();
        JLabel lblOrt = new JLabel("Ort:");
        JTextField tfOrt = new JTextField();

        JButton btnHinzufuegen = new JButton("Hinzufügen");
        JButton btnAnzeigen = new JButton("Anzeigen (Konsole)");
        JButton btnAktualisieren = new JButton("Aktualisieren");

        lblKundenId.setHorizontalAlignment(SwingConstants.RIGHT);
        lblVorname.setHorizontalAlignment(SwingConstants.RIGHT);
        lblNachname.setHorizontalAlignment(SwingConstants.RIGHT);
        lblAdresse.setHorizontalAlignment(SwingConstants.RIGHT);
        lblPlz.setHorizontalAlignment(SwingConstants.RIGHT);
        lblOrt.setHorizontalAlignment(SwingConstants.RIGHT);

        // für look and feel eine einheitliche Schrift
        Font font = new Font("Segoe UI", Font.PLAIN, 14);
        tfVorname.setFont(font);
        tfNachname.setFont(font);
        tfAdresse.setFont(font);
        tfPlz.setFont(font);
        tfOrt.setFont(font);
        tfKundenId.setFont(font);

        // Buttons etwas moderner machen
        btnHinzufuegen.setFocusPainted(false);
        btnAnzeigen.setFocusPainted(false);
        btnAktualisieren.setFocusPainted(false);

        panel.add(lblKundenId);
        panel.add(tfKundenId);
        panel.add(lblVorname);
        panel.add(tfVorname);
        panel.add(lblNachname);
        panel.add(tfNachname);
        panel.add(lblAdresse);
        panel.add(tfAdresse);
        panel.add(lblPlz);
        panel.add(tfPlz);
        panel.add(lblOrt);
        panel.add(tfOrt);
        panel.add(btnHinzufuegen);
        panel.add(btnAnzeigen);
        panel.add(new JLabel());
        panel.add(btnAktualisieren);

        outerPanel.add(panel, BorderLayout.CENTER);

        JLabel title = new JLabel("Kundenverwaltung");
        title.setFont(new Font("Segoe UI", Font.BOLD, 18));
        title.setHorizontalAlignment(SwingConstants.CENTER);
        frame.add(title, BorderLayout.NORTH);

        frame.add(outerPanel, BorderLayout.CENTER);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        // Datenbank und Tabelle anlegen, falls noch nicht vorhanden
        createTableIfNotExists();

        btnHinzufuegen.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String vorname = tfVorname.getText().trim();
                String nachname = tfNachname.getText().trim();
                String adresse = tfAdresse.getText().trim();
                String plz = tfPlz.getText().trim();
                String ort = tfOrt.getText().trim();

                if (!isInputValid(vorname, nachname, adresse, plz, ort)) {
                    JOptionPane.showMessageDialog(frame,
                            "Bitte alle Felder ausfüllen. PLZ muss genau 5 Ziffern haben.");
                    return;
                }

                try {
                    insertKunde(vorname, nachname, adresse, plz, ort);
                    JOptionPane.showMessageDialog(frame, "Kunde erfolgreich hinzugefügt.");
                    clearInputs(tfKundenId, tfVorname, tfNachname, tfAdresse, tfPlz, tfOrt);
                } catch (SQLException ex) {
                    JOptionPane.showMessageDialog(frame, "Fehler beim Hinzufügen: " + ex.getMessage());
                }
            }
        });

        btnAnzeigen.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                printAllKunden();
            }
        });

        btnAktualisieren.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String idText = tfKundenId.getText().trim();
                if (idText.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Für Aktualisieren bitte KundenID eintragen.");
                    return;
                }

                int id;
                try {
                    id = Integer.parseInt(idText);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "KundenID muss eine Zahl sein.");
                    return;
                }

                String vorname = tfVorname.getText().trim();
                String nachname = tfNachname.getText().trim();
                String adresse = tfAdresse.getText().trim();
                String plz = tfPlz.getText().trim();
                String ort = tfOrt.getText().trim();

                if (!isInputValid(vorname, nachname, adresse, plz, ort)) {
                    JOptionPane.showMessageDialog(frame,
                            "Bitte alle Felder ausfüllen. PLZ muss genau 5 Ziffern haben.");
                    return;
                }

                try {
                    int changed = updateKunde(id, vorname, nachname, adresse, plz, ort);
                    if (changed > 0) {
                        JOptionPane.showMessageDialog(frame, "Kunde erfolgreich aktualisiert.");
                    } else {
                        JOptionPane.showMessageDialog(frame,
                                "Kein Datensatz gefunden. Prüfe KundenID.");
                    }
                } catch (SQLException ex) {
                    JOptionPane.showMessageDialog(frame, "Fehler beim Aktualisieren: " + ex.getMessage());
                }
            }
        });
    }

    private static boolean isInputValid(String vorname, String nachname, String adresse, String plz, String ort) {
        return !vorname.isEmpty() && !nachname.isEmpty() && !adresse.isEmpty() && !ort.isEmpty()
                && plz.matches("\\d{5}");
    }

    private static void clearInputs(JTextField tfKundenId, JTextField tfVorname, JTextField tfNachname,
            JTextField tfAdresse, JTextField tfPlz, JTextField tfOrt) {
        tfKundenId.setText("");
        tfVorname.setText("");
        tfNachname.setText("");
        tfAdresse.setText("");
        tfPlz.setText("");
        tfOrt.setText("");
    }

    private static void createTableIfNotExists() {
        try (Connection conn = DriverManager.getConnection(DB_URL)) {
            if (!tableExists(conn, TABLE_NAME)) {
                try (Statement stmt = conn.createStatement()) {
                    stmt.executeUpdate(
                            "CREATE TABLE Kunden ("
                                    + "KundenID INT NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1), "
                                    + "Vorname VARCHAR(255), "
                                    + "Nachname VARCHAR(255), "
                                    + "Adresse VARCHAR(255), "
                                    + "PLZ VARCHAR(5), "
                                    + "Ort VARCHAR(255), "
                                    + "PRIMARY KEY (KundenID))");
                }
            }
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null, "Fehler beim Erstellen der Tabelle: " + e.getMessage());
        }
    }

    private static boolean tableExists(Connection conn, String tableName) throws SQLException {
        DatabaseMetaData metaData = conn.getMetaData();
        try (ResultSet rs = metaData.getTables(null, null, tableName.toUpperCase(), null)) {
            return rs.next();
        }
    }

    /**
     * insertKunde nimmt den Input aus der GUI und speichert ihn in der Datenbank.
     *
     * Verwendet PreparedStatement (schützt vor SQL-Injection und ist Best
     * Practice).
     */
    private static void insertKunde(String vorname, String nachname, String adresse, String plz, String ort)
            throws SQLException {
        try (Connection conn = DriverManager.getConnection(DB_URL)) {
            String sql = "INSERT INTO Kunden (Vorname, Nachname, Adresse, PLZ, Ort) VALUES (?, ?, ?, ?, ?)";
            try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
                pstmt.setString(1, vorname);
                pstmt.setString(2, nachname);
                pstmt.setString(3, adresse);
                pstmt.setString(4, plz);
                pstmt.setString(5, ort);
                pstmt.executeUpdate();
            }
        }
    }

    private static int updateKunde(int id, String vorname, String nachname, String adresse, String plz, String ort)
            throws SQLException {
        // Aktualisiert anhand KundenID.
        try (Connection conn = DriverManager.getConnection(DB_URL)) {
            String sql = "UPDATE Kunden SET Vorname = ?, Nachname = ?, Adresse = ?, PLZ = ?, Ort = ? WHERE KundenID = ?";

            try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
                pstmt.setString(1, vorname);
                pstmt.setString(2, nachname);
                pstmt.setString(3, adresse);
                pstmt.setString(4, plz);
                pstmt.setString(5, ort);
                pstmt.setInt(6, id);
                return pstmt.executeUpdate();
            }
        }
    }

    private static void printAllKunden() {
        String sql = "SELECT * FROM Kunden";
        // Liest alle Kunden aus und gibt alle vorhandenen Spalten dynamisch aus
        try (Connection conn = DriverManager.getConnection(DB_URL); // Verbindung zur Datenbank herstellen
                Statement stmt = conn.createStatement(); // Das Statement bereitet die SQL Abfrage vor
                ResultSet rs = stmt.executeQuery(sql)) { // ResultSet liefert das Ergebnis der Abfrage

            ResultSetMetaData meta = rs.getMetaData();
            int cols = meta.getColumnCount();

            System.out.println("--- Alle Kunden ---");
            while (rs.next()) {
                StringBuilder row = new StringBuilder();
                for (int i = 1; i <= cols; i++) {
                    if (i > 1) {
                        row.append(", ");
                    }
                    row.append(meta.getColumnName(i)).append(": ").append(rs.getString(i));
                }
                System.out.println(row);
            }
        } catch (SQLException e) {
            System.out.println("Fehler beim Anzeigen: " + e.getMessage());
        }
    }
}
