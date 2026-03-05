/* Entwickle ein kleines Programm in Java, das folgende Aufgaben erfüllt:

a) Definiere eine Funktion berechneQuersumme, die als Parameter eine ganze Zahl entgegennimmt 
und die Quersumme dieser Zahl berechnet und zurückgibt. 
Verwende eine while-Schleife, um die Ziffern der Zahl zu durchlaufen und die Quersumme zu berechnen.

b) Definiere eine Funktion istPrimzahl, die als Parameter eine ganze Zahl entgegennimmt 
und mittels einer for-Schleife überprüft, ob es sich um eine Primzahl handelt. 
Die Funktion soll einen booleschen Wert zurückgeben: true, wenn es sich um eine Primzahl handelt, und false andernfalls.

c) Implementiere eine Funktion analysiereZahl, die zwei Parameter entgegennimmt: 
eine ganze Zahl und einen String, der angibt, welche Analyse durchgeführt werden soll ("quersumme" oder "primzahl"). 
Verwende eine switch-case-Verzweigung, um zu entscheiden, welche Funktion aufgerufen werden soll. 
Die Funktion soll das Ergebnis der jeweiligen Analyse als String zurückgeben.

d) Schreibe eine main-Methode, die die Funktion analysiereZahl mit verschiedenen Zahlen und Analyseanforderungen aufruft 
und die Ergebnisse auf der Konsole ausgibt.  */

public class Matthias_Kahlert_Teilpruefung_01 {
    // a) Funktion zur Berechnung der Quersumme
    public static int berechneQuersumme(int zahl) {
        String zahlString = String.valueOf(zahl); // String: 567 → "567"
        String[] ziffern = zahlString.split(""); // Array:["5", "6", "7"]
        int quersumme = 0;
        int i = 0;

        while (i < ziffern.length) {
            quersumme += Integer.parseInt(ziffern[i]); // Ziffer umwandeln und addieren
            i++; // nächste Ziffer bis ziffern.length erreicht ist
        }
        return quersumme;
    }

    // b) Funktion zur überprüfung, ob eine Zahl eine Primzahl ist also größer 1 und
    // nur durch 1 und sich selbst teilbar ist
    public static boolean istPrimzahl(int zahl) {
        if (zahl <= 1) {
            return false; // Zahlen <= 1 sind keine Primzahlen
        }
        for (int i = 2; i <= zahl / 2; i++) {
            if (zahl % i == 0) {
                return false; // Teiler gefunden, es ist demnach keine Primzahl, Schleife läuft weiter
            }
        }
        return true; // Zahl ist eine Primzahl, schleife läuft maximal bis zahl / 2
    }

    // c) Funktion zur Analyse der Zahl
    public static String analysiereZahl(int zahl, String analyse) {
        switch (analyse.toLowerCase()) {
            case "quersumme":
                return "Die Quersumme von " + zahl + " ist: " + berechneQuersumme(zahl);
            case "primzahl":
                return zahl + (istPrimzahl(zahl) ? " ist eine Primzahl." : " ist keine Primzahl.");
            default:
                return "Ungültiger Analysetyp. Bitte 'quersumme' oder 'primzahl' eingeben.";
        }
    }

    public static void main(String[] args) {
        // d) Funktionsaufrufe mit verschiedenen Zahlen und Analyseanforderungen
        System.out.println(analysiereZahl(567, "quersumme"));
        System.out.println(analysiereZahl(666, "primzahl"));
        System.out.println(analysiereZahl(29, "primzahl"));
        System.out.println(analysiereZahl(1337, "quersumme"));
        System.out.println(analysiereZahl(789, "ungültig"));
    }

}
