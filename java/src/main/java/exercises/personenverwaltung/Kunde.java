package personenverwaltung;

public class Kunde extends Person {

    public Kunde(String vn, String nn, String str, int nummer, String p, String o) {
        super(vn, nn, str, nummer, p, o);
    }

    public static void main(String[] args) {
        Kunde kunde1 = new Kunde("Max", "Mustermann", "Musterstraße", 1, "12345", "Musterstadt");
        System.out.println("Kunde: " + kunde1.vorname + " " + kunde1.nachname);
        System.out.println("Adresse: " + kunde1.adresse.strasse + " " + kunde1.adresse.getHausnummer() + ", "
                + kunde1.adresse.plz + " " + kunde1.adresse.ort);
    }
}
