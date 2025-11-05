# Meine Markdown notes Woche 1

## Tag 6

## Learningfacts - Kapitel 6 - Funktionen

Funktionen sind gruppierte Anweisungen. man definiert sie mit dem Schlüsselwort function, was den Anweisungen in geschweiften Klammern einen Funktionsnamen zuweist.
```js
function
{
    ...
}
```
Sie bilden einen block von anweisungen, die das script mehrfach nutzen kann.
Man kann Funktionen definieren, bevor man sie aufruft. Funktionen werden vom interpreter ignoriert, bis sie aufgerufen werden.

Zur Reihenfolge von funktionen lässt sich sagen, dass JavaScript Funktionen ausführt, in der Reihenfolge in der sie aufgerufen werden (und nicht in der Reihenfolge, in der sie definiert werden). Man darf funktionen aufrufen, bevor sie definiert wurden.

```js
function hallo() {
    console.log(`Hallo Welt!`);
}

hallo()

```
### Parameter und Argumente
In den runden Klammern kann man der Funktion noch Parameter übergeben wobei im folgenden Beispiel a und b die Parameter sind und 500 und 234 die Argumente.


```js
function rechnen (a,b){
    const ergebnis = a - b

    console.log(`Es wird berechnet, wieviel ${a} -${b} ist.
    Das Ergebnis ist ${ergebnis}.`);
}

rechnen(500,234);
```
### return - Rückgabewert von Funktionen

Das return statement / Schlüsselwort beendet die Ausführung einer Funktion und gibt den Wert an den Funktionsaufruf zurück.
Der console.log im Beispiel wird nicht ausgeführt, denn mit return wird die Funktion beendet. Nur mit Rückgabewert (return ...) kann ich Variablen außerhalb der funktion das Ergebnis zuweisen. Würde die funktion keinen Wert zurückgeben, wäre das Ergebnis undefined.
```js
function rechnen (a,b){
    const ergebnis = a - b
        return ergebnis;
    console.log(`Es wird berechnet, wieviel ${a} -${b} ist.
    Das Ergebnis ist ${ergebnis}.`);
}



function teilen (a,b){
    const wert = a / b;
    return wert;
    console.log("wert", wert);
}
const divi = teilen(110,700);  
console.log("divi", divi, typeof divi); // ohne den rückgabewert wäre divi undefined.
```

Wenn eine Funktion einen Parameter erwartet, dieser aber nicht übergeben wird,
kann man einen Standardwert (Default-Wert) definieren, der automatisch verwendet wird.
Mit einem default Parameter wird der Standardwert direkt in der funktionsdefinnition angegeben.
```js
function publishPost3(titel3 = "Caspar David Friedrichs schönste Werke"){
    return  `Besuchen sie unsere Ausstellung: ${titel3}.`;
}

console.log(publishPost3()); // Besuchen Sie unsere Ausstellung: Caspar David Friedrichs schönste Werke.

console.log(publishPost3("Franz Marc´s blaue Pferde")); // Besuchen Sie unsere Ausstellung: Franz Marc´s blaue Pferde.

``` 

return inner;	gibt die Funktion inner selbst zurück
return inner();	würde das Ergebnis eines Aufrufs von inner() zurückgeben


### verschachtelte Funktionen

Funktionen können innerhalb anderer Funktionen liegen.
Variablen der *inneren Funktion* sind für die *äußere Funktion* undefined, während Variablen der *äußeren Funktion* für die *innere Funktion* sichebar sind!
```js
function outer() {
  function inner() {
    console.log("Ich bin jetzt von außen aufrufbar!");
  }

  return inner; // gibt die Funktion selbst zurück als Wert
}

const innerFunction = outer(); // die Variable innerFunction bekommt den Rückgabewert von outer() zugewiesen,  outer() wird ausgeführt, inner() wird zurückgegeben
innerFunction(); //  funktioniert jetzt von außen
```


### Funktionsausdrücke - function expressions

Wird das Ergebnis einer Funktion direkt einer Variablen zugewiesen, haben wir einen Funktionsausdruck.
```js
const multiply = function(a, b) {
    return a * b;
};
```
Funktionsausdrücke haben normalerweise keinen Namen und werden daher auch als anonyme Funktionen bezeichnet.
Man könnte sie aber auch nenennen also zb 
```js
const multiply = function name(a,b) { // dann würde man von einer named function expression sprechen.
    return a * b;
};
```
Von aussen würde man die Funktion weiterhin über multiply ansprechen, aber von innen kann man über name() auf sie rekursiv zugreifen.

function expressions müssen hinter der schießenden geschweiften klammer mit semikolon abgeschlossen werden, da sie ein ausdruck sind und keine deklaration:

Einfache Eselsbrücke

Deklaration: function … { … } → einfach schreiben, kein ;

Ausdruck: const … = function() { … }; → wie jede andere Variable abschließen → ;

### 6.5 Arrow Funktionen

Die Arrow Funktion hat gegenüber der klassischen Schreibweise den Vorteil, dass sie kompakter ist und ein implizites return hat.
ein 
```js
function summe (a,b) {
    return a+b;
} 
```

wird zum 
```js 
const summe = (a,b) => a + b;
```
Wenn die Funktion nur einen Parameter hat, dann fallen auch die runden klammern weg:
```js
const euro = x => x + " €";

console.log(euro(15));
 // Diese funktion klassisch geschrieben
function temparatur(celsius) {
    return (celsius * 1.8) + 32;
 }

 const temparatur = function(celsius)
 {
     return (celsius * 1.8) + 32;  
 };
// wird mit nutzung von arrow zu

const temparatur = celsius => (celsius * 1.8) + 32;



```



#### Arrow funktionen mit Objekten als rückgabewert
Man muss auf die Klammeretzung achten, wenn man arrow funktionen nutzen will um objekte zurückzugeben. Arrow Funktionen sitzen ja genau so in geschweiften Klammern wie Objekte. 
Objekte in arrows müssen immer in runde klammern: () => ({ ... })

```js
const counter = [1,2,3,4,5];

counter.forEach(function(n) { console.log(n); }); // klassische Schreibweise
counter.forEach(n => console.log(n));            // Arrow-Funktion
counter.forEach(n => console.log(n * 2));       // Elemente weiterverarbeiten
```


### 6.6 Debugging

Debugging ist die Kontrolle des Programmflusses um Fehler zu finden, mit breakpoints kann man schritt für schritt die Werte der Variablen und berechnungen durchgehen:
1. Öffne die Developer Tools (F12 oder Rechtsklick → „Untersuchen“).
2. Gehe zum Sources-Tab.
3. Setze Breakpoints auf die gewünschten Zeilen.
4. Lade die Seite neu.
5. Der Code stoppt an den Breakpoints, du kannst:
6. Step over: nächste Zeile ausführen ohne in Funktionen zu springen.
7. Step into: in Funktionen hineingehen und Zeile für Zeile prüfen.
8. Step out: eine Funktion verlassen und zum übergeordneten Scope zurückkehren.
9. So kann man Werte von Variablen überwachen und Berechnungen nachvollziehen.


## Tag 8

## Learningfacts - Kapitel 7 - Objekte
### 7.1 Grundlagen

Wenn die Logok von Programmen komplexer wird braucht man Objekte. Sie sind Paare von Schlüsseln und Werten. Das Document Object Model bildet alle Elemente der Webseite
als JavaScript-Objekt ab.
```js
const  objekt = {
    schlüssel1:    wert,
    schlüssel2:     wert,
    schlüssel3:     wert        // Das Komma hinter dem letzten Wert kann entfallen
}

const kinofilm = {
    title:          "Der Herr der Ringe",
    actor:          "Cate Blanchett",
    published:      2001
    "Erster Teil":  "Die Gefährten"
}
```
Die Eigenschaften des Objekts werden innerhabl der geschweiften Klammern deklariert. Die schlüsselnamen folgen den Regeln von Variablen, also klein beginnen, caseCamel, keine Zahl am anfang, keine Bindestriche, Schlüssel dürfen im Gegensatz zu Variablen aber leerzeichen beinhalten, brauchen dann aber hochkommas.

#### dot Notation
von aussen angesprochen werden eigenschaften mit dot-notation:
const x = kinofilm.title;

Nur wenn Eigenschaften mit einem Leerzeichen geschrieben werden, muss der Zugriff auf die Eigenschaft in eckigen Klammern stehen.
x = kinofilm["erster Teil"];

Objekte in Objekten
Eigenschaften können selbst Objekte sein.
```js
const kinofilm = {
    title:          "Der Herr der Ringe",
    actor:          "Cate Blanchett",
    published:      2001,
    "Erster Teil":  "Die Gefährten",
    buch:           {
        title:      "Der Herr der Ringe",
        author:     "JRR Tolkien"
    }
}

y=kinofilm.buch.author; // "JRR Tolkien
```

Elemente von Objekten ändern:
// Eigenschaft aus Objekt löschen

delete kinofilm.published;
// Eigenschaft hinzufügen
kinofilm.hasOscae = true;
// Eigenschaft ändern

kinofilm.title = kinofilm.title + " Teil 1";

Objekte können Funktionen enthalten, man nennt sie  „Methoden von Objekten“.
Der Zugriff auf die Elemente innerhalb der Funktion geschieht über das
Schlüsselwort this, gefolgt vom Dot, gefolgt vom jeweiligen Schlüssel des
Element.

```js
    play:       function(){
        console.log(`Der Film "${this.title}" entstand nach dem Buch "${this.buch.title}" von "${this.buch.author}".`);
    }
```

Regel: Wenn du mit Funktionen auf Eigenschaften des eigenen Objekts zugreifen willst, verwende IMMER this.

### for-in Schleife in Objekten

Objekte haben ihre eigene for-Schleife: for-in

for...in läuft über alle Schlüssel (property names) eines Objekts.

```js

const imgObj = {
    src:    "/media/image.jpg",
    width:  1080,
    height: 720,
    alt: "Ein Bild"
}

for (const key in imgObj){
    console.log("Object key", key); // gibt die Schlüssel des Objekts aus Object key src, key width, key height, key alt
}

for (const key in imgObj){
    console.log("Object value", imgObj[key]);
}
```

Das bedeutet:

Beim 1. Durchlauf ist key = "src"

Beim 2. Durchlauf key = "width"

Dann key = "height"

Und key = "alt"


man kann for ... in auch auf Arrays anwenden, da sie auch Objekte sind.
```js

const imgArr = [1060, 1280, 1440, 1980];
for (const key in imgArr){
    console.log(`${key}, ${imgArr[key]}`);
```

### 7.3 Das Object document

Scripte auf Webseiten greifen auf das Document Object Model (kurz DOM) zurück. Das DOM beschreibt die Elemente einer Webseite als Objekt.
Das DOM muss nicht angelegt werden.
HTML elemente wie head und body sind über das DOM ansprechbar.

```js
const head = document.head;
console.log(head)
```

***document*** ist also das Objekt, das alle Elemente der Webseite enthält!
JavaScript kann über das DOM mit der Webseite reden, zb elemente auswählen, Inhalt ändern, Attribute Ändern. das DOM ist DIE verbindung zwischen HTML und JavaScript. Alles im Document Object Model ist ein Objekt, das JavaScript manipulieren kann.

#### querySelector


querySelector ist eine Methode des DOM mit der man ein einzelnes HTML Element auswählen kann.

document.querySelector() → wählt ein HTML-Element aus.


<button id="meinButton">Klick mich!</button>
const button = document.querySelector("#meinButton");
console.log(button); // zeigt das <button>-Element im Console-Log

#meinButton → selektiert das Element mit der ID meinButton.

.klasse → selektiert Elemente nach CSS-Klasse.

tagname → selektiert nach HT

ML-Tag (z. B. p, div).
Merksatz: querySelector = "Finde das Element, das zu diesem CSS-Selektor passt."

#### addEventListener


addEventListener ist eine Methode eines Elements, mit der du auf Ereignisse reagierst, z. B. Klicks, Mausbewegungen oder Tastendrücke.

element.addEventListener() → reagiert auf Ereignisse, die auf diesem Element passieren.

```js
const button = document.querySelector("#meinButton");

button.addEventListener("click", function() {
  alert("Button wurde geklickt!");
});

```
"click" → das Event, auf das du reagieren willst.

function() { ... } → die Funktion, die ausgeführt wird, wenn das Event passiert.

Merksatz: addEventListener = "Wenn dieses Ereignis passiert, führe diese Funktion aus."

💡 Tipp: querySelector + addEventListener sind ein Dream-Team: Zuerst das Element auswählen, dann sagen, was passieren soll, wenn der Nutzer damit interagiert.

### 7.4 Konstruktor Funktionen
Eine Konstruktorfunktion ist im Grunde eine Vorlage (Blueprint), mit der du viele ähnliche Objekte automatisch erzeugen kannst.

Die klassische Schreibweise zum Anlegen von Objekten sind mit geschweiften klammern 

```js
const produkteA {
    kategorie:  "Haushalt"
    produktName:    "Haarbürste"
}
```
oder mit der dot.-schreibweise

```js
const prudukteB {
    produktB.produktName = "Bürste klein"
    produktB.kategorie: "Haushalt"
}
```
Eina andere Methode kommt zum Einsatz, wenn das Skript eine gruppe von zzusammenhängenden Objekten erzeugen soll.

JavaScript rufe eine Konstruktor Funktion mit dem Schlüsselwort new auf.

```js
const produkt = new Object();
```
Elemente werden dann mit dot.Notatoion deklariert.
Mit der Konstruktor Funktion kann man eine Vorlage also eine Blaupause für Objekte anlegen. Hier dient das Schlüsselwort this nicht als wert sondern als platzhalter, das this bezieht sich auf das neue Objekt, das nach der Konstruktor definition erzeugt wird.
```js
function Produkt(kategorie, name, bild, showImage) {     // definiert die Konstruktorfunktion
    this.kategorie = kategorie;                         // legt fest, dass jedes Objekt eine eigenschaft kategorie bekommt
    this.name = name;
    this.bild=bild
    this.showImage = function(){                        fügt jedem Objekt eine eigene Methode hunzu
        console.log(`img src="${this.bild}"
        alt="${this.name}">`);
    }
}
```
Erst das erzeugen mit dem Schlüsselwort new vor dem aufruf der Konstruktor Funktion weist den eigenschaften den Wert zu.
```js
const p1 = new Produkt("Haushalt",
"Bürste Minimale",
"product-01.jpg");
const p2 = new Produkt("Elektronik", "Föhn","product-01.jpg");
p1.showImage(); //// soll dies ausgeben: <img src="product-01.jpg" alt="Bürste Mini"> aus
console.log(p2);

```
Die namen von Konstruktor-Funktionen sollen mit einem Großbuchstaben beginnen.


### 7.5 Klassen

Eine Klasse ist wie eine Blaupause für Objekte, man definiert einmal was ein Objekt haben soll und kann danach beliebig viele Objekte erzeugen.
Mit extends kann eine Klasse die Methoden und Eigenschaften einer anderen Klasse erben.

```js
class Auto {
  constructor(marke, farbe) {
    this.marke = marke;
    this.farbe = farbe;
  }

  zeigeInfo() {                 // Alles, was in einer Klasse als Name + Klammern {} steht, ist eine Methode, auch ohne function davor.
    console.log(`${this.marke} ist ${this.farbe}`);
  }
}

const meinAuto = new Auto("BMW", "rot");
meinAuto.zeigeInfo(); // BMW ist rot


class ElektroAuto extends Auto {
  constructor(marke, farbe, batterie) {
    super(marke, farbe); // ruft die Konstruktorfunktion von Auto auf
    this.batterie = batterie;
  }

  zeigeBatterie() {
    console.log(`Batteriegröße: ${this.batterie} kWh`);
  }
}

const meinEAuto = new ElektroAuto("Tesla", "blau", 75);
meinEAuto.zeigeInfo(); // Tesla ist blau
meinEAuto.zeigeBatterie(); // Batteriegröße: 75 kWh

```
ElektroAuto erbt alles von Auto (marke, farbe, zeigeInfo) und fügt noch eigene Sachen hinzu (batterie, zeigeBatterie).Beim anlegen von Methoden braucht man das Schlüsselwort function nicht mehr. Alles, was in einer Klasse als Name + Klammern {} steht, ist eine Methode, auch ohne function davor.

Wenn sich Klassen Ändern, erben auch erzeugte Klasseninstanzen diese Änderungen.

### 7.6 Datum und Zeit

es gibt ein eingebautes Objekt namens Date. es wird mit new Date() erzeugt.

```js
const heute = new Date();
console.log(heute); //Wed Nov 05 2025 14:07:30 GMT+0100 (Mitteleuropäische Normalzeit)
```
folgende Syntax wird angewendet, wobei der Monat in JavaScript bei 0 beginnt!
const datumGestern = date(jahr, monat, tag, stunden minuten, sekunden, millisekunden)

const dateGestern = new Date(2024,0,1,1,12,55,123);
console.log(dateGestern);

Leichtere Schreibweise:
const datum = new Date("2024-01-24 13:53:12")

Das Datumsformat ist auch Lokalen Anforderungen unterworfen, im diesen zu entsprechen, kann man toLocaleString() nutzen um die Zeitangabe zu konvertieren.
const meeting = new Date().toLocaleString();
console.log("Meeting", meeting);        Meeting 5.11.2025, 14:19:50

toLocaleString() hat zwei optionale Parameter
einen String für die JEweilie Sprache wie z.B. de-DE und options für Stil eigenschaften (f+ull, long, short)

const week5 = new Date().toLocaleString("de-DE, {weekday: "short"});

Das Inntl.DateTimeFormat-Object kann genutzt werden um herauszufinden in welcher Zeitzone ich mich gerade befinde.

const f = new Date();
f = Intl.DateTimeFormat().resolvedOptions().timeZone;
console.log(date);



