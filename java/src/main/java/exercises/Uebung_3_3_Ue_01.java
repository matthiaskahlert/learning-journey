public class Uebung_3_3_Ue_01 {
    public static void main(String[] args) {
        // a) Deklaration und Initialisierung der Variable anzahlSchüler
        int anzahlSchüler = 28;

        // b) Deklaration und Initialisierung der Variable durchschnittsNote
        double durchschnittsNote = 2.7;

        // c) Berechnung der Gesamtanzahl der Notenpunkte
        double gesamtNotenpunkte = anzahlSchüler * durchschnittsNote;

        // d) Erhöhung der Anzahl der Schüler um 2
        anzahlSchüler += 2; // oder anzahlSchüler = anzahlSchüler + 2;

        // e) Ausgabe der aktualisierten Anzahl der Schüler und der Gesamtanzahl der Notenpunkte
        System.out.println("Aktualisierte Anzahl der Schüler: " + anzahlSchüler);
        System.out.println("Gesamtanzahl der Notenpunkte: " + gesamtNotenpunkte);
    }
}
/*
Erstelle ein Java-Programm, das die folgenden Anforderungen erfüllt:

a) Deklariere eine Variable vom Typ int mit dem Namen anzahlSchüler und weise ihr die Anzahl der Schüler in einer Klasse zu. Die Klasse hat 28 Schüler.

b) Deklariere eine Variable vom Typ double mit dem Namen durchschnittsNote und weise ihr die durchschnittliche Note der Klasse zu. Die durchschnittliche Note ist 2.7.

c) Berechne die Gesamtanzahl der Notenpunkte in der Klasse, indem du die Anzahl der Schüler mit der durchschnittlichen Note multiplizierst. Speichere das Ergebnis in einer neuen Variable vom Typ double mit dem Namen gesamtNotenpunkte.

d) Erhöhe die Anzahl der Schüler um 2, da zwei neue Schüler in die Klasse gekommen sind, und aktualisiere die Variable anzahlSchüler entsprechend.

e) Gib die aktualisierte Anzahl der Schüler und die Gesamtanzahl der Notenpunkte auf der Konsole aus.
*/