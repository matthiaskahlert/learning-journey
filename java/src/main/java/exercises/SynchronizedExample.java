public class SynchronizedExample {
    // Die Klasse enthält einen counter, der als gemeinsame ressource dient
    private int counter = 0;

    // Die Methode increment() ist mit dem Schlüsselwort synchronized versehen.
    // Dadurch wird sichergestellt, dass nur ein Thread gleichzeitig auf die Methode zugreifen kann.
    public synchronized void increment() {
        counter++;
    }

    // In der main-Methode wird ein Objekt der Klasse SynchronizedExample erstellt, 
    // das von mehreren Threads gemeinsam genutzt wird.
    public static void main(String[] args) {
        SynchronizedExample example = new SynchronizedExample();
        
        // Ein Runnable-Objekt wird definiert, 
        // das über eine Schleife 1000-mal die Methode increment() aufruft.
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                example.increment();
            }
        };

        // Jeder Thread, der dieses Runnable ausführt, versucht, den counter 1000-mal zu erhöhen.
        // Durch die Synchronisierung wird sichergestellt, dass der counter korrekt erhöht wird.
        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();

        // Die join()-Methode sorgt dafür, dass die main-Methode wartet, 
        // bis beide Threads ihre Arbeit beendet haben.
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Das Endergebnis wird ausgegeben, das aufgrund der Synchronisierung korrekt 2000 ist.
        System.out.println("Endergebnis: " + example.counter); // Endergebnis: 2000
    }
}