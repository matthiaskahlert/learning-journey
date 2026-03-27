import java.nio.file.*;

public class DBConfig {

    public static String getDBUrl(String dbName) {
        try {
            Path path = Paths.get(
                    DBConfig.class
                            .getProtectionDomain()
                            .getCodeSource()
                            .getLocation()
                            .toURI()
            ).toAbsolutePath().normalize();

            // Falls CodeSource eine Datei ist (z. B. JAR), auf Ordner wechseln
            if (Files.isRegularFile(path)) {
                path = path.getParent();
            }

            // Nach oben bis Projekt-Root (pom.xml)
            while (path != null && !Files.exists(path.resolve("pom.xml"))) {
                path = path.getParent();
            }

            if (path == null) {
                throw new RuntimeException("Projekt-Root nicht gefunden");
            }

            // Wenn Root einen Unterordner "java" hat -> java/Datenbanken, sonst Datenbanken
            Path dbBase = Files.isDirectory(path.resolve("java"))
                    ? path.resolve("java").resolve("Datenbanken")
                    : path.resolve("Datenbanken");

            Files.createDirectories(dbBase);

            Path dbPath = dbBase.resolve(dbName).toAbsolutePath().normalize();
            return "jdbc:derby:" + dbPath + ";create=true";

        } catch (Exception e) {
            throw new RuntimeException("Fehler beim Ermitteln des DB-Pfads", e);
        }
    }
}