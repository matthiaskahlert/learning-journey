package personenverwaltung;

public class Adresse {
    String strasse;
    private int hausnummer;
    String plz;
    String ort;

    public Adresse(String strasse, int hausnummer, String plz, String ort) {
        this.strasse = strasse;
        this.hausnummer = hausnummer;
        this.plz = plz;
        this.ort = ort;
    }

    public int getHausnummer() {
        return this.hausnummer;
    }

    public void setHausnummer(int hausnummer) {
        if (hausnummer >= 0) {
            this.hausnummer = hausnummer;
        } else {
            this.hausnummer = 0;
        }
    }
}
