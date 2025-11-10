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
Es kommt darauf an, dass der Rückgabewert mit der folgenden Methode kompatibel ist.

const farben = ["grün", "blau", "rot", "gelb", "schwarz", "weiß"];
const str = farben.splice(2,5).reverse().toString();
console.log("str:", str);

join() - Array Elemente zu einem String zusammenführen
array.join() wandelt array Elemente in einen String um, man kann trennzeichen angeben.

    const satz = ["Nutze", "den", "Tag"];

console.log(satz.join(""));

#### Array Destructure und Rest-Operator

Mit sestructure kann man arrayinhalte variablen zuweisen:
```js
let a, b, rest;
[a, b] = [10, 20];

console.log(a);
// Expected output: 10

console.log(b);
// Expected output: 20

[a, b, ...rest] = [10, 20, 30, 40, 50];

console.log(rest);
// Expected output: Array [30, 40, 50]
```

| Kontext - Name                                | Bedeutung                    |Beispiel                                                       |
| --------------------------------------------- | ---------------------------- | ------------------------------------------------------------- |
| Beim Destructuring - Rest-Operator            | sammelt den Rest             | const [a, ...b] = [1,2,3] → b = [2,3]                         |
| Beim Erstellen / Aufrufen	- Spread-Operator   | entpackt Arrays oder Objekte | const arr = [1,2,3]; const neu = [0, ...arr, 4] → [0,1,2,3,4] |

Methode:
Array.isArray() - prüfen ob ein objekt ein array ist

### 8.3 Arrays sortieren
array.sort() sorttiert arrays in aufsteigender Reihenfolge, es gibt den die sortierung basiert auf unicode index. Umlaute wandern ans ende, zahlen vor buchstaben, groß vor kleinschreibung etc.

wenn keine strings vorliegen kann man die vergleichsfunktion nutzen

const numerischesArray = [3,45,567456,34,13541345,6,468,2,234];
numerischesArray.sort()
console.log(numerischesArray); // [13541345, 2, 234, 3, 34, 45, 468, 567456, 6]
dies zeigt, für numerisches sortieren braucht man eine vergleichsfunktion:
numerischesArray.sort((a,b) => a-b);

ich sage JavaScript hier: z.B. vergleiche (3, 45) → 3 - 45 = -42
negativ
a (3) kommt vor b
Dies passiert so lange bis das array sortiert ist.

### 8.4 Arrays verschachteln und zusammenführen

array.push() hängt ein neues Element an das ende eines arrays. Wenn man nun ein array als element ousht, ist das array teil des arrays.

const sortiert = ['%', '.rose', 28, 'Juwel', 'drei', 'Ärger', 'über']
const namen = ["Edda", "Kjell", "Matze"]
sortiert.push(namen);

Wenn ich nun auf ein element des arrays zugreifen will, brauche ich zwei positionen, den indes indem das array ist und die indexposition des gewünschten elements.

console.log(sortiert[7[3]]);


Man kann arrays auch folgendermaßen zusammenführen
const blumen = ["Rosen", "Vergissmeinicht"];
const pflanzen = ["Gänseblümchen", "Löwenzahn"];
const newArr = [blumen,pflanzen];
console.log(newArr);
console.log(newArr[1][1]);

#### 8.4.2 array.concat
array.concat() - Elemente aneinanderhängen
let x = blumen.concat(pflanzen)

concat() fügt Arrays zusammen, aber nur eine Ebene tief. Verschachtelte Arrays bleiben verschachtelt.

#### 8.4.3 spread-Operator – Array-Elemente aneinanderhängen
statt concat mann man auch den spread operator nutzen

const arr = [1,2,3]; 
const neu = [0, ...arr, 4]; // ergibt [0,1,2,3,4]
let y =[...blumen, ...pflanzen];

s... kann iterierbare Objekte auseinanderziehen.

Iterierbare Objekte sind z. B.: Arrays, Strings, Sets, Maps.

man kann mit spread Elemente eines Arrays auf die
Argumente einer Funktion verteilen:
function addiere (a,b,c){
    return a+b+c;
}
const zahlen = [3,4,5];

const ergebnis = addiere (...zahlen);
cosole.log(ergebnis);

array.flat()
array.flat erzeugt ein neues array, welchesverschachtelte arrays auf einer ebene angibt. es hat einen optionalen parameter depth, der die tiefe angibt bis zu der das array abgeflacht wird.

const arr4 = [100,86[17,200,3], [0,14], 200];
const newArr4 = arr4.flat(2);
console.log(newArr4);