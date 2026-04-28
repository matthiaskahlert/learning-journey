# Spickzettel: JUnit, REST und JSON (Anfaenger)

Dieser Zettel zeigt dir einfache Syntax-Muster aus deinen Beispielen.

## 1) JUnit Basics

### Was brauchst du fast immer?

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
```

### Einfachster Test

```java
@Test
void addieren_klappt() {
    int summe = 2 + 3;
    assertEquals(5, summe);
}
```

### Setup fuer mehrere Tests

```java
import org.junit.jupiter.api.BeforeEach;

private String name;

@BeforeEach
void setup() {
    name = "Max";
}

@Test
void name_ist_gesetzt() {
    assertEquals("Max", name);
}
```

## 2) REST-Methoden testen (ohne echten Serverstart)

Idee: Du rufst die Methoden des Handlers direkt auf (z. B. `handleGet()`, `handlePut(...)`).

### GET testen

```java
@Test
void handleGet_gibt_json_array_zurueck() {
    TestablePersonHandler handler = new TestablePersonHandler(null); // keine ID

    String result = handler.handleGet();

    assertTrue(result.startsWith("["));
    assertTrue(result.endsWith("]"));
}
```

### PUT testen

```java
@Test
void handlePut_aktualisiert_vorname() {
    TestablePersonHandler handler = new TestablePersonHandler("1");

    String result = handler.handlePut("{\"vorname\":\"Moritz\"}");

    assertTrue(result.contains("teilweise aktualisiert"));
}
```

### Trick fuer Path-Parameter im Test

```java
private static class TestablePersonHandler extends PersonHandler {
    private final String id;

    private TestablePersonHandler(String id) {
        this.id = id;
    }

    @Override
    public String getAttribute(String name) {
        if ("id".equals(name)) {
            return id;
        }
        return null;
    }
}
```

Damit simulierst du z. B. `/personen/1`, ohne HTTP-Server.

## 3) REST-Endpoint bereitstellen (einfach)

Beispiel mit Java HttpServer:

```java
HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
server.createContext("/mitarbeiter", new MitarbeiterHandler());
server.setExecutor(null);
server.start();
```

### Handler fuer GET

```java
static class MitarbeiterHandler implements HttpHandler {
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        if (!"GET".equals(exchange.getRequestMethod())) {
            exchange.sendResponseHeaders(405, -1);
            return;
        }

        String response = "[{\"id\":1,\"vorname\":\"Max\"}]";
        exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");
        exchange.sendResponseHeaders(200, response.getBytes().length);
        exchange.getResponseBody().write(response.getBytes());
        exchange.getResponseBody().close();
    }
}
```

## 4) JSON verarbeiten + externe GET-Anfrage

### Schritt 1: HTTP GET senden

```java
String urlString = "https://jsonplaceholder.typicode.com/posts";
URL url = URI.create(urlString).toURL();
HttpURLConnection verbindung = (HttpURLConnection) url.openConnection();
verbindung.setRequestMethod("GET");
verbindung.connect();
```

### Schritt 2: Antwort lesen

```java
StringBuilder datenString = new StringBuilder();
Scanner scanner = new Scanner(verbindung.getInputStream());
while (scanner.hasNext()) {
    datenString.append(scanner.nextLine());
}
scanner.close();
```

### Schritt 3: JSON parsen

```java
JSONArray posts = new JSONArray(datenString.toString());
JSONObject ersterPost = posts.getJSONObject(0);

int userId = ersterPost.getInt("userId");
String title = ersterPost.getString("title");
```

### Schritt 4: Einfach filtern

```java
for (int i = 0; i < posts.length(); i++) {
    JSONObject post = posts.getJSONObject(i);
    String body = post.getString("body");

    if (body.length() > 100) {
        System.out.println(post.getString("title"));
    }
}
```

## 5) Mini-Merkhilfe (Wann nutze ich was?)

- `@BeforeAll`: einmal vor allen Tests
- `@BeforeEach`: vor jedem Test neu initialisieren
- `@Test`: ein Testfall
- `assertEquals(erwartet, echt)`: exakter Vergleich
- `assertTrue(bedingung)`: Bedingung muss true sein
- `HttpURLConnection`: externe REST-API aufrufen
- `JSONArray`/`JSONObject`: JSON lesen und Felder auslesen

## 6) Typische Fehler am Anfang

- JSON-Keys falsch geschrieben (`"userId"` vs `"userid"`)
- `responseCode != 200` nicht geprueft
- bei Strings in JSON die Quotes nicht escaped
- in Tests zu viel auf einmal pruefen statt kleine, klare Assertions

Wenn du willst, mache ich dir als naechsten Schritt einen zweiten Spickzettel nur mit "copy-paste Templates" (1x GET-Test, 1x PUT-Test, 1x Endpoint, 1x API-Client) in extra kurz.
