public class Kunde {
    String vorname;
    String nachname;
    String strasse;
    int hausnummer;
    int plz;
    String ort;

    public Kunde(String vn, String nn, String str, int nummer, int p, String o) {
        vorname = vn;
        nachname = nn;
        strasse = str;
        hausnummer = nummer;
        plz = p;
        ort = o;
    }

    public static void main(String[] args) {
        Kunde kunde1 = new Kunde("Max", "Mustermann", "Musterstraße", 1, 12345, "Musterstadt");
        System.out.println("Kunde: " + kunde1.vorname + " " + kunde1.nachname);
        System.out.println("Adresse: " + kunde1.strasse + " " + kunde1.hausnummer + ", " + kunde1.plz + " " + kunde1.ort);
    }
}
