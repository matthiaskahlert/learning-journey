package personenverwaltung;

public class Person {
    String vorname;
    String nachname;
    Adresse adresse;

    public String getVorname() {
        return vorname;
    }

    public void setVorname(String vorname) {
        this.vorname = vorname;
    }

    public String getNachname() {
        return nachname;
    }

    public void setNachname(String nachname) {
        this.nachname = nachname;
    }

    public Adresse getAdresse() {
        return adresse;
    }

    public void setAdresse(Adresse adresse) {
        this.adresse = adresse;
    }

    public String ganzerName() {
        return vorname + " " + nachname;
    }

    public Person(String vorname, String nachname, String strasse, int hausnummer, String plz, String ort) {
        this.vorname = vorname;
        this.nachname = nachname;
        this.adresse = new Adresse(strasse, hausnummer, plz, ort);
    }
}
