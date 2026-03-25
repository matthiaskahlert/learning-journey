package personenverwaltung;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class Kundenverwaltung {
    private static final String DB_URL = "jdbc:derby:Datenbanken/KundenDB;create=true";

    public static void main(String[] args) {
        // GUI Setup
        JFrame frame = new JFrame("Kundenverwaltung");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new BorderLayout());

        JPanel panel = new JPanel(new GridLayout(6, 2, 5, 5));
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

        frame.add(panel, BorderLayout.CENTER);
        frame.setVisible(true);

        // Datenbank und Tabelle anlegen
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

                // Validierung
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
                // Daten speichern
                insertKunde(vorname, nachname, adresse, plz, kundennummer);
                JOptionPane.showMessageDialog(frame, "Kunde gespeichert!");
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
        try (Connection conn = DriverManager.getConnection(DB_URL); Statement stmt = conn.createStatement()) {
            stmt.executeUpdate(
                    "CREATE TABLE Kunden (Vorname VARCHAR(255), Nachname VARCHAR(255), Adresse VARCHAR(255), PLZ VARCHAR(255), Kundennummer INT)");
        } catch (SQLException e) {
            // Tabelle existiert evtl. schon
        }
    }

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
