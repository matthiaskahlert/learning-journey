# Meine Markdown notes Woche 5

## Tag 21

## Learningfacts - Kapitel 11 - Ereignisse / Events
### Event Handling
Ereigniserkennung ist in JavaScript schon eingebaut, die Reaktion auf ein Event wird in event-Handlern programmiert.
Einige Arten von Events sind:

- keyboard - Tastatur
- loading/unloading - Laden / Schließen des Dokuments
- media - Video / Audio
- messaging - Ereignisse des Browserfensters
- mouse - Ereignisse der Maus
- text selection - Ereignisse von Eingabefeldern
- touch - Touch-Events auf Touchscreen
 
 #### Eventerkennung Version 1
 
 Eventerkennung war in ihrer ursprünglichen Form mit onclick, onchange und onblur vorhanden. 
 ```js
<img onclick="alert('Vase Cracked Porzellan')"
    loading="lazy" src="vase.jpg"
    width="331" height="331" alt="Vase cracked Porzellan">
```
onclick öffnet mit alert() ein Dialogfenster, das den Ablauf blockiert, bis der Benutzer es schließt.

Im folgenden Beispiel setzt man die onclick-Eigenschaft des Elements img auf einen String.
Browser behandeln das dann wie ein Inline-Event-Handler und konvertieren den String intern zu einer Funktion. also Der Browser erstellt intern eine Funktion wie
```js
function onclick(event) {
   this.src='vase.jpg';
   this.style='transform: scale(2,2)';
}
```

```js
img.onclick =
    "this.src='vase.jpg'; this.style='transform: scale(2,2)'"; // dies überschreibt ALLE Inline-Styles des Elements.
```
Die Anweisungen tauschen das src-Attribut des img-Tags gegen ein anderes Bild und zoomen es um den Faktor 2. Strings als Event-Handler sind allerdings veraltet, unsicher und gelten als schlechter Stil,
Moderner würde man es so umsetzen:
```js
img.addEventListener("click", () => {
    img.src = "vase.jpg";
    img.style.transform = "scale(2,2)";
});
```
Das Schlüsselwort this:
- In einer normalen Funktion (ohne strict mode) ist this das globale Objekt (window).
- In einer Funktion mit strict mode ist this undefined.
- Arrow-Funktionen besitzen kein eigenes this, sie erben dieses vom äußeren Kontext.
- In einem Event verweist this auf das Element, auf dem das Event stattfindet.

this ist keine Variable, sondern ein Schlüsselwort und kann nicht geändert werden.

#### Eventerkennung Version 2 - EventListener

CSS kennt die Pseudoklasse :hover.
JavaScript kennt Hover nicht als Konzept, aber es kennt die Mausereignisse, die dasselbe abbilden. Man setzt dies mit dem EventListener um, einem Beobachter. JavaScript unterscheidet die Position der Maus in hinsicht auf das Element in:
- onmouseenter - Grenze zum Element überschreiten
- onmouseover - über dem Element liegen
- onmousemove - über dem Element bewegen
- onmouseout - Element verlassen

Für Touchscreens:
- ontouchstart – mit dem Finger auf das Element tippen
- ontouchend – Finger angehoben
- ontouchmove – Finger über das Element bewegen
- ontouchcancel – Event abgebrochen (z. B. Systeminteraktion)

In JavaScript müssen Eventnamen, vor allem bei addEventListener oder element.on…, stets lowercase sein

Der richtige Ersatz für CSS-Hover im JS ist mouseenter & mouseleave (nicht mouseover/mouseout).


Man nutzt auch **addEventListener()** um Ereignisse und dazugehörige Aktionen zu registrieren.
mit elem.addEventListener wird ein Event für ein Element angemeldet und definiert, was beim eintreten des Events passieren soll.
Die Event Listener-Methode hat zwei Parameter: die Art des Events und eine Callback-Funktion
```js
const button = document.querySelector("#btn");
button.addEventListener("click", showlarge);

button.addEventListener("click", function() { ... });
// oder als Arrow-Funktion
button.addEventListener("click", () => {});
```



Mit dem eventListener behandelt man Events für window, document und individuelle Elemente der Webseite und ruft eine Funktion als EventHandler auf, sobald das Event feuert.



Callback-Funktionen sind Funktionen, die als Argumente an andere Funktionen übergeben werden und dort später ausgeführt werden, etwa bei forEach() oder in Ereignisbehandlungen. Sie ‚merken‘ sich dabei den ursprünglichen Kontext zum Zeitpunkt ihres Aufrufs und können ihn bei der Ausführung wiederherstellen.
```js
arr.forEach (function() { ... })
addEventListener("click", function() { ... })



const color = document.querySelector(".color");
const change = document.querySelector("#change");

function changeColor(evt) {
evt.target.classList.toggle("dark");
color.classList.toggle("black");
}
klick.addEventListener("click", changeColor);

```

##### addEventListener() für eine Gruppe von Elementen


addEventListener soll oft auf eine Gruppe von elementen reagieren, zb alle eingabefelder prüfen nachdem ein nutzer alles ausgefüllt hat.

```html
<div class="columns">
    <label><input class="feld" placeholder="Ort"></label>
    <label><input class="feld" placeholder="Straße"></label>
    <label><input class="feld" placeholder="Land"></label>
</div>
```

```js
  // EventHandler reagiert auf Grupe von Elementen
  const input = document.querySelectorAll(".feld");
  input.forEach((elem) =>  {
    elem.addEventListener("blur",()=>{
        elem.closest("label").append(elem.value); 
    })
  })
  ```
blur bedeutet: Das Input-Feld verliert den Fokus (z. B. man klickt heraus oder tabbt weiter).
elem.closest("label") sucht das nächstgelegene <label> um das Input herum..append(elem.value) hängt den eingegebenen Text als reinen Textknoten hinter das Label.
Ein Event Handler kann mit elem.onclick = null; entfernt werden.


##### removeEventListener() Die Beobachtung eines Elements beenden
mit removeEventListener() kann man den eventhandler von einem event entkoppeln / lösen. dies geht jedoch nicht mit anonymen funktionen. 
Warum kann man anonyme Funktionen nicht entfernen?
Weil removeEventListener denselben Funktions-Verweis braucht, der beim addEventListener verwendet wurde.
```js
elem.addEventListener("blur", () => {});
elem.removeEventListener("blur", () => {}); // funktioniert NICHT
```

### 11.2 Eigenschaften und Methoden der Maus-Events


Maus-Events umfassen nicht nur Klicks, sondern auch:

- Einfache Klicks
- Doppelklicks
- Beteiligte Maustasten
- Position der Maus über einem Element
- Scrollrad der Maus

Unterschiedliche Klickarten können unterschiedliche Aktionen auslösen, z. B. Farbwechsel eines Buttons.



Jedes Maus-Event liefert Informationen über:

Auslösendes Element (event.target)
Typ des Events (event.type)
Zeitpunkt des Eintreffens (event.timestamp)


| Beschreibung                                        | Property        |
| --------------------------------------------------- | --------------- |
| Das Element, das das Ereignis gemeldet hat          | `target`        |
| Das Element, an das der Event Listener gebunden ist | `currentTarget` |
| Das auslösende Event                                | `type`          |
| Zeitpunkt des Events                                | `timestamp`     |
| Die x-Position der Maus relativ zum Browserfenster  | `clientX`       |
| Die y-Position der Maus relativ zum Browserfenster  | `clientY`       |
| Die x-Position der Maus relativ zum Element         | `offsetX`       |
| Die y-Position der Maus relativ zum Element         | `offsetY`       |
| Die x-Position der Maus relativ zur Seite           | `pageX`         |
| Die y-Position der Maus relativ zur Seite           | `pageY`         |
| Die x-Position der Maus relativ zum Bildschirm      | `screenX`       |
| Die y-Position der Maus relativ zum Bildschirm      | `screenY`       |


| Property        | Merkhilfe / Eselsbrücke                                                |
| --------------- | ---------------------------------------------------------------------- |
| `target`        | „Wer hat geklickt?“ → das Element, das den Event ausgelöst hat         |
| `currentTarget` | „Wo hängt der Listener dran?“ → das Element, an dem der Listener sitzt |
| `type`          | „Was ist passiert?“ → z. B. click, mouseover, blur                     |
| `timestamp`     | „Wann?“ → Zeitpunkt des Events                                         |
| `clientX/Y`     | „Fenster-Koordinaten“ → wie weit rechts/unten im Browserfenster        |
| `offsetX/Y`     | „Element-Koordinaten“ → relative Position zur Ecke des Elements        |
| `pageX/Y`       | „Seiten-Koordinaten“ → scrollbare Seite, unabhängig vom Fenster        |
| `screenX/Y`     | „Bildschirm-Koordinaten“ → absolute Position auf dem Monitor           |
folgend ein eventlistener, der die clickposition auf einem bild element registriert, es geht um eine klassische 5 sterne bewertung:


```html
<img id="stars" src="images/stars-0.svg" alt="Bewertung" style="width:200px; cursor:pointer;">

```

```js


const stars = document.querySelector("#stars");

stars.addEventListener("click", function(evt) {

  const width = this.width;
  const position = evt.offsetX;

  switch(true) {
    case (position > width/5 * 4):
      this.src = "images/stars-5.svg";
      break;
    case (position > width/5 * 3):
      this.src = "images/stars-4.svg";
      break;
    case (position > width/5 * 2):
      this.src = "images/stars-3.svg";
      break;
    case (position > width/5):
      this.src = "images/stars-2.svg";
      break;
    default:
      this.src = "images/stars-1.svg";
  }

}); // ← Schließt die Funktion und den Eventlistener
```

Das Bild wird in 5 gleiche Abschnitte unterteilt (width/5).
Je nachdem, in welchem Abschnitt der Klick landet, wird ein anderes Bild geladen:

Rechts außen → 5 Sterne
weiter links → 4 Sterne
mittig → 3 Sterne
etc.


#### event.target und after()

event.target

Das HTML-Element, auf dem ein Event passiert ist.
Ermöglicht es, gezielt CSS zu ändern oder Informationen vom Element zu nutzen.

Beispiel: Klick auf ein Bild → event.target ist genau dieses Bild.

after()

Hängt Text oder ein neues Element direkt hinter ein bestehendes Element an.
Wird oft verwendet, um zusätzliche Informationen anzuzeigen, z. B. den Namen einer gewählten Frucht.

Praktischer Tipp:
Nach dem Einfügen kann der Event-Listener mit removeEventListener() entfernt werden, damit ein erneuter Klick nicht erneut etwas anhängt.

```js
const frucht = document.querySelectorAll(".frucht img");

frucht.forEach(item => {
  item.addEventListener("click", function myCaption(evt) {
    const caption = evt.target.getAttribute("alt");
    const figcaption = document.createElement("figcaption");
    figcaption.innerHTML = caption;

    evt.target.after(figcaption);
    evt.target.removeEventListener("click", myCaption);
  });
});

```

1️⃣ Auswahl der Elemente
const frucht = document.querySelectorAll(".frucht img");

Es werden alle <img>-Elemente ausgewählt, die sich innerhalb eines Elements mit der Klasse .frucht befinden.
Ergebnis: Eine NodeList mit allen Fruchtbildern.

2️⃣ Event-Listener für jeden Klick hinzufügen
frucht.forEach(item => {
  item.addEventListener("click", function myCaption(evt) {
    ...
  });
});


Für jedes Bild wird ein Click-Event hinzugefügt.
Die Funktion myCaption wird ausgeführt, wenn man auf ein Bild klickt.

3️⃣ Alt-Text auslesen
const caption = evt.target.getAttribute("alt");
evt.target ist das angeklickte Bild.
getAttribute("alt") holt den Alt-Text, z. B. den Namen der Frucht.

4️⃣ Neues Element erstellen
const figcaption = document.createElement("figcaption");
figcaption.innerHTML = caption;
Ein neues <figcaption>-Element wird erzeugt.
Darin wird der Alt-Text als Inhalt gesetzt.

5️⃣ Figcaption hinter das Bild setzen
evt.target.after(figcaption);

Das <figcaption> wird direkt hinter das angeklickte Bild eingefügt.
Beispiel: Klick auf ein Apfelbild → unter dem Bild erscheint „Apfel“.

6️⃣ Event-Listener entfernen
evt.target.removeEventListener("click", myCaption);

Damit wird verhindert, dass ein zweiter Klick den Text nochmal anhängt.
Jeder Klick wirkt also nur einmal pro Bild.

✅ Zusammengefasst
Alle Fruchtbilder werden ausgewählt.
Klick auf ein Bild → der Alt-Text wird ausgelesen.
Ein <figcaption> mit dem Alt-Text wird unter das Bild gesetzt.
Danach wird der Klicklistener entfernt, damit es nicht doppelt angezeigt wird.


Maus-Events

onmousemove → wird bei jeder Bewegung der Maus ausgelöst.
onmouseover → wird ausgelöst, sobald die Maus die Grenze eines Elements betritt.
onmouseout → wird ausgelöst, sobald die Maus ein Element verlässt.
onmouseup → wird ausgelöst, wenn eine Maustaste losgelassen wird.
Anwendungsbereiche: Grundlage für Zeichenprogramme, Spiele und interaktive Webseiten.

### 11.4 keyboard events

keydown, keypress und keyup werden beim Drücken und Loslassen einer Taste ausgelöst.
keydown und keypress feuern solange die Taste gedrückt wird.
keyup feuert einmal beim Loslassen der Taste.
keydown reagiert auch auf Steuertasten wie Shift, Esc, Pfeiltasten oder Akzent-Tasten.

```html
<input id="textfld" type="text" placeholder="Geben sie einen Text ein">
```

```js
textfld.addEventListener("keydown", evt => {
    console.log("keydown");
});
```
#### Eigenschaften von Tastatur-Events:

Tastatur-Events (keypress, keydown, keyup) liefern Informationen über die gedrückte Taste.
Sie können z. B. in Formularen oder Spielen bestimmte Aktionen auslösen (Enter, Pfeiltasten).
Alle Event-Informationen sind in der Konsole sichtbar.
Wichtige Standard-Eigenschaften: event.target, event.currentTarget, event.type.

Beispielsweise bewegen die tasten w,a,s,d einenn cursor oder einen character in Spielen.

| Eigenschaft           | Beschreibung                                                                                  |
| --------------------- | --------------------------------------------------------------------------------------------- |
| `key`                 | Gibt einen Namen für die gedrückte Taste zurück, z. B. `"Digit7"`, `"Numpad7"` oder `"KeyP"`. |
| `code`                | Gibt einen Unicode-Wert als Symbol für die gedrückte Taste zurück.                            |
| `keyCode` (veraltet)  | Gibt einen numerischen Wert der Taste zurück. Wichtig für Steuer-Tasten wie Enter.            |
| `charCode` (veraltet) | Gibt den Wert der Taste zurück. Wird von alten Browsern ggf. nicht unterstützt.               |
| `repeat`              | Gibt `true` zurück, wenn eine Taste dauerhaft gehalten wird.                                  |
| `shiftKey`            | Gibt `true` zurück, wenn die Shift-Taste zusätzlich gedrückt wird.                            |
| `ctrlKey`             | Gibt `true` zurück, wenn die Ctrl-Taste zusätzlich gedrückt wird.                             |
| `altKey`              | Gibt `true` zurück, wenn die Alt-Taste (Option auf macOS) zusätzlich gedrückt wird.           |

### 11.6 event.preventDefault() - Vorbestimmte Verhalten verhindern
preventDefault()

Viele HTML-Elemente führen von Haus aus Aktionen aus (z. B. Links springen, Buttons senden Formulare).
Mit event.preventDefault() kannst du diese Standardaktionen verhindern.
Dadurch kann dein Skript z. B. Formulardaten prüfen, bevor sie abgeschickt werden, oder eigene Aktionen nach einem Link-Klick durchführen.
Die Methode wird mit leeren runden Klammern aufgerufen: event.preventDefault().


#### Eingabeformulare prüfen
Beim Absenden eines Formulars löst der Browser ein submit-Event aus.

Mit evt.preventDefault() kann man dieses Standardverhalten verhindern, damit das Formular nicht sofort an den Server gesendet wird.
Unterhalb von preventDefault() kann mein Skript jetzt fortfahren und die Aktionen durchführen, die geplant sind z.b. bevor das submit event stattfindet.


Dadurch kann das Skript zuerst validieren, ob alle Eingaben korrekt sind.
Typischer Ablauf bei der Validierung
form.addEventListener("submit", handler) fängt den Submit ab.
evt.preventDefault() stoppt das automatische Absenden.
Das Skript liest die Werte der Eingabefelder über .value.
Reguläre Ausdrücke (Regex) testen, ob Name, E-Mail, Telefonnummer und Text korrekt sind.
Fehlermeldungen werden in ein Element wie .emsg geschrieben.
Wenn alle Tests bestanden sind, wird das Formular manuell mit form.submit() abgeschickt.
Validierungsregeln (vereinfacht)
Name: mindestens 3 Zeichen, Buchstaben + Sonderzeichen (inkl. Umlaute).
Telefonnummer: mindestens 7 Zeichen, Ziffern + Klammern/Bindestriche erlaubt.
E-Mail: Buchstaben/Ziffern vor @, danach Domain + 2–6 Zeichen Endung.
Nachricht: mindestens 30 Zeichen.

### 11.8 Event Delegation - ein Event Handler für viele Elemente

Wenn viele gleiche events behandelt werden müssen setzt man eine Event Delegation auf ein gemeinsames ElternElement.

```html
<div class="gallery">
<div class="ding">
  <img src="musik.jpg" width="920" height="612">
  <div class="del">X</div>
</div>
...
</div>
```
```js
const gallery = document.querySelector(".gallery");

gallery.addEventListener("click", (evt) => {
if (evt.target.className === "del") {
evt.target.parentElement.remove()
}
});
```
Bei einem Klick auf das gallery-Element prüft evt.target.className, ob ein Element mit dieser CSS-Klasse vorliegt. 
Wenn das der Fall ist, greift evt.target.parentElement auf das umfassende Element zu, 
also auf das div-Element mit der CSS-Klasse ding. 
remove() löscht das  Element.

### 11.9 Ereignisse des Window-Objekts

Das Window-Objekt repräsentiert das Browserfenster und löst Ereignisse wie Laden der Seite, Ändern der Fenstergröße, Schließen und Scrollen aus. 
Viele dieser Events müssen heute jedoch kaum noch direkt beobachtet werden:

defer und async bei Skripten machen zusätzliche Lade-Event-Handler oft überflüssig.
CSS Media Queries übernehmen Layout-Anpassungen bei Größenänderungen des Fensters.
Lazily geladene Inhalte lassen sich inzwischen ohne Scroll-Events realisieren – HTML bietet loading="lazy" und JavaScript den IntersectionObserver, der ältere, aufwendige Scroll-Abfragen ersetzt.
Window-Events werden wie Document-Events mit addEventListener behandelt, nur dass man dafür das globale window-Objekt anspricht.

| Event            | Beschreibung                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------|
| load             | löst aus, wenn das Dokument mit allen Ressourcen (Bilder, CSS-Dateien, Skripte usw.) vollständig geladen wurde. |
| domContentLoaded | löst aus, wenn das Dokument geladen wurde, aber die externen Ressourcen noch nicht verfügbar sind.        |
| unload           | löst aus, wenn der Benutzer die Seite verlässt oder das Dokument geschlossen wird.                        |
| beforeunload     | löst aus, bevor der Benutzer die Seite verlässt; kann genutzt werden, um den Benutzer vor ungeseherten Änderungen zu warnen. |
| resize           | löst aus, wenn das Browserfenster vergrößert oder verkleinert wird.                                      |
| scroll           | löst aus, wenn der Benutzer das Dokument scrollt.                                                         |

```js
window.addEventListener("resize", function() {
// Behandlung des resize-Events

});
```


## Learningfacts - Kapitel 12 - Formulare prüfen und versenden
Ein klassisches Webformular besteht aus zwei Teilen:

1. HTML-Formular
Enthält form-, input-, select- usw. Elemente.
Jedes Eingabefeld nutzt ein name-Attribut, damit der Server die Daten als Name-Value-Paare empfangen kann.
→ name = Identifier für das Feld
→ value = Nutzer-Eingabe oder optionaler Vorgabewert

2. PHP-Programm auf dem Server
Empfängt die Daten aus dem Formular und verarbeitet sie. Das HTML-Formular wird so gestaltet, dass es genau die Daten liefert, die das PHP-Skript erwartet.

JavaScript ist optional. Bei einfachen Formularen wie Kontakt- oder Kommentarformularen braucht man es nicht.
Wenn JavaScript eingesetzt wird, übernimmt es die Rolle eines Vermittlers, z. B.:

- verhindert das automatische Absenden des Formulars,
- prüft Eingaben direkt im Browser,
- gibt sofort Rückmeldungen, ohne die Seite neu zu laden.

Als JavaScript-Programmierer muss man kein PHP können – man musst nur wissen, welche Namen und Werte das PHP-Skript erwartet.

Beispiel: JS-Validierung

Problem: Username zu kurz → muss mindestens 3 Zeichen haben.
```js
<form id="loginForm">
  <input type="text" name="username" id="username">
  <button type="submit">Senden</button>
</form>

<script>
document.getElementById("loginForm").addEventListener("submit", function(e) {
  const user = document.getElementById("username").value;

  if (user.length < 3) {
    e.preventDefault(); // Absenden verhindern
    alert("Username muss mindestens 3 Zeichen lang sein.");
  }
});
</script>

```
### Werte von Eingabefeldern lesen & schreiben – Überblick

JavaScript prüft Eingaben vor dem Absenden, um unnötige Serveranfragen zu vermeiden.
Der Server kann umgekehrt auch Werte zurückgeben, die JavaScript in Formularfelder einträgt.

Beim Klick auf „Senden“ (submit) erstellt der Browser automatisch einen HTTP-Request aus allen name=value-Paaren des Formulars (Query-String). Das Zusammenbauen übernimmt der Browser – die Serveranwendung erhält die Daten bereits korrekt formatiert.

Zugriff auf Formularfelder

JavaScript greift auf Werte in Formularen genauso zu wie auf andere DOM-Elemente:

- Über id
document.getElementById("feld")
oder
document.querySelector("#feld")

- Über name
document.getElementsByName("username")[0]

Das funktioniert, weil Formulare immer name-Attribute nutzen, um Werte für den Server eindeutig zu identifizieren.

Absenden verhindern (Wichtig für Validierung)

Beim Klick auf den Button löst der Browser ein submit-Event aus.
Für eigene Prüfungen muss JavaScript dieses Ereignis abfangen und das Absenden stoppen:
```js
form.addEventListener("submit", e => {
  e.preventDefault(); // verhindert HTTP-Request
});

```
Eingaben erkennen (Events)

Es gibt mehrere Events, um Eingaben zu überwachen:

- blur – Feld verliert den Fokus (z. B. Klick neben das Feld)
- change – Inhalt eines Felds ändert sich (nützlich für select)
- input – reagiert auf jede Tastatureingabe (ähnlich: keydown)

Praktischer Tipp

Zum Testen ein kleines Ausgabefeld einbauen, das dir live zeigt, was eingegeben wurde (anstatt immer in die Konsole zu schauen).
Vor Veröffentlichung wieder entfernen.

Beispiel: Wert lesen, prüfen und wieder ins Feld schreiben

Aufgabe: Nutzer soll eine Postleitzahl eingeben. Zulässig sind nur 5 Ziffern.
```html
<div class="test" id="output"></div>

<form id="plzForm">
  <input type="text" id="plz" name="plz">
  <button type="submit">Senden</button>
</form>

<script>
const plzInput = document.getElementById("plz");
const output   = document.getElementById("output");
const form     = document.getElementById("plzForm");

// Eingaben live anzeigen
plzInput.addEventListener("input", () => {
  output.textContent = "Eingabe: " + plzInput.value;
});

// Form-Validierung
form.addEventListener("submit", (e) => {
  const val = plzInput.value;

  if (!/^\d{5}$/.test(val)) {
    e.preventDefault();
    alert("PLZ muss genau 5 Ziffern enthalten.");
    return;
  }

  // Beispiel: Wert aus Serverantwort wieder ins Feld schreiben
  // plzInput.value = serverAntwort.plz;
});
</script>
```

### Checkboxen & Radiobuttons – Übersicht
✔️ Checkboxen (<input type="checkbox">)

Haben ein implizites value-Attribut
→ Wenn kein eigener Wert vergeben wird, liefert .value immer "on"

Haben zusätzlich eine checked-Eigenschaft
→ checked = true (aktiviert)
→ checked = false (nicht aktiviert)

Zum Auslesen nutzt man meistens:
```js
checkbox.checked     // true/false
checkbox.value       // "on" oder eigener Wert

```
Radiobuttons (<input type="radio">)

Mehrere Radiobuttons teilen sich einen gemeinsamen Namen (name="...")
Immer nur ein Radiobutton der Gruppe kann aktiv sein
Auslesen erfolgt am einfachsten über das click-Event:

```js
radio.addEventListener("click", () => console.log(radio.value));

```
Um den aktiven Radiobutton zu finden:
```js
document.querySelector('input[name="choice"]:checked').value;

```
focus-Event

Wird ausgelöst, wenn ein Eingabefeld den Fokus erhält (z. B. durch Anklicken)
Wird häufig genutzt, um das aktive Feld optisch hervorzuheben (z. B. Rahmenfarbe)

Beispiel:
```js
input.addEventListener("focus", () => {
  input.style.border = "2px solid blue";
});

```
blur-Event

Gegenstück zu focus
Wird ausgelöst, wenn ein Element den Fokus verliert
Praktisch für Validierungen oder um Eingaben zu speichern

```js
input.addEventListener("blur", () => {
  console.log("Feld verlassen:", input.value);
});

```

Bonus: CSS clamp() für Schriftgrößen

clamp(min, preferred, max) begrenzt einen Wert auf einen definierten Bereich
Wird häufig für responsive Schriftgrößen verwendet

Beispiel:
```js
font-size: clamp(1rem, 2vw, 2rem);
```

Damit wird die Schriftgröße:

nie kleiner als 1rem
nie größer als 2rem

dazwischen flexibel abhängig vom Viewport

## 12.2 Formulardaten versenden

Formulardaten versenden – Zusammenfassung
1. Absenden des Formulars verhindern

Bevor Formulardaten gesendet werden, prüft das Skript die Eingaben.
Dazu wird das automatische Absenden durch evt.preventDefault() gestoppt.
```js
const form = document.querySelector("#form-element");

function formSubmit(evt) {
  evt.preventDefault(); // verhindert das Abschicken
}

form.addEventListener("submit", formSubmit);
```

2. Werte aus Feldern auslesen (klassische Methode)

Formulare senden Name–Wert-Paare, wobei:

der Name aus name="..." kommt

der Wert aus .value oder .checked

✔️ value für Text, Select, Textarea

Beispiele:

inputUsername.value
ortSelection.value
text.value

✔️ checked für Checkboxen
checkbox.checked   // true / false

✔️ Radiobuttons (name-Gruppe)

Radiobuttons mit gleichem name werden gesammelt:
```js
for (const item of radio) {
  if (item.checked) {
    console.log("choice", item.value);
    break;
  }
}
```

3. FormData – moderne Methode zum Sammeln und Senden von Formulardaten

FormData erleichtert das Auslesen und Übermitteln von Formulardaten:

sammelt automatisch alle Felder

berücksichtigt Name-Value-Paare

encodiert Werte korrekt (z. B. Umlaute, Leerzeichen)

spart eigenes Durchlaufen der Felder

Beispiel:
```js
function formSubmit(evt) {
  evt.preventDefault();

  const data = new FormData(formdemo);

  for (const [name, value] of data) {
    console.log(name, value);
  }
}
```

Vorteile:

Kein Durchhangeln durch einzelne Inputs

Unterstützt mehrfach vorkommende Namen (z. B. Checkbox-Gruppen stadt[])

Bereit für fetch() oder AJAX-Requests

4. HTML-Beispiel für FormData
<form action="formdata.php" method="post" id="formdemo">
  <select name="artikel">
    <option value="regenjacke">Regenjacke</option>
    <option value="wanderstiefel">Wanderstiefel</option>
    <option value="rucksack">Rucksack</option>
  </select>

  <input type="checkbox" name="stadt[]" value="München"> München
  <input type="checkbox" name="stadt[]" value="Rüdesheim" checked> Rüdesheim
  <input type="checkbox" name="stadt[]" value="Straßburg" checked> Straßburg

  <textarea name="txt" id="txt">
    Text mit Umlauten wie Ä, ß; und Semikolon
  </textarea>

  <input type="checkbox" name="mitm" id="mitm" checked> Mitmachen!

  <button type="submit">Senden</button>
</form>


Besonderheit:
stadt[] erzeugt ein Array mehrerer Werte, ideal für Mehrfachauswahl mit Checkboxen.

Kurzfazit

* preventDefault() verhindert das automatische Absenden, damit JavaScript vorher prüfen kann
.value → Inhalt von Text/Select/Textarea
.checked → Zustand von Checkbox und Radio

* Radiobuttons → Gruppe über getElementsByName() durchlaufen
* FormData → moderne, flexible, automatische Sammlung aller Formulardaten


### FormData & typische Hürden bei Formularen – Zusammenfassung
1. Typische Probleme bei Formularen

Codierung:
Sonderzeichen (Ä, ß, &, ;) müssen korrekt codiert werden, damit sie sauber übertragen werden.

Checkboxen:

Einzelne Checkbox → überträgt "on" (falls kein eigenes value gesetzt ist)
Mehrere Checkboxen mit gleichem Namen (stadt[]) → erzeugen ein Array von Name–Value-Paaren

2. Warum FormData diese Probleme löst

Das FormData-Objekt…

- sammelt alle Formularwerte automatisch
- codiert Sonderzeichen korrekt
- arbeitet direkt mit Name-Value-Paaren
- eignet sich viel besser als das manuelle Auslesen per .value und .checked

3. Wichtige Methoden von FormData
### 3. Wichtige Methoden von FormData

| Methode              | Zweck                                                            |
|----------------------|------------------------------------------------------------------|
| `get(name)`          | Gibt den Wert eines Felds zurück (bei mehrfachen Feldern den ersten). |
| `entries()`          | Iterator über alle Name–Value-Paare (ideal zum Durchlaufen aller Felder). |
| `append(name, value)`| Fügt ein neues Name–Value-Paar hinzu.                           |
| `values()`           | Iterator, der nur die Werte liefert.                             |

4. FormData anlegen und Werte auslesen
```js
const form = document.querySelector("#formdemo");

function formData(evt) {
  evt.preventDefault();
  const data = new FormData(form);

  const artikel = data.get("artikel");
  const stadt   = data.get("stadt");
  const txt     = data.get("txt");

  console.log("data:", artikel, stadt, txt);
}

```
Vorteil:
Sauber, kompakt, keine manuelle Navigation durch einzelne Inputs nötig.

5. Mit entries() alle Formularwerte durchlaufen

entries() ist besonders nützlich, sobald ein Formular mehr als ein paar Felder enthält.
```js
function formData(evt) {
  evt.preventDefault();
  const data = new FormData(form);
  const entries = data.entries();

  for (const item of entries) {
    console.log(item);   // item = [name, value]
  }
}
```

Ergebnis:
Du bekommst für jedes Feld automatisch ein Array:
```js
["artikel", "regenjacke"]
["stadt[]", "Rüdesheim"]
["txt", "Text …"]
…
```
Kurzfazit
- Formulare liefern Name–Value-Paare → FormData macht das Automatisch
- Codierung und Checkbox-Arrays sind typische Stolperfallen → FormData löst sie
- get() für einzelne Werte, entries() für komplette Übersicht
- Ideal für moderne Formverarbeitung und fetch()-Requests

## 12.3 Datum und Dauer – Formulareingaben
1. Datepicker in HTML

Eingabefelder wie input type="date", type="datetime-local", type="month" oder type="week" zeigen im Browser einen Kalender oder spezielle Zeitfelder.

Vorteil:

- Einheitliche und benutzerfreundliche Eingabe
- Keine manuelle Formatierung nötig
Nachteil:

- Browser-darstellung kann unterschiedlich sein
- Intern wird das Datum immer ISO-formatiert (YYYY-MM-DD für date)

Beispiel:

<input type="date" id="datepicker" value="">

2. Datum auslesen (Datepicker)

Klassische Methode: .value → liefert einen String
Mit Event Listener auf input kann der Wert sofort verarbeitet werden
```js
const date = document.querySelector("#datepicker");

date.addEventListener("input", function() {
  const d = this.value;             // String im Format YYYY-MM-DD
  document.querySelector("#userinput").innerText = d;

  const dateObj = new Date(d);      // Umwandlung in Date-Objekt
  document.querySelector("#userinput").innerText += "\n" + dateObj;
});
```

Alternative: .valueAsDate
liefert direkt ein Date-Objekt, ohne new Date()

Beispiel: 

```js
const dateObj = this.valueAsDate;
```
3. datetime-local – Datum + Uhrzeit

Eingabe liefert ebenfalls einen String
Muss für Berechnungen in ein Date-Objekt umgewandelt werden
```js
<input type="datetime-local" id="dt">

const dt = document.querySelector("#dt");

dt.addEventListener("input", function() {
  console.log(this.value);           // String z.B. "2025-11-26T15:30"
  const zeit = new Date(this.value);
  console.log("zeit", zeit);        // Date-Objekt für Berechnungen
});
```
4. Tipps für die Praxis

- Event Handler auf input fangen Änderungen sofort ab
- .value → String, .valueAsDate → Date-Objekt
- Mit new Date(string) kann jeder String aus input in ein Date-Objekt umgewandelt werden
- Optional: Attribute wie min, max, value einschränken oder Vorgaben machen