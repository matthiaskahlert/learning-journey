/* 
Entwickle ein kleines Java-Programm, das Daten von einer REST-Schnittstelle abruft, verarbeitet und basierend auf bestimmten Kriterien Entscheidungen trifft. Das Programm soll folgende Schritte durchführen:

a) Stelle eine GET-Anfrage an die REST-Schnittstelle https://jsonplaceholder.typicode.com/posts, um eine Liste von Posts zu erhalten. Jeder Post ist ein JSON-Objekt, das mindestens die Felder userId, id, title und body enthält.

b) Analysiere die erhaltenen Daten und filtere alle Posts heraus, deren body länger als 100 Zeichen ist.

c) Verwende eine Schleife, um über die gefilterten Posts zu iterieren. Innerhalb der Schleife, prüfe für jeden Post, ob die userId gerade oder ungerade ist.

d) Für Posts mit einer geraden userId, füge den Titel des Posts einer Liste geradePosts hinzu. Für Posts mit einer ungeraden userId, füge den Titel des Posts einer Liste ungeradePosts hinzu.

e) Nachdem alle Posts verarbeitet wurden, gib die Anzahl der Titel in geradePosts und ungeradePosts aus und zeige die Titel jeweils in der Konsole an.
*/

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;
import org.json.JSONArray;
import org.json.JSONObject;

public class Uebung_14_3_A_01 {
    public static void main(String[] args) throws IOException {
        // a) GET-Anfrage an REST-Schnittstelle
        String urlString = "https://jsonplaceholder.typicode.com/posts";
        URL url = URI.create(urlString).toURL();
        HttpURLConnection verbindung = (HttpURLConnection) url.openConnection();
        verbindung.setRequestMethod("GET");
        verbindung.connect();

        int antwortCode = verbindung.getResponseCode();
        if (antwortCode != 200) {
            throw new RuntimeException("HttpResponseCode: " + antwortCode);
        } else {
            StringBuilder datenString = new StringBuilder();
            Scanner scanner = new Scanner(verbindung.getInputStream());
            while (scanner.hasNext()) {
                datenString.append(scanner.nextLine());
            }
            scanner.close();

            // b) JSON-Daten analysieren und filtern
            JSONArray posts = new JSONArray(datenString.toString());
            ArrayList<String> geradePosts = new ArrayList<>();
            ArrayList<String> ungeradePosts = new ArrayList<>();

            // c) Schleife über gefilterte Posts
            for (int i = 0; i < posts.length(); i++) {
                JSONObject post = posts.getJSONObject(i);
                String body = post.getString("body");
                if (body.length() > 100) { // nur Posts mit langem Body
                    int userId = post.getInt("userId");
                    String title = post.getString("title");
                    // d) Nach gerader/ungerader userId sortieren
                    if (userId % 2 == 0) {
                        geradePosts.add(title);
                    } else {
                        ungeradePosts.add(title);
                    }
                }
            }

            // e) Ergebnisse ausgeben
            System.out.println("Anzahl der Titel in geradePosts: " + geradePosts.size());
            System.out.println("Anzahl der Titel in ungeradePosts: " + ungeradePosts.size());
            System.out.println("Titel der geradePosts:");
            geradePosts.forEach(System.out::println);
            System.out.println("Titel der ungeradePosts:");
            ungeradePosts.forEach(System.out::println);
        }
    }
}
