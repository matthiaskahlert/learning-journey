# Meine Markdown notes Woche 6

## Tag 26

## Learningfacts - Kapitel 13 - Asynchrones JavaScript
### 13.1 Zeitgesteuerte Anwendungen


-  JavaScript ist **single-threaded** → führt Anweisungen **nacheinander** aus.
-  Lange laufende Aufgaben würden den Ablauf **blockieren** (z. B. `alert()`, Laden von Dateien, Serveranfragen).
-  Asynchrones JS verhindert Blockaden: zeitaufwändige Aufgaben wandern in eine **Task Queue** und werden ausgeführt, wenn der **Call Stack frei** ist.
-  Beispiele: `addEventListener()` wartet im Hintergrund und ruft später eine **Callback-Funktion** auf.
-  Haupttechniken für Asynchronität: **Callbacks**, **Promises**, **async/await**.



* **setTimeout()** und **setInterval()** gehören zu den ältesten APIs für asynchrone Abläufe.
* Timer sind keine echten Events, verhalten sich aber ähnlich: Sie „schlafen“ eine bestimmte Zeit und führen danach ihre Callback-Funktion aus.
* Die Callback-Funktion wird in eine **Warteschlange (Task Queue)** gelegt und ausgeführt, sobald die festgelegte Zeit verstrichen ist und der **Call Stack frei** ist.
* Syntax: `window.setTimeout(action, timeout)` → führt eine Funktion nach einer angegebenen Zeit (in ms) aus.

Warum setTimeout() und setInterval() APIs sind

Beide Funktionen gehören nicht zum JavaScript-Kern der Sprache (ECMAScript), sondern zur Web API des Browsers.
Browser stellen JavaScript zusätzliche Funktionen zur Verfügung, die außerhalb des eigentlichen JS-Engines laufen: z. B. DOM, fetch, Timers, Geolocation, Canvas usw.
Diese bereitgestellten Funktionen bilden eine Schnittstelle („Application Programming Interface“) zwischen JavaScript und den Fähigkeiten des Browsers.
setTimeout() und setInterval() sind Teil genau dieser Schnittstelle - also Browser-APIs.


#### setTimeout()

führt eine Funktion einmalig nach mindestens delay ms aus.
blockiert nicht sondern läuft sofort weiter.

Syntax:
```js
setTimeout(fn, delay);
```
#### setInterval()

führt eine Funktion wiederholt alle interval ms aus

Syntax:
```js
setInterval(fn, interval);
```
Timer stoppen
```js
clearTimeout(id);
clearInterval(id);

//Beispiel:
const id = setTimeout(...); 
clearTimeout(id);

const id2 = setInterval(...);
clearInterval(id2);

```

Merke: Delay/Interval = Mindestzeit, tatsächliche Ausführung erst, wenn der Call Stack frei ist.



#### requestAnimationFrame()

Was es macht:

requestAnimationFrame() ist eine moderne Methode für flüssige Animationen in JavaScript.

Sie sagt dem Browser: „Führe diese Funktion aus, bevor der nächste Bildschirm-Frame gezeichnet wird.“

Im Gegensatz zu setTimeout oder setInterval passt sich requestAnimationFrame() automatisch der Bildschirmwiederholrate an (z. B. 60 FPS).

Wenn die Seite gerade nicht sichtbar ist, pausiert der Browser die Animation automatisch → energiesparend.

Funktionsweise:

Du übergibst eine Callback-Funktion, die die Animation Schritt für Schritt aktualisiert.

Am Ende der Callback-Funktion rufst du erneut requestAnimationFrame auf, um die Animation fortzusetzen.

Syntax:
```js
// 1. callback definieren
function animate(timestamp) {
    // Animation hier aktualisieren
    // z.B. Position eines Elements ändern

    // nächsten Frame anfordern
    requestAnimationFrame(animate);
}

// 2. Animation starten
requestAnimationFrame(animate);
```
Hinweise:

timestamp ist ein optionaler Parameter, den der Browser automatisch liefert (aktueller Zeitpunkt in Millisekunden).

Ideal für Game-Loops oder jede Animation, die flüssig laufen soll.

Vorteile gegenüber setTimeout/setInterval: flüssiger, synchronisiert mit Refresh-Rate, pausiert automatisch im Hintergrund.


#### JS-Animationen – Kurzüberblick

- setTimeout() → einfache, einmalige zeitbasierte Aktion; für Wiederholung rekursiv aufrufen.
- setInterval() → wiederholt Funktion automatisch in festen Intervallen; weniger flexibel für Animationen.
- requestAnimationFrame() → für flüssige Animationen, synchron mit Bildschirm-Frames, pausiert automatisch im Hintergrund.
- Einschränkung klassischer JS-Animationen → läuft gleichmäßig wie ein Metronom; echtes „Easing“ nur mit CSS oder Web Animations API möglich.

### 13.2 AJAX – XMLHTTPRequest – Kommunikation mit dem Server
Web 2.0: Laden von Daten im Hintergrund

Ziel: Kommunikation mit dem Server, ohne die Seite komplett neu zu laden.
XMLHttpRequest / AJAX: Erste Technik für asynchronen Datenaustausch zwischen Client und Server.
Unterstützt alle textbasierten Formate (nicht nur XML).
Daten können im Hintergrund geladen werden → flüssigeres Nutzererlebnis.

Modern: Meistens wird heute das Fetch-API verwendet, XMLHttpRequest ist aber noch verfügbar.

HTTP-Grundlagen:

Client: sendet Anfrage (z. B. Benutzerdaten).
Server: liefert Antwort (HTML, Daten, Bilder usw.).
Hauptmethoden für Datenübertragung:

**GET: Daten werden in der URL übermittelt.**

**POST: Daten werden im HTTP-Body übertragen, nicht sichtbar in der URL.**
Unabhängig davon, ob GET oder POST verwendet wird, gibt der Server eine Antwort mit einem Status-Code zurück. Einige der häufigsten Statusmeldungen:

| Statuscode | Bedeutung / Beschreibung                   |
|------------|-------------------------------------------|
| 100        | Fortsetzen – Prozess läuft noch           |
| 200        | Erfolg – Anfrage erfolgreich bearbeitet  |
| 201        | Neue Ressource erstellt                   |
| 204        | Kein Inhalt zurückzusenden                |
| 300        | Redirect / Weiterleitung zu anderer URL  |
| 301        | Ressource dauerhaft verschoben            |
| 304        | Ressource schon lokal, keine neuen Daten |
| 400        | Client-Fehler, Anfrage fehlerhaft oder unzulässig  |
| 401        | Keine Autorisierung                        |
| 403        | Zugriff verboten                           |
| 404        | Nicht gefunden                             |
| 500        | Server-Fehler                              |

AJAX / XMLHttpRequest – Daten mit dem Server austauschen
Grundidee

Mit JavaScript kannst du Daten von einem Server anfordern oder an eine Serveranwendung senden, ohne die ganze Seite neu zu laden. Dafür brauchst du nur ein HTML-Element, um die Daten anzuzeigen, z. B.:

<div id="demo"></div>

Aufbau eines XMLHttpRequest

XHR-Objekt erstellen
```js
const xhr = new XMLHttpRequest();
```

Request öffnen
```js
xhr.open("POST", "app.php"); // Methode + URL der Serveranwendung
```

Event-Handler für Statusänderungen
```js
xhr.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        const myObj = JSON.parse(this.responseText); // JSON in JS-Objekt
        document.getElementById("demo").innerHTML = 
            `Studentin: ${myObj.student} <br>
             Alter: ${myObj.alter} <br>
             Note: ${myObj.note}`;
    }
}
```

Request absenden
```js
xhr.send();
```
Wichtige Punkte

readyState (Status des Requests):

Wert	Bedeutung
0	Request nicht initialisiert
1	Verbindung zum Server aufgebaut
2	Request empfangen
3	Request wird ausgeführt
4	Request abgeschlossen, Antwort bereit

status: HTTP-Antwort-Code

200 = Erfolg, Daten können verarbeitet werden

responseText enthält die Antwort vom Server als Text.

Mit JSON.parse() wandelst du JSON-Daten in ein JavaScript-Objekt um.

Praktische Hinweise

Zum Testen brauchst du einen Webserver, der PHP-Dateien ausführen kann. Ohne Server funktioniert nur das Abtippen / Syntax lernen.

Moderne Anwendungen nutzen APIs, z. B. für Wetterdaten, Karten oder Social Media.

APIs bestehen aus Befehlen, Funktionen, Protokollen und Objekten, die Daten im XML- oder JSON-Format bereitstellen.

Ein praktisches Beispiel ist die Suche nach Synonymen über die Webseite OpenThesaurus (https://openthesaurus.de). 
Das API unterstützt XML- und JSON- Abfragen. Man kann ein Suchwort eingeben und über einen Button die Anfrage an das API senden.

### 13.3 Das Fetch-API – GET – Daten abholen
fetch() – asynchron Daten holen und senden

fetch() ist der moderne Nachfolger von XMLHttpRequest (XHR).
Mit fetch() kannst du Daten vom Server abrufen oder dorthin senden – asynchron, also ohne die Seite neu zu laden.

```js
// Einfaches Beispiel: JSON-Datei laden
fetch("konzerte-10.json")
    .then((response) => {
        console.log("Content-type:", response.headers.get("Content-Type"));
        console.log("Redirected:", response.redirected);
        console.log("Status:", response.status);
        console.log("Status-text:", response.statusText);
        console.log("Response type:", response.type);
    })
    .then((response) => console.log(response));

```
fetch(url) gibt ein Promise zurück.
Ein Promise verspricht, dass die asynchrone Aktion entweder erfolgreich abgeschlossen wird oder fehlschlägt.

Methoden von Promises:

- .then() → wird ausgeführt, wenn die Aktion erfolgreich war
- .catch() → wird ausgeführt, wenn ein Fehler passiert
- .finally() → wird immer ausgeführt, egal ob Erfolg oder Fehler

```js
// Ein Promise erstellen
const meinPromise = new Promise((resolve, reject) => {
  // hier kann der asynchrone Code hin
  const allesGut = true; // Beispielbedingung
  if (allesGut) {
    resolve("Erfolg!"); // Promise erfüllt
  } else {
    reject("Fehler!"); // Promise abgelehnt
  }
});

// Mit dem Promise arbeiten, an nutzt da meistens .then und .catch methoden
meinPromise
  .then((ergebnis) => {
    console.log(ergebnis); // Wird ausgeführt, wenn resolve() aufgerufen wurde
  })
  .catch((fehler) => {
    console.error(fehler); // Wird ausgeführt, wenn reject() aufgerufen wurde
  })
  .finally(() => {
    console.log("Promise ist abgeschlossen, egal ob Erfolg oder Fehler");
  });
```

JSON-Daten abrufen

```js
fetch("konzerte-10.json")
    .then((response) => response.json()) // response in JSON umwandeln
        // Der Rückgabewert des ersten then() wird in das data-Argument des nächsten then() übergeben
    .then((data) => {
        console.log(data); // die Daten stehen hier zur Verfügung
    })
    .catch((error) => console.error("Fehler beim Laden:", error));

```
Der Rückgabewert des ersten .then() wird als Argument (data) in das nächste .then() übergeben.
fetch() kann nicht nur JSON, sondern auch Textdateien abrufen:
```js
fetch("info.txt")
    .then(response => response.text()) 
    .then(text => console.log(text));

```

GET- und POST-Requests

Ohne Optionen: fetch() macht einen einfachen GET-Request - lädt die Daten von der angegebenen URL.
Will man Daten senden (z. B. POST), kann man fetch Optionen übergeben:
```js
fetch("app.php", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: "Sara", alter: 21 })
})
.then(response => response.json())
.then(data => console.log(data));
```
Vorteile von fetch() gegenüber XHR

- Bessere Lesbarkeit des Codes → weniger Callback-Hell
- Rückgabe als Promise - einfaches Verketten von .then() und .catch()
- Einfachere Handhabung von verschiedenen Datenformaten (JSON, Text, Blob, etc.)

### REST-APIs

Viele APIs funktionieren als REST-APIs (Representational State Transfer). Sie sind weit verbreitet und erlauben es, Daten zu senden, zu empfangen und zu bearbeiten. Zum Beispiel nutzt WordPress ein REST-API, damit Entwickler über HTTP auf Funktionen und Daten zugreifen können. Die Informationen werden meistens im JSON-Format bereitgestellt.
Was ist eine REST-API?

Eine REST-API ist eine Art, wie zwei Systeme über das Internet miteinander kommunizieren.
Sie basiert auf HTTP – also denselben Regeln, mit denen auch Webseiten geladen werden.

Kurz gesagt:
REST-APIs stellen Daten bereit oder nehmen Daten entgegen – meist im JSON-Format.

🔹 Wofür verwendet man REST-APIs?

Daten lesen (z. B. Blogposts eines WordPress-Blogs abrufen)
Daten erstellen
Daten bearbeiten
Daten löschen

Viele moderne Webanwendungen (WordPress, Shopify, GitHub, OpenWeather usw.) bieten REST-APIs an.


```md
### 🔹 Wichtige HTTP-Methoden (CRUD)

| Aktion | Bedeutung      | HTTP-Methode | Beispiel               |
|--------|----------------|--------------|-------------------------|
| Create | Anlegen        | POST         | neuen Nutzer erstellen |
| Read   | Lesen          | GET          | Blogposts abrufen      |
| Update | Aktualisieren  | PUT / PATCH  | Titel ändern           |
| Delete | Löschen        | DELETE       | Beitrag löschen        |
```


REST-APIs arbeiten also meistens nach dem CRUD-Prinzip.

🔹 Wie sieht eine typische REST-URL aus?
https://example.com/wp-json/wp/v2/posts


Diese URL gibt die Posts des WordPress-Blogs zurück.
REST-APIs liefern ihre Daten fast immer als JSON.

Beispiel-Antwort (vereinfacht):
```js
[
  {
    "id": 123,
    "title": { "rendered": "Mein erster Beitrag" },
    "content": { "rendered": "Hallo Welt!" }
  }
]
```
🔹 Mit fetch() auf eine REST-API zugreifen
```js
fetch("https://wordpress.org/news/wp-json/wp/v2/posts")
  .then(response => response.json())
  .then(data => {
    console.log(data); // Array von Posts
  })
  .catch(error => console.error("Fehler:", error));
```

Warum funktioniert das gut?
Weil fetch() ein Promise zurückgibt → der Code bleibt lesbar und asynchron.

🔹 Vorteile von REST-APIs

leicht zu verwenden
nutzen standardisierte HTTP-Methoden
JSON ist einfach und überall lesbar
funktionieren in jeder Programmiersprache
flexibel und schnell

🔹 Wann treten Probleme auf?

Manchmal blockieren Server Anfragen aus dem Browser wegen CORS („Cross-Origin Resource Sharing“).
Dann erscheint im Browser z. B.:
Access to fetch at ... has been blocked by CORS policy


✔ REST = Regeln für den Datenaustausch über HTTP
✔ Daten werden meist als JSON geliefert
✔ CRUD über die Methoden GET, POST, PUT, DELETE
✔ fetch() wird genutzt, um REST-APIs anzusprechen
✔ Sehr häufig in modernen Webanwendungen (WordPress, API-Dienste usw.)


### 13.5 Fetch Async/Await – warten auf die Antwort
### Async & Await (einfach erklärt)

JavaScript führt manche Aufgaben asynchron aus (z. B. fetch oder setTimeout).  
Der Code danach läuft sofort weiter, obwohl die Aufgabe noch nicht fertig ist.

async/await löst dieses Problem:

- `async` macht eine Funktion asynchron (sie gibt ein Promise zurück)
- `await` wartet darauf, dass ein Promise fertig wird, bevor der Code weiterläuft

Damit kann man asynchronen Code schreiben, der aussieht wie normaler, linearer Code.

Beispiel:

```js
async function load() {
  const response = await fetch("daten.json");
  const data = await response.json();
  console.log(data);
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function count() {
  for (let i = 1; i <= 5; i++) {
    console.log(i);
    await delay(1000); // echte Pause
  }
}

count();
```

