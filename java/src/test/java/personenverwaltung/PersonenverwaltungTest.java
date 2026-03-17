package personenverwaltung;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PersonenverwaltungTest {

    @Test
    void main_runsKundeFlow_withoutException() {
        String input = String.join(System.lineSeparator(),
                "Max",
                "Mustermann",
                "Musterstrasse",
                "12",
                "12345",
                "Berlin",
                "nein",
                "nein") + System.lineSeparator();

        String output = runMainWithInput(input);

        assertTrue(output.contains("Neue Person erfassen"));
        assertTrue(output.contains("Datenerfassung abgeschlossen"));
    }

    @Test
    void main_runsMitarbeiterFlow_withoutException() {
        String input = String.join(System.lineSeparator(),
                "Erika",
                "Musterfrau",
                "Hauptstrasse",
                "7",
                "54321",
                "Hamburg",
                "ja",
                "4200",
                "nein") + System.lineSeparator();

        String output = runMainWithInput(input);

        assertTrue(output.contains("Neue Person erfassen"));
        assertTrue(output.contains("Datenerfassung abgeschlossen"));
    }

    private String runMainWithInput(String input) {
        PrintStream originalOut = System.out;
        java.io.InputStream originalIn = System.in;

        ByteArrayOutputStream capturedOut = new ByteArrayOutputStream();
        ByteArrayInputStream simulatedIn = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));

        try {
            System.setIn(simulatedIn);
            System.setOut(new PrintStream(capturedOut, true, StandardCharsets.UTF_8));

            assertDoesNotThrow(() -> Personenverwaltung.main(new String[0]));
            return capturedOut.toString(StandardCharsets.UTF_8);
        } finally {
            System.setOut(originalOut);
            System.setIn(originalIn);
        }
    }
}
