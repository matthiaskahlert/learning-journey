package Caesar;

/**
 * Caesar-Chiffre Verschlüsselung und Entschlüsselung.
 * Implementiert die klassische Caesar-Verschiebung mit Unterstützung für
 * Groß-/Kleinschreibung und Beibehaltung von Nicht-Buchstaben-Zeichen.
 */
public class CaesarCipher {

    private static final int ALPHABET_SIZE = 26;
    private static final char LOWERCASE_START = 'a';
    private static final char UPPERCASE_START = 'A';

    /**
     * Verschlüsselt einen Text mit Caesar-Verschiebung.
     * 
     * @param text  Der zu verschlüsselnde Text
     * @param shift Die Verschiebung (1-25)
     * @return Der verschlüsselte Text
     * @throws IllegalArgumentException wenn shift ungültig ist
     */
    public static String encrypt(String text, int shift) {
        if (!isValidShift(shift)) {
            throw new IllegalArgumentException("Verschiebung muss zwischen 1 und 25 liegen");
        }
        return transform(text, shift);
    }

    /**
     * Entschlüsselt einen Text, der mit Caesar-Verschiebung codiert wurde.
     * 
     * @param text  Der zu entschlüsselnde Text
     * @param shift Die ursprüngliche Verschiebung (1-25)
     * @return Der entschlüsselte Text
     * @throws IllegalArgumentException wenn shift ungültig ist
     */
    public static String decrypt(String text, int shift) {
        if (!isValidShift(shift)) {
            throw new IllegalArgumentException("Verschiebung muss zwischen 1 und 25 liegen");
        }
        // Zum Entschlüsseln: rückwärts verschieben
        int reverseShift = ALPHABET_SIZE - shift;
        return transform(text, reverseShift);
    }

    /**
     * Prüft, ob die Verschiebung gültig ist.
     * 
     * @param shift Die zu prüfende Verschiebung
     * @return true wenn 1 <= shift <= 25
     */
    public static boolean isValidShift(int shift) {
        return shift >= 1 && shift <= 25;
    }

    /**
     * Interne Methode zur Transformation eines Textes mit Verschiebung.
     * Nur alphabetische Zeichen werden verschoben, andere bleiben unverändert.
     * 
     * @param text  Der zu transformierende Text
     * @param shift Die Verschiebung (0-25)
     * @return Der transformierte Text
     */
    private static String transform(String text, int shift) {
        StringBuilder result = new StringBuilder();

        for (char c : text.toCharArray()) {
            if (Character.isUpperCase(c)) {
                // Großbuchstabe: A-Z
                int position = c - UPPERCASE_START;
                int shiftedPosition = (position + shift) % ALPHABET_SIZE;
                char shiftedChar = (char) (UPPERCASE_START + shiftedPosition);
                result.append(shiftedChar);
            } else if (Character.isLowerCase(c)) {
                // Kleinbuchstabe: a-z
                int position = c - LOWERCASE_START;
                int shiftedPosition = (position + shift) % ALPHABET_SIZE;
                char shiftedChar = (char) (LOWERCASE_START + shiftedPosition);
                result.append(shiftedChar);
            } else {
                // Nicht-Buchstaben bleiben unverändert
                result.append(c);
            }
        }

        return result.toString();
    }
}
