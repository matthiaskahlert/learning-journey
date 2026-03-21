import java.util.Scanner;

public class QuizSpiel {

    public static boolean istAntwortRichtig(String eingabe, String richtigeAntwort) {
        if (eingabe.equalsIgnoreCase(richtigeAntwort)) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int richtigeAntworten = 0;

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

        if (richtigeAntworten == 5) {
            System.out.println("Bewertung: Ausgezeichnet");
        } else if (richtigeAntworten == 4) {
            System.out.println("Bewertung: Sehr gut");
        } else if (richtigeAntworten == 3) {
            System.out.println("Bewertung: Gut");
        } else if (richtigeAntworten == 2) {
            System.out.println("Bewertung: Ausreichend");
        } else {
            System.out.println("Bewertung: Versuchen Sie es noch einmal");
        }

        scanner.close();
    }
}