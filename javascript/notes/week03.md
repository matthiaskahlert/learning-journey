# Meine Markdown notes Woche 3

## Tag 11

## Learningfacts - Kapitel 8 - Arrays

Ein Array ist ein Objekt in denm eine Liste von Werten gespeichert ist. Man spricht die einzelnen elemente über ihren Index an. Der Index startet bei 0.
const arr = [123,1234,465,27635];

Elemente können Zahlen sein, aber auch Strings, Objekte somit auch Andere Arrays.
Man kann auch Datentypen mixen
const arr2 = ["Foo", 234, arr, "bar", true];

Man kann Arrays auch mit einem Konstruktor erstellen:
const stoff = new Array("Leinen", "Baumwolle", "Seide");
const wahl = `Ich bevorzuge ${stoff[1]} für T-shirts`;
console.log("wahl", wahl);

### 8.2 Arraymethoden
Man braucht Arraymethoden im Document Object Model (DOM).
Man kann sich spezielle ArrayMethoden in der Browserkonsole anzeigen lassen mit namen des arrays gefolgt von einem punkt. Dies ginge auch mit Object.getPrototypeOf(myarray)
Manche Methoden Ändern das array und sind daher als destruktiv zu bezeichnen.


wichtige sind:
array.push() - Einfügen am Ende eines Arrays
const stoffLen = stoff.push("Viskose", "Jeans")
array.pop() - entfernt letzten eintrag und goibt ihn aus
array.unshift() - Einfügen am Anfang des Arrays - Ähnlich wie push
array.shift() - Erstes Element Löschen
slice(startIndex, endIndex) - Teil des arrays kopieren. der endIndex ist exclusiv, also wird nicht mit aufgeführt.
array.splice(startindex, Anzahl der zu entfernenden Elemente) - Ausschneiden von Elementen
array.reverse() - Umkehrung der Elementreihenfolge.
array.includes() - prüft ob wert vorhanden, gibt true oder false zurück
array.indexOf() - index des ersten vorkommens eines Wertes - oder gibt -1 zurück, wenn nichts gefunden
array.lastIndexOf() - letzter Index der dem angegebenen wert entsppricht - oder gibt -1 zurück, wenn nichts gefunden

#### arraymethoden verketten
analog zu Strings und Objekten kann man Arrays verknüpfen.
Es kommt darauf an, dass der rückgabewert mit der folgenden methode kompatibel ist.

const farben = ["grün", "blau", "rot", "gelb", "schwarz", "weiß"];
const str = farben.splice(2,5).reverse().toString();
console.log("str:", str);

join() - Array Elemente zu einem String zusammenführen
array.join() wandelt array Elemente in einen String um, man kann trennzeichen angeben.
const satz = ["Nutze", "den", "Tag"];

console.log(satz.join(""));

#### Array Destructure und Rest-Operator

weiter mit Seite 133 am Montag.




