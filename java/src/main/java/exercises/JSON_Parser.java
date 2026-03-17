import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;

public class JSON_Parser {
    public static void main(String[] args) {
        try {
            String text = new String(Files.readAllBytes(Paths.get("personen.json")), StandardCharsets.UTF_8);

            Object parsed = new JSONTokener(text).nextValue();

            if (parsed instanceof JSONArray) {
                JSONArray array = (JSONArray) parsed;
                System.out.println("JSON erfolgreich geladen. Anzahl Elemente: " + array.length());
            } else if (parsed instanceof JSONObject) {
                JSONObject object = (JSONObject) parsed;
                System.out.println("JSON erfolgreich geladen. Anzahl Felder: " + object.length());
            } else {
                System.out.println("JSON erfolgreich geladen, aber unbekanntes Format.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (RuntimeException e) {
            System.out.println("Fehler beim Verarbeiten der JSON-Daten: " + e.getMessage());
        }
    }

}
