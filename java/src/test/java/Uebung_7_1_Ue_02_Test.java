import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Uebung_7_1_Ue_02_Test {

    @Test
    public void testProduktHinzufuegen() {
        Uebung_7_1_Ue_02 uebung = new Uebung_7_1_Ue_02();
        Uebung_7_1_Ue_02.Produkt[] lager = new Uebung_7_1_Ue_02.Produkt[10];

        uebung.produktHinzufuegen(lager, "Apfel", 50);
        assertNotNull(lager[0]);
        assertEquals("Apfel", lager[0].name);
        assertEquals(50, lager[0].menge);

        uebung.produktHinzufuegen(lager, "Apfel", 20);
        assertEquals(70, lager[0].menge);
    }

    @Test
    public void testProduktEntfernen() {
        Uebung_7_1_Ue_02 uebung = new Uebung_7_1_Ue_02();
        Uebung_7_1_Ue_02.Produkt[] lager = new Uebung_7_1_Ue_02.Produkt[10];

        lager[0] = uebung.new Produkt("Apfel", 50);
        uebung.produktEntfernen(lager, "Apfel");
        assertNull(lager[0]);

        uebung.produktEntfernen(lager, "Birne"); // Produkt nicht vorhanden
    }

    @Test
    public void testLagerBestandAnzeigen() {
        Uebung_7_1_Ue_02 uebung = new Uebung_7_1_Ue_02();
        Uebung_7_1_Ue_02.Produkt[] lager = new Uebung_7_1_Ue_02.Produkt[10];

        lager[0] = uebung.new Produkt("Apfel", 50);
        lager[1] = uebung.new Produkt("Birne", 30);

        // Lagerbestand anzeigen sollte keine Fehler werfen
        uebung.lagerBestandAnzeigen(lager);
    }
}