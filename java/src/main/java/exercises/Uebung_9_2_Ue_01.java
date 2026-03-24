
/* 
Erstelle ein Java-Programm, das folgende Funktionen ausführt:

a) Definiere ein Array von Strings, das mehrere Namen von Studierenden enthält.

b) Schreibe eine Methode speichereNamenInDatei, die das Array entgegennimmt 
und jeden Namen in eine Textdatei namen.txt schreibt. 
Jeder Name soll in einer neuen Zeile stehen. 
Verwende dabei einen BufferedWriter zusammen mit einem FileWriter. 
Achte darauf, dass du Fehler mit einem try-catch-Block behandelst. 
Falls die Datei bereits existiert, soll sie nicht überschrieben, sondern der Inhalt soll angehängt werden.

c) Implementiere eine weitere Methode leseNamenAusDatei, die die Datei namen.txt liest 
und jeden Namen auf der Konsole ausgibt. Verwende dafür einen Scanner.
Behandle auch hier mögliche Fehler mit try-catch.

d) Sorge dafür, dass am Ende des Programms in einem finally-Block überprüft wird, 
ob der BufferedWriter bzw. der Scanner noch offen ist und schließe ihn gegebenenfalls.
*/
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Uebung_9_2_Ue_01 {
    private static final String DATEINAME = "namen.txt";

    public static void speichereNamenInDatei(String[] namen) {
        BufferedWriter writer = null;

        try {
            writer = new BufferedWriter(new FileWriter(DATEINAME, true));
            for (String name : namen) {
                writer.write(name);
                writer.newLine();
            }
            System.out.println("Namen wurden erfolgreich in die Datei geschrieben.");
        } catch (IOException e) {
            System.out.println("Fehler beim Schreiben der Datei: " + e.getMessage());
        } finally {
            if (writer != null) {
                try {
                    writer.close();
                } catch (IOException e) {
                    System.out.println("Fehler beim Schließen des Writers: " + e.getMessage());
                }
            }
        }
    }

    public static void leseNamenAusDatei() {
        Scanner scanner = null;

        try {
            scanner = new Scanner(new File(DATEINAME));
            System.out.println("Namen aus der Datei:");

            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        } catch (IOException e) {
            System.out.println("Fehler beim Lesen der Datei: " + e.getMessage());
        } finally {
            if (scanner != null) {
                scanner.close();
            }
        }
    }

    public static void main(String[] args) {
        String[] studierendenNamen = {
                "Anna",
                "Ben",
                "Clara",
                "David",
                "Elif"
        };

        speichereNamenInDatei(studierendenNamen);
        leseNamenAusDatei();
    }
}
