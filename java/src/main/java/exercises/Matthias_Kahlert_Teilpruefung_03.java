import java.util.Scanner;

/* 
Aufgabe
Entwickle ein Java-Programm, das die Rolle eines einfachen Quiz-Spiels übernimmt. 
Das Programm soll fünf Fragen zu allgemeinem Wissen stellen, 
wobei jede Frage vier Antwortmöglichkeiten hat (A, B, C, D). 
Der Benutzer gibt die Antwort als Buchstaben ein, und das Programm gibt an, 
ob die Antwort richtig oder falsch ist. 
Nachdem alle Fragen beantwortet wurden, soll das Programm die Anzahl der korrekten Antworten anzeigen 
und eine Bewertung ausgeben: 

"Ausgezeichnet" für 5 richtige Antworten, 
"Sehr gut" für 4 richtige, 
"Gut" für 3 richtige, 
"Ausreichend" für 2 richtige und 
"Versuchen Sie es noch einmal" für 1 oder 0 richtige Antworten. 

Verwende if-else Verzweigungen, um die Logik für die Bewertung und die Antwortüberprüfung zu implementieren.
*/

public class Matthias_Kahlert_Teilpruefung_03 {

    // Vergleicht die Benutzereingabe mit der richtigen Antwort

    public static boolean istAntwortRichtig(String eingabe, String richtigeAntwort) {
        return eingabe.equalsIgnoreCase(richtigeAntwort); // (Groß-/Kleinschreibung wird ignoriert)
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Nutzereingaben lesen
        int richtigeAntworten = 0; // Zählt die Anzahl der korrekten Antworten

        System.out.println("=== Quiz-Spiel ===");
        System.out.println("Bitte geben Sie bei jeder Frage A, B, C oder D ein.");
        System.out.println();

        // Frage 1
        System.out.println("Frage 1: Was ist die Hauptstadt von Deutschland?");
        System.out.println("A) München");
        System.out.println("B) Berlin");
        System.out.println("C) Hamburg");
        System.out.println("D) Köln");
        System.out.print("Ihre Antwort: ");
        String antwort1 = scanner.nextLine();

        if (istAntwortRichtig(antwort1, "B")) {
            System.out.println("Richtig!");
            richtigeAntworten++;
        } else {
            System.out.println("Falsch! Richtige Antwort: B");
        }
        System.out.println();

        // Frage 2
        System.out.println("Frage 2: Welcher Planet wird als roter Planet bezeichnet?");
        System.out.println("A) Venus");
        System.out.println("B) Jupiter");
        System.out.println("C) Mars");
        System.out.println("D) Saturn");
        System.out.print("Ihre Antwort: ");
        String antwort2 = scanner.nextLine();

        if (istAntwortRichtig(antwort2, "C")) {
            System.out.println("Richtig!");
            richtigeAntworten++;
        } else {
            System.out.println("Falsch! Richtige Antwort: C");
        }
        System.out.println();

        // Frage 3
        System.out.println("Frage 3: Wie viele Kontinente gibt es auf der Erde?");
        System.out.println("A) 5");
        System.out.println("B) 6");
        System.out.println("C) 7");
        System.out.println("D) 8");
        System.out.print("Ihre Antwort: ");
        String antwort3 = scanner.nextLine();

        if (istAntwortRichtig(antwort3, "C")) {
            System.out.println("Richtig!");
            richtigeAntworten++;
        } else {
            System.out.println("Falsch! Richtige Antwort: C");
        }
        System.out.println();

        // Frage 4
        System.out.println("Frage 4: In welchem Jahr begann der Erste Weltkrieg?");
        System.out.println("A) 1914");
        System.out.println("B) 1918");
        System.out.println("C) 1939");
        System.out.println("D) 1945");
        System.out.print("Ihre Antwort: ");
        String antwort4 = scanner.nextLine();

        if (istAntwortRichtig(antwort4, "A")) {
            System.out.println("Richtig!");
            richtigeAntworten++;
        } else {
            System.out.println("Falsch! Richtige Antwort: A");
        }
        System.out.println();

        // Frage 5
        System.out.println("Frage 5: Welches Element hat das chemische Symbol O?");
        System.out.println("A) Gold");
        System.out.println("B) Sauerstoff");
        System.out.println("C) Silber");
        System.out.println("D) Wasserstoff");
        System.out.print("Ihre Antwort: ");
        String antwort5 = scanner.nextLine();

        if (istAntwortRichtig(antwort5, "B")) {
            System.out.println("Richtig!");
            richtigeAntworten++;
        } else {
            System.out.println("Falsch! Richtige Antwort: B");
        }
        System.out.println();

        System.out.println("Sie haben " + richtigeAntworten + " von 5 Fragen richtig beantwortet.");

        // Bewertung anhand der Anzahl richtiger Antworten ausgeben
        if (richtigeAntworten == 5) {
            System.out.println("Bewertung: Ausgezeichnet");
        } else if (richtigeAntworten == 4) {
            System.out.println("Bewertung: Sehr gut");
        } else if (richtigeAntworten == 3) {
            System.out.println("Bewertung: Gut");
        } else if (richtigeAntworten == 2) {
            System.out.println("Bewertung: Ausreichend");
        } else {
            // Gilt für 0 oder 1 richtige Antwort
            System.out.println("Bewertung: Versuchen Sie es noch einmal");
        }

        scanner.close(); // Scanner schließen, da er nicht mehr benötigt wird
    }
}
