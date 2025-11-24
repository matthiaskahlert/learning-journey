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

});```