/* 
Beschreibe, wie ein Data Race in einem Java-Programm entstehen kann und erkläre, wie das Konzept der Locks dazu verwendet werden kann, um solche Data Races zu verhindern. Gehe dabei auf folgende Punkte ein:

a) Definiere, was ein Thread in Java ist und wie Threads generell gestartet werden.

b) Erkläre, was ein Data Race ist und unter welchen Umständen es in einem Java-Programm auftreten kann.

c) Beschreibe, wie das Schlüsselwort synchronized und das Konzept der Locks in Java dazu beitragen können, Data Races zu vermeiden.

d) Entwickle ein einfaches Beispiel, in dem zwei Threads auf eine gemeinsame Variable zugreifen und ein Data Race verursachen könnten. 
Verwende dann Locks, um das Problem zu lösen, und zeige den Code vor und nach der Anwendung der Locks.
*/

/*
a) Ein Thread ist ein Ausführungsstrang innerhalb eines Programms.
   Mehrere Threads können gleichzeitig (also parallel) laufen und teilen sich den gleichen Speicher.
   In Java kann man Threads auf zwei Arten starten:
   - Eine Klasse von Thread erben und run() überschreiben
   - Das Interface Runnable implementieren und an ein Thread-Objekt übergeben
   Gestartet wird ein Thread immer mit .start(), nicht mit .run() direkt,
   da .start() einen neuen Ausführungsstrang erzeugt, während .run() nur die Methode im aktuellen Thread aufruft.

b) Ein Data Race entsteht, wenn zwei oder mehr Threads gleichzeitig auf eine gemeinsame Variable zugreifen
   und mindestens einer davon schreibend zugreift, ohne dass der Zugriff synchronisiert ist.
   Das Problem: Die Reihenfolge der Zugriffe ist nicht vorhersagbar (Race Condition).
   Beispiel: Zwei Threads erhöhen gleichzeitig einen Zähler um 1.
   Beide lesen den Wert 5, beide schreiben 6 zurück → eine Erhöhung geht verloren.

c) Die Schlüsselwörter synchronized und Locks. 
Die Schlüsselwörter synchronized und Locks sorgen dafür, dass immer nur ein Thread gleichzeitig auf einen
   kritischen Codeabschnitt zugreifen kann. Die anderen Threads müssen warten.

   - synchronized: Ein Schlüsselwort, das automatisch eine Methode oder einen Block sperrt.
   Nutzt das Lock des Objekts. Ist einfacher aber unflexibler.
   - Lock (z.B. ReentrantLock): Explizites Lock-Objekt aus java.util.concurrent.locks.
   Bietet manuelle Methoden wie tryLock() ""Ist die Ressource frei? Wenn nicht, warte ich nicht, sondern mache was anderes." 
   oder lockInterruptibly() "Ich warte, aber wenn mich jemand unterbricht, höre ich auf zu warten." mehr Kontrolle als synchronized.
   Beide Mechanismen verhindern, dass mehrere Threads gleichzeitig auf die kritische Variable zugreifen,
   wodurch Data Races verhindert werden.
*/

import java.util.concurrent.locks.ReentrantLock;

public class Uebung_12_4_A_01 {

    // d) Gemeinsame Variable, auf die beide Threads zugreifen
    static int zaehlerOhneLock = 0;
    static int zaehlerMitLock = 0;

    // Lock-Objekt, das den Zugriff auf zaehlerMitLock schützt
    static ReentrantLock lock = new ReentrantLock();

    public static void main(String[] args) throws InterruptedException {

        // === OHNE LOCK (Data Race möglich) ===
        System.out.println("=== Ohne Lock (Data Race) ===");

        // Zwei Threads, die jeweils 100000 mal den Zähler erhöhen
        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 100000; i++) {
                zaehlerOhneLock++; // nicht synchronisiert, Data Race möglich
            }
        });

        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 100000; i++) {
                zaehlerOhneLock++; // gleicher Zähler, gleicher Fehler
            }
        });

        thread1.start(); // Thread starten, nicht .run()!
        thread2.start();

        // .join() wartet, bis der Thread fertig ist, damit wir danach das Ergebnis
        // lesen können
        thread1.join();
        thread2.join();

        // Ergebnis sollte 200000 sein, ist aber oft weniger wegen Data Race
        System.out.println("Erwarteter Wert: 200000");
        System.out.println("Tatsächlicher Wert des Zählers ohne Lock: " + zaehlerOhneLock);
        System.out.println();

        // === MIT LOCK (kein Data Race) ===
        System.out.println("=== Mit Lock (sicher) ===");

        Thread thread3 = new Thread(() -> {
            for (int i = 0; i < 100000; i++) {
                lock.lock(); // Lock holen, andere Threads müssen warten
                try {
                    zaehlerMitLock++;
                } finally {
                    lock.unlock(); // Lock immer im finally freigeben, damit es auch bei Fehlern freigegeben wird
                }
            }
        });

        Thread thread4 = new Thread(() -> {
            for (int i = 0; i < 100000; i++) {
                lock.lock();
                try {
                    zaehlerMitLock++;
                } finally {
                    lock.unlock();
                }
            }
        });

        thread3.start();
        thread4.start();

        thread3.join();
        thread4.join();

        // Mit Lock ist das Ergebnis immer korrekt 200000
        System.out.println("Erwarteter Wert: 200000");
        System.out.println("Tatsächlicher Wert des Zählers mit Lock: " + zaehlerMitLock);
    }

    /*
    Ausgabe: 
    Erwarteter Wert: 200000
    Tatsächlicher Wert des Zählers ohne Lock: 136601

    === Mit Lock (sicher) ===
    Erwarteter Wert: 200000
    Tatsächlicher Wert des Zählers mit Lock: 200000 */
}
