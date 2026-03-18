package personenverwaltung;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.AbstractTableModel;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.JTableHeader;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONArray;
import org.json.JSONObject;
// FlatLaf Dependency (Maven):
// <dependency>
//     <groupId>com.formdev</groupId>
//     <artifactId>flatlaf</artifactId>
//     <version>3.4</version>
// </dependency>
import com.formdev.flatlaf.FlatDarkLaf;
import com.formdev.flatlaf.FlatLightLaf;

public class ModerneIPersonenverwaltung {
    private static List<Person> personenListe = new ArrayList<>();
    private static PersonenTableModel tableModel;
    private static JFrame frame;
    private static boolean isDarkMode = true;

    // Moderne Farbpalette 2026
    private static final Color ACCENT_COLOR = new Color(99, 102, 241); // Indigo
    private static final Color ACCENT_HOVER = new Color(129, 140, 248);
    private static final Color SUCCESS_COLOR = new Color(34, 197, 94);
    private static final Color DANGER_COLOR = new Color(239, 68, 68);

    public static void main(String[] args) {
        // FlatLaf initialisieren
        FlatDarkLaf.setup();
        UIManager.put("Button.arc", 12);
        UIManager.put("Component.arc", 12);
        UIManager.put("TextComponent.arc", 12);
        UIManager.put("ScrollBar.thumbArc", 999);
        UIManager.put("ScrollBar.thumbInsets", new Insets(2, 2, 2, 2));

        SwingUtilities.invokeLater(() -> createAndShowGUI());
    }

    private static void createAndShowGUI() {
        frame = new JFrame();
        frame.setUndecorated(false);
        frame.setTitle("Personenverwaltung");
        frame.setSize(1200, 800);
        frame.setMinimumSize(new Dimension(800, 600));
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout(0, 0));
        // Header Panel
        JPanel headerPanel = createHeaderPanel();
        frame.add(headerPanel, BorderLayout.NORTH);
        // Main Content
        JPanel contentPanel = createContentPanel();
        frame.add(contentPanel, BorderLayout.CENTER);
        // Status Bar
        JPanel statusBar = createStatusBar();
        frame.add(statusBar, BorderLayout.SOUTH);
        frame.setVisible(true);
    }

    private static JPanel createHeaderPanel() {
        JPanel header = new JPanel(new BorderLayout());
        header.setBorder(new EmptyBorder(20, 30, 20, 30));
        header.setOpaque(false);
        // Linke Seite: Titel
        JPanel titlePanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 0, 0));
        titlePanel.setOpaque(false);

        JLabel iconLabel = new JLabel("👥");
        iconLabel.setFont(new Font("Segoe UI Emoji", Font.PLAIN, 28));

        JLabel titleLabel = new JLabel("  Personenverwaltung");
        titleLabel.setFont(new Font("Segoe UI", Font.BOLD, 24));

        JLabel subtitleLabel = new JLabel("    v2026.1");
        subtitleLabel.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        subtitleLabel.setForeground(Color.GRAY);

        titlePanel.add(iconLabel);
        titlePanel.add(titleLabel);
        titlePanel.add(subtitleLabel);
        // Rechte Seite: Buttons
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT, 12, 0));
        buttonPanel.setOpaque(false);
        File defaultDir = new File(System.getProperty("user.home"),
                "repositories/learning-journey/java/src/main/java/exercises/personenverwaltung");
        final JFileChooser fc = new JFileChooser(defaultDir);
        JButton addButton = createStyledButton("➕ Hinzufügen", ACCENT_COLOR, ACCENT_HOVER);
        addButton.addActionListener(e -> addNewPerson());
        JButton deleteButton = createStyledButton("🗑️ Löschen", DANGER_COLOR, DANGER_COLOR.brighter());
        deleteButton.addActionListener(e -> deleteSelectedPerson());
        JButton loadButton = createStyledButton("📂 Laden", null, null);
        loadButton.addActionListener(e -> loadData(fc));
        JButton saveButton = createStyledButton("💾 Speichern", SUCCESS_COLOR, SUCCESS_COLOR.brighter());
        saveButton.addActionListener(e -> saveData(fc));
        JButton themeToggle = createIconButton(isDarkMode ? "☀️" : "🌙");
        themeToggle.setToolTipText("Theme wechseln");
        themeToggle.addActionListener(e -> toggleTheme(themeToggle));
        buttonPanel.add(addButton);
        buttonPanel.add(deleteButton);
        buttonPanel.add(Box.createHorizontalStrut(20));
        buttonPanel.add(loadButton);
        buttonPanel.add(saveButton);
        buttonPanel.add(Box.createHorizontalStrut(10));
        buttonPanel.add(themeToggle);
        header.add(titlePanel, BorderLayout.WEST);
        header.add(buttonPanel, BorderLayout.EAST);
        return header;
    }

    private static JButton createStyledButton(String text, Color bgColor, Color hoverColor) {
        JButton button = new JButton(text);
        button.setFont(new Font("Segoe UI", Font.BOLD, 13));
        button.setFocusPainted(false);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));
        button.setBorder(new EmptyBorder(10, 20, 10, 20));

        if (bgColor != null) {
            button.setBackground(bgColor);
            button.setForeground(Color.WHITE);
            button.addMouseListener(new MouseAdapter() {
                public void mouseEntered(MouseEvent e) {
                    button.setBackground(hoverColor);
                }

                public void mouseExited(MouseEvent e) {
                    button.setBackground(bgColor);
                }
            });
        }

        return button;
    }

    private static JButton createIconButton(String emoji) {
        JButton button = new JButton(emoji);
        button.setFont(new Font("Segoe UI Emoji", Font.PLAIN, 18));
        button.setFocusPainted(false);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));
        button.setBorder(new EmptyBorder(8, 12, 8, 12));
        return button;
    }

    private static JPanel createContentPanel() {
        JPanel content = new JPanel(new BorderLayout());
        content.setBorder(new EmptyBorder(0, 30, 20, 30));
        content.setOpaque(false);
        // Suchleiste
        JPanel searchPanel = new JPanel(new BorderLayout());
        searchPanel.setOpaque(false);
        searchPanel.setBorder(new EmptyBorder(0, 0, 15, 0));

        JTextField searchField = new JTextField();
        searchField.putClientProperty("JTextField.placeholderText", "🔍 Personen durchsuchen...");
        searchField.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        searchField.setBorder(BorderFactory.createCompoundBorder(
                searchField.getBorder(),
                new EmptyBorder(12, 15, 12, 15)));
        searchPanel.add(searchField, BorderLayout.CENTER);
        // Tabelle
        tableModel = new PersonenTableModel(personenListe);
        JTable table = new JTable(tableModel);
        styleTable(table);

        JScrollPane scrollPane = new JScrollPane(table);
        scrollPane.setBorder(BorderFactory.createEmptyBorder());
        scrollPane.getViewport().setBackground(table.getBackground());
        content.add(searchPanel, BorderLayout.NORTH);
        content.add(scrollPane, BorderLayout.CENTER);
        return content;
    }

    private static void styleTable(JTable table) {
        table.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        table.setRowHeight(48);
        table.setShowGrid(false);
        table.setIntercellSpacing(new Dimension(0, 0));
        table.setSelectionBackground(ACCENT_COLOR.darker());
        table.setSelectionForeground(Color.WHITE);
        table.setFillsViewportHeight(true);
        // Header Styling
        JTableHeader header = table.getTableHeader();
        header.setFont(new Font("Segoe UI", Font.BOLD, 13));
        header.setPreferredSize(new Dimension(header.getPreferredSize().width, 50));
        header.setBorder(BorderFactory.createMatteBorder(0, 0, 1, 0, Color.GRAY));
        // Zellen-Renderer für alternierenden Hintergrund
        table.setDefaultRenderer(Object.class, new DefaultTableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                    boolean isSelected, boolean hasFocus, int row, int column) {
                Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                setBorder(new EmptyBorder(0, 15, 0, 15));

                if (!isSelected) {
                    if (row % 2 == 0) {
                        c.setBackground(table.getBackground());
                    } else {
                        c.setBackground(new Color(
                                table.getBackground().getRed() + (isDarkMode ? 10 : -10),
                                table.getBackground().getGreen() + (isDarkMode ? 10 : -10),
                                table.getBackground().getBlue() + (isDarkMode ? 10 : -10)));
                    }
                }
                return c;
            }
        });
    }

    private static JPanel createStatusBar() {
        JPanel statusBar = new JPanel(new BorderLayout());
        statusBar.setBorder(new EmptyBorder(10, 30, 15, 30));
        statusBar.setOpaque(false);
        JLabel statusLabel = new JLabel("✓ Bereit");
        statusLabel.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        statusLabel.setForeground(Color.GRAY);
        JLabel countLabel = new JLabel("0 Einträge");
        countLabel.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        countLabel.setForeground(Color.GRAY);
        // Update count when table changes
        tableModel.addTableModelListener(e -> countLabel.setText(personenListe.size() + " Einträge"));
        statusBar.add(statusLabel, BorderLayout.WEST);
        statusBar.add(countLabel, BorderLayout.EAST);
        return statusBar;
    }

    private static void toggleTheme(JButton button) {
        isDarkMode = !isDarkMode;
        try {
            if (isDarkMode) {
                UIManager.setLookAndFeel(new FlatDarkLaf());
                button.setText("☀️");
            } else {
                UIManager.setLookAndFeel(new FlatLightLaf());
                button.setText("🌙");
            }
            SwingUtilities.updateComponentTreeUI(frame);
        } catch (UnsupportedLookAndFeelException e) {
            e.printStackTrace();
        }
    }

    private static void addNewPerson() {
        personenListe.add(new Person("Neu", "Person", "Musterstraße", 1, "12345", "Musterstadt"));
        tableModel.fireTableDataChanged();
        showToast("Person hinzugefügt", SUCCESS_COLOR);
    }

    private static void deleteSelectedPerson() {
        // Implementierung für Löschen
        if (personenListe.size() > 0) {
            personenListe.remove(personenListe.size() - 1);
            tableModel.fireTableDataChanged();
            showToast("Person gelöscht", DANGER_COLOR);
        }
    }

    private static void showToast(String message, Color color) {
        JWindow toast = new JWindow(frame);
        JPanel panel = new JPanel();
        panel.setBackground(color);
        panel.setBorder(new EmptyBorder(12, 24, 12, 24));

        JLabel label = new JLabel(message);
        label.setFont(new Font("Segoe UI", Font.BOLD, 13));
        label.setForeground(Color.WHITE);
        panel.add(label);

        toast.add(panel);
        toast.pack();
        toast.setLocation(
                frame.getX() + frame.getWidth() / 2 - toast.getWidth() / 2,
                frame.getY() + frame.getHeight() - 100);
        toast.setVisible(true);

        new Timer(2000, e -> toast.dispose()).start();
    }

    private static void loadData(JFileChooser fc) {
        int returnVal = fc.showOpenDialog(frame);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            try {
                String text = new String(Files.readAllBytes(fc.getSelectedFile().toPath()), StandardCharsets.UTF_8);
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
                showToast("Daten erfolgreich geladen!", SUCCESS_COLOR);
            } catch (IOException ex) {
                showToast("Fehler beim Laden!", DANGER_COLOR);
            }
        }
    }

    private static void saveData(JFileChooser fc) {
        int returnVal = fc.showSaveDialog(frame);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            if (fc.getSelectedFile().exists()) {
                int result = JOptionPane.showConfirmDialog(frame,
                        "Datei existiert bereits. Überschreiben?", "Bestätigung",
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
                showToast("Erfolgreich gespeichert!", SUCCESS_COLOR);
            } catch (IOException ex) {
                showToast("Fehler beim Speichern!", DANGER_COLOR);
            }
        }
    }

    // Person und PersonenTableModel bleiben identisch zum Original
    static class Person {
        private String vorname, nachname, strasse, plz, ort;
        private int hausnummer;

        public Person(String vorname, String nachname, String strasse, int hausnummer, String plz, String ort) {
            this.vorname = vorname;
            this.nachname = nachname;
            this.strasse = strasse;
            this.hausnummer = hausnummer;
            this.plz = plz;
            this.ort = ort;
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

    static class PersonenTableModel extends AbstractTableModel {
        private final List<Person> personenListe;
        private final String[] columns = { "Vorname", "Nachname", "Straße", "Nr.", "PLZ", "Ort" };

        public PersonenTableModel(List<Person> liste) {
            this.personenListe = liste;
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
        public String getColumnName(int col) {
            return columns[col];
        }

        @Override
        public boolean isCellEditable(int r, int c) {
            return true;
        }

        @Override
        public Object getValueAt(int row, int col) {
            Person p = personenListe.get(row);
            return switch (col) {
                case 0 -> p.getVorname();
                case 1 -> p.getNachname();
                case 2 -> p.getStrasse();
                case 3 -> p.getHausnummer();
                case 4 -> p.getPlz();
                case 5 -> p.getOrt();
                default -> null;
            };
        }

        @Override
        public void setValueAt(Object value, int row, int col) {
            Person p = personenListe.get(row);
            switch (col) {
                case 0 -> p.setVorname(value.toString());
                case 1 -> p.setNachname(value.toString());
                case 2 -> p.setStrasse(value.toString());
                case 3 -> p.setHausnummer(Integer.parseInt(value.toString()));
                case 4 -> p.setPlz(value.toString());
                case 5 -> p.setOrt(value.toString());
            }
            fireTableCellUpdated(row, col);
        }
    }
}