import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;

public class JSON_Parser {
    public static void main(String[] args) {
        try {
            String text = new String(Files.readAllBytes(Paths.get("personen.json")), StandardCharsets.UTF_8);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
