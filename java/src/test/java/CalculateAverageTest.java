import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculateAverageTest {

    @Test
    public void testCalculateAverage() {
        int[] zahlen = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        float result = CalculateAverage.calculateAverage(zahlen);
        assertEquals(5.5, result, 0.01); // Erwarteter Wert: 5.5
    }

    @Test
    public void testEmptyArray() {
        int[] zahlen = {};
        float result = CalculateAverage.calculateAverage(zahlen);
        assertEquals(-1, result); // Erwarteter Wert: -1 fuer leeres Array
    }
}
