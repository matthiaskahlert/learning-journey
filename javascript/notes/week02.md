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

