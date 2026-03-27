/* 
Implementiere eine Java-Klasse PersonService, die eine REST-Schnittstelle für das Verwalten von Personen-Objekten bereitstellt. 
Die Klasse soll Methoden für die HTTP-Methoden GET, POST, PUT und DELETE enthalten, 
die jeweils eine Person anhand ihrer ID abrufen, eine neue Person hinzufügen, 
die Daten einer vorhandenen Person aktualisieren bzw. eine Person löschen. 
Verwende dabei eine lokale HashMap als Datenbank, in der die Person-Objekte gespeichert werden. 
Die Person-Klasse soll die Attribute id, vorname, nachname, adresse haben, 
wobei adresse selbst eine Klasse mit den Attributen strasse, hausnummer, plz und ort ist. 
Implementiere zusätzlich eine einfache Schleife, die alle Personen in der "Datenbank" ausgibt, 
wenn eine spezielle GET-Anfrage ohne ID erfolgt. 
Die REST-Schnittstelle soll mit dem Framework Restlet implementiert werden.
*/

import java.util.HashMap;
import java.util.Map;
import org.restlet.Application;
import org.restlet.Component;
import org.restlet.Restlet;
import org.restlet.data.Protocol;
import org.restlet.resource.Delete;
import org.restlet.resource.Get;
import org.restlet.resource.Post;
import org.restlet.resource.Put;
import org.restlet.resource.ServerResource;
import org.restlet.routing.Router;
import org.json.JSONArray;
import org.json.JSONObject;

public class Uebung_14_4_Ue_01 extends Application {

    // HashMap als In-Memory-Datenbank (static, damit alle Resource-Klassen darauf
    // zugreifen können)
    private static Map<Integer, Person> personenDatenbank = new HashMap<>();
    private static int naechsteId = 1;

    // Zwei Testpersonen beim Start einfügen
    static {
        Adresse a1 = new Adresse("Musterstraße", 1, "12345", "Berlin");
        personenDatenbank.put(naechsteId, new Person(naechsteId++, "Max", "Mustermann", a1));

        Adresse a2 = new Adresse("Beispielweg", 5, "54321", "Hamburg");
        personenDatenbank.put(naechsteId, new Person(naechsteId++, "Erika", "Musterfrau", a2));
    }

    public static void main(String[] args) throws Exception {
        Component component = new Component();
        component.getServers().add(Protocol.HTTP, 8080);
        component.getDefaultHost().attach(new Uebung_14_4_Ue_01());
        component.start();
        System.out.println("PersonService läuft auf http://localhost:8080");
        System.out.println("  GET    /person        -> alle Personen");
        System.out.println("  GET    /person/{id}   -> eine Person");
        System.out.println("  POST   /person        -> neue Person");
        System.out.println("  PUT    /person/{id}   -> Person aktualisieren");
        System.out.println("  DELETE /person/{id}   -> Person löschen");
    }

    @Override
    public Restlet createInboundRoot() {
        Router router = new Router(getContext());
        router.attach("/person", PersonenResource.class); // GET alle, POST
        router.attach("/person/{id}", PersonResource.class); // GET, PUT, DELETE
        return router;
    }

    // -------------------------------------------------------------------------
    // Resource für /person (GET alle + POST)
    // -------------------------------------------------------------------------
    public static class PersonenResource extends ServerResource {

        // GET /person -> alle Personen ausgeben (Schleife über die Datenbank)
        @Get("json")
        public String repraesentiere() {
            JSONArray array = new JSONArray();
            for (Person p : personenDatenbank.values()) {
                array.put(p.toJson());
                System.out.println("Person: " + p.getVorname() + " " + p.getNachname());
            }
            System.out.println("GET alle Personen: " + array.length() + " Einträge.");
            return array.toString();
        }

        // POST /person -> neue Person anlegen
        @Post("json")
        public String akzeptiere(String daten) {
            JSONObject json = new JSONObject(daten);
            JSONObject aj = json.getJSONObject("adresse");
            Adresse adresse = new Adresse(
                    aj.getString("strasse"),
                    aj.getInt("hausnummer"),
                    aj.getString("plz"),
                    aj.getString("ort"));
            Person p = new Person(naechsteId++,
                    json.getString("vorname"),
                    json.getString("nachname"),
                    adresse);
            personenDatenbank.put(p.getId(), p);
            System.out.println("POST: Neue Person -> " + p.getVorname() + " " + p.getNachname());
            return p.toJson().toString();
        }
    }

    // -------------------------------------------------------------------------
    // Resource für /person/{id} (GET eine, PUT, DELETE)
    // -------------------------------------------------------------------------
    public static class PersonResource extends ServerResource {

        // GET /person/{id} -> eine Person abrufen
        @Get("json")
        public String repraesentiere() {
            int id = Integer.parseInt(getAttribute("id"));
            Person p = personenDatenbank.get(id);
            if (p == null) {
                return new JSONObject().put("fehler", "Person " + id + " nicht gefunden").toString();
            }
            System.out.println("GET Person ID " + id + ": " + p.getVorname() + " " + p.getNachname());
            return p.toJson().toString();
        }

        // PUT /person/{id} -> Person aktualisieren
        @Put("json")
        public String aktualisiere(String daten) {
            int id = Integer.parseInt(getAttribute("id"));
            if (!personenDatenbank.containsKey(id)) {
                return new JSONObject().put("fehler", "Person " + id + " nicht gefunden").toString();
            }
            JSONObject json = new JSONObject(daten);
            JSONObject aj = json.getJSONObject("adresse");
            Adresse adresse = new Adresse(
                    aj.getString("strasse"),
                    aj.getInt("hausnummer"),
                    aj.getString("plz"),
                    aj.getString("ort"));
            Person p = new Person(id,
                    json.getString("vorname"),
                    json.getString("nachname"),
                    adresse);
            personenDatenbank.put(id, p);
            System.out.println("PUT: Person ID " + id + " aktualisiert.");
            return p.toJson().toString();
        }

        // DELETE /person/{id} -> Person löschen
        @Delete("json")
        public String entferne() {
            int id = Integer.parseInt(getAttribute("id"));
            Person p = personenDatenbank.remove(id);
            if (p == null) {
                return new JSONObject().put("fehler", "Person " + id + " nicht gefunden").toString();
            }
            System.out.println("DELETE: Person ID " + id + " gelöscht.");
            return new JSONObject().put("nachricht", "Person " + id + " wurde gelöscht").toString();
        }
    }

    // -------------------------------------------------------------------------
    // Person-Klasse mit privaten Feldern und Gettern/Settern
    // -------------------------------------------------------------------------
    public static class Person {
        private int id;
        private String vorname;
        private String nachname;
        private Adresse adresse;

        public Person(int id, String vorname, String nachname, Adresse adresse) {
            this.id = id;
            this.vorname = vorname;
            this.nachname = nachname;
            this.adresse = adresse;
        }

        public int getId() {
            return id;
        }

        public void setId(int id) {
            this.id = id;
        }

        public String getVorname() {
            return vorname;
        }

        public void setVorname(String v) {
            this.vorname = v;
        }

        public String getNachname() {
            return nachname;
        }

        public void setNachname(String n) {
            this.nachname = n;
        }

        public Adresse getAdresse() {
            return adresse;
        }

        public void setAdresse(Adresse a) {
            this.adresse = a;
        }

        public JSONObject toJson() {
            return new JSONObject()
                    .put("id", id)
                    .put("vorname", vorname)
                    .put("nachname", nachname)
                    .put("adresse", adresse.toJson());
        }
    }

    // -------------------------------------------------------------------------
    // Adresse-Klasse mit privaten Feldern und Gettern/Settern
    // -------------------------------------------------------------------------
    public static class Adresse {
        private String strasse;
        private int hausnummer;
        private String plz;
        private String ort;

        public Adresse(String strasse, int hausnummer, String plz, String ort) {
            this.strasse = strasse;
            this.hausnummer = hausnummer;
            this.plz = plz;
            this.ort = ort;
        }

        public String getStrasse() {
            return strasse;
        }

        public void setStrasse(String s) {
            this.strasse = s;
        }

        public int getHausnummer() {
            return hausnummer;
        }

        public void setHausnummer(int h) {
            this.hausnummer = h;
        }

        public String getPlz() {
            return plz;
        }

        public void setPlz(String p) {
            this.plz = p;
        }

        public String getOrt() {
            return ort;
        }

        public void setOrt(String o) {
            this.ort = o;
        }

        public JSONObject toJson() {
            return new JSONObject()
                    .put("strasse", strasse)
                    .put("hausnummer", hausnummer)
                    .put("plz", plz)
                    .put("ort", ort);
        }
    }
}
