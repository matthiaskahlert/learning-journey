import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.Files;

import org.json.JSONArray;
import org.json.JSONObject;

public class JsonReader {
    public static void main(String[] args) {
        try {
            Path jsonPath = Path.of("src", "main", "java", "exercises", "data.json");
            String jsonText = Files.readString(jsonPath, StandardCharsets.UTF_8);

            JSONObject person = new JSONObject(jsonText);
            String name = person.getString("name");
            int age = person.getInt("age");
            JSONArray skills = person.getJSONArray("skills");

            System.out.println("JSON erfolgreich gelesen.");
            System.out.println("Name: " + name);
            System.out.println("Alter: " + age);
            System.out.println("Skills: " + skills.toList());
        } catch (IOException e) {
            e.printStackTrace();
        } catch (RuntimeException e) {
            System.out.println("JSON konnte nicht verarbeitet werden: " + e.getMessage());
        }
    }
}
