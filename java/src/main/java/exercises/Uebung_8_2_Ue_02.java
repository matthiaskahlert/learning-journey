
/* 
Du sollst ein Java-Programm schreiben, das ein Array von Strings (Wörter) einliest 
und diese Wörter in Zahlen umwandelt. 
Dabei soll für jedes Wort geprüft werden, ob es sich in eine ganze Zahl umwandeln lässt. 
Falls die Umwandlung nicht möglich ist, soll eine eigene Fehlermeldung ausgegeben 
und der Nutzer aufgefordert werden, eine neue Eingabe zu tätigen. 
Dies soll so lange wiederholt werden, bis ein gültiges Wort eingegeben wird, 
das sich in eine Zahl umwandeln lässt. Verwende dazu eine Schleife und einen try-catch-Block. 
Nach erfolgreicher Umwandlung soll die Zahl in einem Integer-Array gespeichert werden. 
Am Ende des Programms soll das Integer-Array ausgegeben werden. 
Achte darauf, dass das Programm auch dann korrekt terminiert, 
wenn der Nutzer die Eingabe von Wörtern mit dem Befehl "ende" beendet.

a) Implementiere die Eingabe der Wörter in einer Schleife. Verwende einen Scanner, um die Eingaben des Nutzers zu lesen.

b) Verwende einen try-catch-Block, um die Umwandlung der Wörter in Zahlen zu handhaben. Gib eine verständliche Fehlermeldung aus, wenn die Umwandlung nicht möglich ist, und fordere den Nutzer auf, eine neue Eingabe zu tätigen.

c) Speichere die umgewandelten Zahlen in einem Integer-Array und gib dieses Array am Ende des Programms aus.

d) Implementiere eine Möglichkeit für den Nutzer, die Eingabe mit dem Befehl "ende" zu beenden. Verwende dazu eine entsprechende Verzweigung.
*/
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;

public class Uebung_8_2_Ue_02 {
    private static final Map<String, Integer> zahlwoerter = new HashMap<>();

    static {
        zahlwoerter.put("null", 0);
        zahlwoerter.put("eins", 1);
        zahlwoerter.put("zwei", 2);
        zahlwoerter.put("drei", 3);
        zahlwoerter.put("vier", 4);
        zahlwoerter.put("fünf", 5);
        zahlwoerter.put("sechs", 6);
        zahlwoerter.put("sieben", 7);
        zahlwoerter.put("acht", 8);
        zahlwoerter.put("neun", 9);
        zahlwoerter.put("zehn", 10);
        zahlwoerter.put("elf", 11);
        zahlwoerter.put("zwölf", 12);
        zahlwoerter.put("dreizehn", 13);
        zahlwoerter.put("vierzehn", 14);
        zahlwoerter.put("fünfzehn", 15);
        zahlwoerter.put("sechzehn", 16);
        zahlwoerter.put("siebzehn", 17);
        zahlwoerter.put("achtzehn", 18);
        zahlwoerter.put("neunzehn", 19);
        zahlwoerter.put("zwanzig", 20);
        zahlwoerter.put("einundzwanzig", 21);
        zahlwoerter.put("zweiundzwanzig", 22);
        zahlwoerter.put("dreiundzwanzig", 23);
        zahlwoerter.put("vierundzwanzig", 24);
        zahlwoerter.put("fünfundzwanzig", 25);
        zahlwoerter.put("sechsundzwanzig", 26);
        zahlwoerter.put("siebenundzwanzig", 27);
        zahlwoerter.put("achtundzwanzig", 28);
        zahlwoerter.put("neunundzwanzig", 29);
        zahlwoerter.put("dreißig", 30);
        zahlwoerter.put("einunddreißig", 31);
        zahlwoerter.put("zweiunddreißig", 32);
        zahlwoerter.put("dreiunddreißig", 33);
        zahlwoerter.put("vierunddreißig", 34);
        zahlwoerter.put("fünfunddreißig", 35);
        zahlwoerter.put("sechsunddreißig", 36);
        zahlwoerter.put("siebenunddreißig", 37);
        zahlwoerter.put("achtunddreißig", 38);
        zahlwoerter.put("neununddreißig", 39);
        zahlwoerter.put("vierzig", 40);
        zahlwoerter.put("einundvierzig", 41);
        zahlwoerter.put("zweiundvierzig", 42);
        zahlwoerter.put("dreiundvierzig", 43);
        zahlwoerter.put("vierundvierzig", 44);
        zahlwoerter.put("fünfundvierzig", 45);
        zahlwoerter.put("sechsundvierzig", 46);
        zahlwoerter.put("siebenundvierzig", 47);
        zahlwoerter.put("achtundvierzig", 48);
        zahlwoerter.put("neunundvierzig", 49);
        zahlwoerter.put("fünfzig", 50);
        zahlwoerter.put("einundfünfzig", 51);
        zahlwoerter.put("zweiundfünfzig", 52);
        zahlwoerter.put("dreiundfünfzig", 53);
        zahlwoerter.put("vierundfünfzig", 54);
        zahlwoerter.put("fünfundfünfzig", 55);
        zahlwoerter.put("sechsundfünfzig", 56);
        zahlwoerter.put("siebenundfünfzig", 57);
        zahlwoerter.put("achtundfünfzig", 58);
        zahlwoerter.put("neunundfünfzig", 59);
        zahlwoerter.put("sechzig", 60);
        zahlwoerter.put("einundsechzig", 61);
        zahlwoerter.put("zweiundsechzig", 62);
        zahlwoerter.put("dreiundsechzig", 63);
        zahlwoerter.put("vierundsechzig", 64);
        zahlwoerter.put("fünfundsechzig", 65);
        zahlwoerter.put("sechsundsechzig", 66);
        zahlwoerter.put("siebenundsechzig", 67);
        zahlwoerter.put("achtundsechzig", 68);
        zahlwoerter.put("neunundsechzig", 69);
        zahlwoerter.put("siebzig", 70);
        zahlwoerter.put("einundsiebzig", 71);
        zahlwoerter.put("zweiundsiebzig", 72);
        zahlwoerter.put("dreiundsiebzig", 73);
        zahlwoerter.put("vierundsiebzig", 74);
        zahlwoerter.put("fünfundsiebzig", 75);
        zahlwoerter.put("sechsundsiebzig", 76);
        zahlwoerter.put("siebenundsiebzig", 77);
        zahlwoerter.put("achtundsiebzig", 78);
        zahlwoerter.put("neunundsiebzig", 79);
        zahlwoerter.put("achtzig", 80);
        zahlwoerter.put("einundachtzig", 81);
        zahlwoerter.put("zweiundachtzig", 82);
        zahlwoerter.put("dreiundachtzig", 83);
        zahlwoerter.put("vierundachtzig", 84);
        zahlwoerter.put("fünfundachtzig", 85);
        zahlwoerter.put("sechsundachtzig", 86);
        zahlwoerter.put("siebenundachtzig", 87);
        zahlwoerter.put("achtundachtzig", 88);
        zahlwoerter.put("neunundachtzig", 89);
        zahlwoerter.put("neunzig", 90);
        zahlwoerter.put("einundneunzig", 91);
        zahlwoerter.put("zweiundneunzig", 92);
        zahlwoerter.put("dreiundneunzig", 93);
        zahlwoerter.put("vierundneunzig", 94);
        zahlwoerter.put("fünfundneunzig", 95);
        zahlwoerter.put("sechsundneunzig", 96);
        zahlwoerter.put("siebenundneunzig", 97);
        zahlwoerter.put("achtundneunzig", 98);
        zahlwoerter.put("neunundneunzig", 99);
        zahlwoerter.put("hundert", 100);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();
        String input;
        boolean weiterEingeben = true;

        while (weiterEingeben) {
            System.out.print("Geben Sie ein Zahlwort zwischen null und 100 ein (z.B. 'eins', 'zwei', ... oder 'ende' zum Beenden): ");
            input = scanner.next().toLowerCase();

            if ("ende".equals(input)) {
                weiterEingeben = false;
            } else {
                try {
                    int number = convertWortToZahl(input);
                    numbers.add(number);
                    System.out.println("✓ Erfolgreich hinzugefügt: " + input + " = " + number);
                } catch (IllegalArgumentException e) {
                    System.out.println("Ungültige Eingabe: " + e.getMessage());
                }
            }
        }

        System.out.println("\nEingegebene Zahlen:");
        for (int zahl : numbers) {
            System.out.println(zahl);
        }
        scanner.close();
    }

    private static int convertWortToZahl(String wort) {
        if (zahlwoerter.containsKey(wort)) {
            return zahlwoerter.get(wort);
        } else {
            throw new IllegalArgumentException("Das Wort '" + wort + "' ist kein gültiges Zahlwort. "
                    + "Bitte geben Sie ein Zahlwort ein (null bis zehn).");
        }
    }
}
