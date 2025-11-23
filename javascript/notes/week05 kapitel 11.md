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

JavaScript selbst, besonders bei addEventListener oder element.on…, müssen die Eventnamen aber immer lowercase sein.

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