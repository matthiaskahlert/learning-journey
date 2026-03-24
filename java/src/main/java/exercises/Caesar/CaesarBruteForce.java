package Caesar;

import java.util.*;
import java.util.concurrent.*;

/**
 * Caesar-Chiffre Brute-Force mit Multithreading.
 * Probiert alle 25 möglichen Verschiebungen parallel mit ExecutorService.
 */
public class CaesarBruteForce {

    private static final int NUM_SHIFTS = 25;
    private static final int THREAD_POOL_SIZE = 25;

    /**
     * Führt Brute-Force auf einem verschlüsselten Text aus.
     * Probiert alle 25 möglichen Verschiebungen parallel.
     * 
     * @param text Der zu analysierte Text
     * @return Map mit Verschiebung → dekodierter Text
     */
    public static Map<Integer, String> bruteForce(String text) {
        ExecutorService executor = Executors.newFixedThreadPool(THREAD_POOL_SIZE);
        List<Future<Map.Entry<Integer, String>>> futures = new ArrayList<>();

        // Alle 25 Verschiebungen als Aufgaben einplanen
        for (int shift = 1; shift <= NUM_SHIFTS; shift++) {
            final int currentShift = shift;

            Future<Map.Entry<Integer, String>> future = executor.submit(() -> {
                String decrypted = CaesarCipher.decrypt(text, currentShift);
                return new AbstractMap.SimpleEntry<>(currentShift, decrypted);
            });

            futures.add(future);
        }

        // Ergebnisse sammeln
        Map<Integer, String> results = new LinkedHashMap<>();
        try {
            // Warte auf alle Threads (max 5 Sekunden)
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                System.err.println("⚠️ Executor hat Timeout überschritten");
                executor.shutdownNow();
            }

            // Ergebnisse aus Futures holen
            for (Future<Map.Entry<Integer, String>> future : futures) {
                try {
                    Map.Entry<Integer, String> entry = future.get();
                    results.put(entry.getKey(), entry.getValue());
                } catch (ExecutionException e) {
                    System.err.println("Fehler bei Thread-Ausführung: " + e.getMessage());
                }
            }
        } catch (InterruptedException e) {
            System.err.println("Brute-Force wurde unterbrochen: " + e.getMessage());
            Thread.currentThread().interrupt();
        } finally {
            executor.shutdown();
        }

        return results;
    }

    /**
     * Formatiert die Brute-Force-Ergebnisse für Ausgabe.
     * 
     * @param results Map der Ergebnisse
     * @return Formatierter String
     */
    public static String formatResults(Map<Integer, String> results) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n").append("=".repeat(60)).append("\n");
        sb.append("🔓 BRUTE-FORCE ERGEBNISSE (25 Verschiebungen)\n");
        sb.append("=".repeat(60)).append("\n");

        for (Map.Entry<Integer, String> entry : results.entrySet()) {
            int shift = entry.getKey();
            String text = entry.getValue();
            sb.append(String.format("Shift %2d: %s\n", shift, text));
        }

        sb.append("=".repeat(60)).append("\n");

        return sb.toString();
    }

    /**
     * Performance-Benchmark für Brute-Force.
     * 
     * @param text Der zu analysierende Text
     */
    public static void benchmark(String text) {
        long startTime = System.currentTimeMillis();
        Map<Integer, String> results = bruteForce(text);
        long endTime = System.currentTimeMillis();

        System.out.println("\n⏱️  Performance-Messung:");
        System.out.println("   Text: \"" + text + "\"");
        System.out.println("   Länge: " + text.length() + " Zeichen");
        System.out.println("   Zeit: " + (endTime - startTime) + " ms");
        System.out.println("   Varianten: " + results.size());
    }
}
