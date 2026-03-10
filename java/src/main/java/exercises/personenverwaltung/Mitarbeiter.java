package personenverwaltung;

public class Mitarbeiter extends Person {
    int gehalt;

    public String ganzerName() {
        return vorname + " " + nachname;
    }

    public Mitarbeiter(String vorname, String nachname, String strasse, int hausnummer, String plz, String ort,
            int gehalt) {
        super(vorname, nachname, strasse, hausnummer, plz, ort);
        this.gehalt = gehalt;
    }
}
