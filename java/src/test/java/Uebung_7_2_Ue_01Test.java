import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

public class Uebung_7_2_Ue_01Test {

    @Test
    public void testFilterEvenNumbers() {
        // Arrange
        List<Integer> input = Arrays.asList(1, 2, 3, 4, 5, 6);
        List<Integer> expected = Arrays.asList(2, 4, 6);

        // Act
        List<Integer> result = Uebung_7_2_Ue_01.filterEvenNumbers(input);

        // Assert
        assertEquals(expected, result, "Die Methode sollte nur gerade Zahlen zurückgeben.");
    }

    @Test
    public void testFilterEvenNumbersWithEmptyList() {
        // Arrange
        List<Integer> input = Arrays.asList();
        List<Integer> expected = Arrays.asList();

        // Act
        List<Integer> result = Uebung_7_2_Ue_01.filterEvenNumbers(input);

        // Assert
        assertEquals(expected, result,
                "Die Methode sollte eine leere Liste zurückgeben, wenn die Eingabeliste leer ist.");
    }

    @Test
    public void testFilterEvenNumbersWithNoEvenNumbers() {
        // Arrange
        List<Integer> input = Arrays.asList(1, 3, 5, 7, 9);
        List<Integer> expected = Arrays.asList();

        // Act
        List<Integer> result = Uebung_7_2_Ue_01.filterEvenNumbers(input);

        // Assert
        assertEquals(expected, result,
                "Die Methode sollte eine leere Liste zurückgeben, wenn keine geraden Zahlen vorhanden sind.");
    }

    @Test
    public void testFilterEvenNumbersWithAllEvenNumbers() {
        // Arrange
        List<Integer> input = Arrays.asList(2, 4, 6, 8);
        List<Integer> expected = Arrays.asList(2, 4, 6, 8);

        // Act
        List<Integer> result = Uebung_7_2_Ue_01.filterEvenNumbers(input);

        // Assert
        assertEquals(expected, result,
                "Die Methode sollte alle geraden Zahlen zurückgeben, wenn alle Zahlen gerade sind.");
    }
}