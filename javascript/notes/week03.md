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

array.pop() - entfernt letzten eintrag und gibt ihn aus
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

Mit destructure kann man arrayinhalten variablen zuweisen:
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

array.push() hängt ein neues Element an das ende eines arrays. Wenn man nun ein array als element pusht, ist das array teil des arrays.

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
array.flat erzeugt ein neues array, welchesverschachtelte arrays auf einer Ebene angibt. es hat einen optionalen parameter depth, der die tiefe angibt bis zu der das array abgeflacht wird.

const arr4 = [100,86[17,200,3], [0,14], 200];
const newArr4 = arr4.flat(2);
console.log(newArr4);
### 8.5 Arrays durchlaufen


for-Schleifen sind gut geeignet um durch arrays zu laufen, sie sprechen jedes element einzeln an.
Beispiel:
```js
const arr = ["Kirschen", "Pfirsiche", "Erdbeeren"];
const l = arr.length;
for (let i = 0; i<l; i++){
    console.log(arr[i]);
}
```
#### Vertiefung for..of Schleife
for for...of schleife kann über arrays, maps, sets, strings und sog. NodeLists und HTML collections laufen. Allerdings nicht über Objekte, da sie keinen Index haben.

```js
const lektion = ["Mathe", "Deutsch", "Physik", "Sport"];
for (const item of lektion){ // item ist eine variable!
    console.log(item);
}

const json = [
    {"author": "Austen Jane", "book": "Mansfield Park"},
    {"author": "Pratchet, Terry", "book": "Total verhext"},
    {"author": "Arnim, Elizabth", "book": "Verzauberter April"}
];
for (const elem of json){
    console.log(`${elem.book} ist von ${elem.author}`);
    
}
```

man kann bei for..of auch break, continue und return nutzen.
kurze wiederholung:
break - bricht die aktuelle Schleife oder ein switch sofort ab.
continue - überspringt den Rest der aktuellen iteration.
return - beendet die funktion und gibt evtl einen Wert zurück.

```js
const city = ["Amsterdam", "Berlin", "Göttingen", "Bielefeld", "Hannover"];
    for (const elem of city){
        console.log(elem);
      if (elem === "Göttingen"){
        console.log(`Bis hierhin und nicht weiter, ${city[3]} existiert nicht xD`);
        break;
    } 
}
```
for .. of mit Index: entries()
Im folgenden Beispiel wird der index der for..of Schleife ebenfalls gebraucht.
Der Zugriff erfolgt über die Methode entries()
```js
const arr = [[128, 156],[32,33],[200,400]];
for (const [index, elem] of arr.entries()){
    console.log(`${index} . ${elem}`);
    for (const [idx, item] of elem.entries() ){
        console.log(`${index}.${idx}:${item}`);
    }
}
```
arr.entries() verleiht der äußeren Schleife einen index, in der inneren Schleife ist key der index.

#### forEach()
bei forEach() muss man die länge des arrays nicht mehr kennen.
forEach ruft für jedes Element des Arrays automatisch eine Callback-Funktion auf.

array.forEach(
    function(currentValue, index, array), thisArg);

forEach führt eine sogenannte Callback funktion aus, welche drei Parameter hat: 
currentValue (erforderlich) - aktuelles Element
index (optional) - index des aktuellen elements
array (optional) - das gesammte array


Callback ist eine Funktion, die an eine andere Funktion übergeben wird, damit sie dort später aufgerufen wird.

Also:
Du gibst eine Funktion weiter, und die andere Funktion ruft sie zu einem passenden Zeitpunkt wieder auf („call back“ = „zurückrufen“).

Einfaches Beisiel:
arr.forEach((elem) => { console.log(elem)});

statt elem könnte hier auch eine andere variable stehen

const score = [17, 129, 27, 8, 51, 99, 12];
    score.forEach((elem)=>{
        if (elem>50) console.log(elem)
    });




Die Callback funktion wird für jedes element durchgeführt da sie als argument der forEach funktion angegeben wird.

Rückgabewert - forEach gibt nichts zurück (undefined)

const images = ["tulpe.jpg","rose.jpg","veilchen.jpg","nelke.jpg", ];
images.forEach(
    (elem, index)=>{
        const tag = <img src="${elem}"> ;
        console.log(`i:${index}`, tag);
        });

forEach kann auch einfach den namen einer Funktion aufrufen.

const images = ["product01.jpg", "product02.jpg"];
function insertGallery(item) { // funktion die ein bild rstellt und es in den container Gallery hinzufügt
        const img = document.createElement("img");
        img.src = "images/" + item;
        document.querySelector("#gallery").append(img);
    }
images.forEach(insertGallery);

#### Mit forEach über Arrays von Objekten iterieren
Dies wird oft genutzt wenn man mit dynamischen anwendungen auf dem Server kommuniziert und Daten z.B. im JSON Format übertragen werden.
```js
const imagesObj = [
    {path: "flowers-01.webp", width: 170 },
    {path: "flowers-02.webp", width: 170 },
    {path: "flowers-06.webp", width: 170 },
    {path: "flowers-04.webp", width: 170 }
];
imagesObj.forEach((obj)=>console.log(obj)); // so gibt forEach die vier Objekte zurück. log: {path: 'flowers-01.webp', width: 170}
```
Um auf die Werte der Elemente zuzugreifen, muss nur der name des Elements aufgenommen werden:
```js
imagesObj.forEach((obj)=>console.log(obj.path));  // log: flowers-01.webp ...
```

#### array.map()
array.map schiebt alle elemente eines arrays in eine funktion und gibt einen neuen wert für ein neues array zurück.
das neue array hat dieselbe anzahl an elementen wie das orginal array.
```js
const preise = [3,22,11,30];
const mwst = preise.map(number=>number*19/100);
console.log("mwst", mwst); //mwst (4) [0.57, 4.18, 2.09, 5.7]
```
Das orginal array bleibt unangetastet, es wird auf das neue array gemappt, wenn es auf zahlen, strings und Booleans angewendet wurd. 
map() erstellt immer ein neues Array, aber bei Objekten kopiert es nur die Referenzen, nicht die Objekte selbst.
Willst du die Objekte unverändert lassen, musst du sie explizit klonen.

beispiel:  halbiere die Mehrwertsteuer für jedes zweite Produkt.
const preise = [3,22,11,30];
const geschenkt = preise.map((number,i)=>{
    if (i % 2 === 0){
        return (number * 9.5 / 100);
    } else {
        return (number * 19 / 100);
    }

});
console.log("geschenkt",  geschenkt);

map() kommt zum einsatz, wenn man nur wenige Werte eines arrays Ändern möchte.

mapping mit objekten in array:
die produkte auf platz 0 und 2 sollen 25% rabbatt erhalten

const product = [
    {name:"Waschmaschine", preis: 399.00, lager: 117},
    {name:"Kühlschrank", preis: 459.00, lager: 32},
    {name:"Backofen", preis: 244.50, lager: 98},
    {name:"Mixer", preis: 199.00, lager: 7},
    {name:"Grill", preis: 80.00, lager: 64}

];

const deal = product.map((item, idx) => {
    const obj = {};
    obj.name = item.name;
    obj.preis = item.preis;
    obj.lager = item.lager;

    if (idx === 0 || idx === 2){
        obj.preis = (item.preis - item.preis * 25 / 100).toFixed(2);
        return obj;
    }
    return obj;
});
console.log("deal", deal);
console.log(product.map(obj=>obj.name));
### 8.6 Callbacks

Wie zuvor beschrieben wird die callback funktion einer anderen funktion als argument übergeben und nur zu gegebener zeit (zb nach abschluss einer aktion) aufgerufen.
dh callback funktionen lösen nicht direkt auf ondern nur bei bestimmten ereignissen oder in bestimmten umgebungen.


#### array.filter() spezielle elemente aus arrays filtern

syntax:

const neuesArray = array.filter(callback);


Neben forEach() ist filter() auch eine funktion höherer ordnung. filter() hat ein array als Rückgabewert.


Was passiert?
filter() = „Schau dir jedes Element an, gib true/false zurück, und nur true kommt ins neue Array.“

const city = ["Amsterdam", "Berlin", "Göttingen", "Bielefeld", "Hannover", "Bonn", "Köln"];
const kurz = city.filter((name)=> name.length < 5);
console.log("Werte des Arrays mit weniger als 5 Zeichen", kurz) //Werte des Arrays mit weniger als 5 Zeichen (2) ['Bonn', 'Köln']

filter() weist den rüückgabewert einer variablen zu: kurz
die callback funktion lautet: (name)=> name.length < 5

die callback muss true oder false ergeben damit filter den wert in das neue array aufnimmt ( oder nicht).


array.forEach() oder array.map() ?

Für das Beispiel oben wäre array.forEach() komplizierter als array.filter(), da es keinen Rückgabewert hat.
Innerhalb der Callback funktion muss eine Abfrage klären, ob das jeweilige Element mit push() in das Ergebnis übernommen wird oder nicht.

const kurzMitForEach = [];
city.forEach((elem) => {
    if (elem.length > 5){
        kurzMitForEach.push(elem)
    }
});


jedes element mit array.map() bearbeiten

const preise = [68.50, 70, 120, 12, 7];

const mwst = preise.map((preis)=>preis*19/100);
console.log(mwst)

const output = preise.map(function(preis){
    return preis.toFixed(2) + " €";
});
console.log("Output:", output); // Output: (5) ['68.50 €', '70.00 €', '120.00 €', '12.00 €', '7.00 €']

zum vergleich mit array.forEach()

const result = [];
preise.forEach((preis) => {
    result.push(preis.toFixed(2) + " €");
});
console.log("map result", result);

array.map-Chaining

durch dot notation kann man mehrere mmap aufgaben verketten

const punkte = [25,9,100,400,900];

const calculus = punkte
    .map(function(p) {
        return Math.sqrt(p);
    }) // was auch immer in der ersten map-Anweisung herauskommt, geht in die zweite map-anweisung!
    .map(function(sqrt) {
        return sqrt * 2;
    })
    console.log("calculus", calsulus); //calculus (5) [10, 6, 20, 40, 60]

const preise = [75,120,127,25,90,7,18,210];
const rabatt = preise
    .filter((preis) => preis >= 100)
    .map((over)=> (over - (0.1 * over)).toFixed(2));
    console.log("rabatt", rabatt);

    beachte: das semikolin schließt die verkettung ab.


array.reduce()
die reduce funktion reduziert array inhalte auf einen einzelnen rückgabewert.
reduce: läuft über ein Array und fasst alle Elemente zu einem einzigen Wert zusammen (z.B. Summe, Produkt, Objekt), 
wobei ein Akkumulator über die Iterationen hinweg aktualisiert wird.

    const arr = [1,2,3,4,5,6,7,8,9,10];
    const initialValue = 0
    const summe = arr.reduce((previousValue, currentValue) =>
        previousValue + currentValue, initialValue // previousValue ist hier der akkumulator also der return wert der letzten iteration
    );
console.log("summe", summe);

läst man den initialValue weg, ist der erste array wert der startwert.

const summe2 = arr.reduce((prev, curr) =>
    prev + curr, 15
);
console.log("summe mit initialValue = 15", summe2);

praxisbeispiel JSON-Array filtern
reduce, filter, find und map kann man gut nutzen bei der verarbeitung von JSON-Arrays
Beispiel:
filtere alle Produkte vom typ Buch und berechne den gesammtwert im Lager

const produkte = [
    {"art": "Buch", "no":1724, "preis":"3.75", "lager":27},
    {"art": "Kalender", "no":475, "preis":"13.99", "lager":13},
    {"art": "Buch", "no":188, "preis":"14.05", "lager":28},
    {"art": "Spiel", "no":774, "preis":"22.99", "lager":4}
];

const buchwert = 
produkte.filter(function(obj){
    if (obj === "Buch"){
        return obj;
    };
    }).map(function(obj){
        return obj.preis * obj.lager;
    }).reduce(function(prev, curr)){
        return((parseFloat(prev) + parseFloat(curr)).toFixed(2))
    };
    console.log("buchwert", buchwert);


### 8.8 Sparse Arrays - Arrays mit Lücken

const arr1 = [1,,3];
console.log(arr1[1]); // undefined

arr1[100]=200.96
console.log("arr1 mit Index100",arr1);
for (let i = 0; i<arr1.length; i++) {
    console.log (i, arr1[i]*19/100 + " ");
}
beim erstellen oder vergeben von indizes erhält man leicht arrays mit lücken.
for schleifen behandeln auch die lücken
forEach hingegen nutzt nur die besettzten arraywerte
arr1.forEach((elem,index) => {
    console.log(index, elem * 19 / 100);
});

## JSON - Java Script Object Notation

### 9.1 JSON-Objekte und JSON-Arrays

APIs (Application Program Interface) sind die Schnittstellen zwischen Programmen, Java Script kann hier viele Aufgaben erledigen um den Datenfluss zu gewährleisten, z.B. bilder aus einer Cloud laden und im CMS anzeigen.
JSON ist ein Austauschformat für strukturierte daten.
Beispiel11:
```js
{
    "titel": "Mansfield Park",
    "published":    "1814",
    "seiten":380
}
```
JSON folgt de Regeln wie Objekte in JavaScript geschrieben werden aber es gibt einige Unterschiede:

Der Schlüssel muss in JSON in doppelten Hochkommas geschrieben werden!
Strings in Werten müssen in doppelten Hochkommas geschrieben werden (also keine backticks).
Zahlen dürfen in JSON nicht mit einer 0 beginnen (falls es eine Rolel spielt muss = als String geliefert werden).
In Javascript dürfen Zahlen auch mit einem punkt Eenden, in JSON geht das nicht.
in JSON: Nach dem letzten Element darf kein Komma stehen

Oft liegen Arrays mit mehreren verschachtelten JSON Objekten vor. JSON Dateoien werden als .json gspeichert.
```JSON
const jsonObj = {
    "author": "austen",
    "firstname": "Jane",
    "books": [
        {"title": "Mansfield Park", "published": 1814},
        {"title": "Stolz und Vorurteil", "published": 1813},
        {"title": "Emma", "published": 1816},
    ]
}
```
Folgend ist ein JSON Array:

```JSON
const jsonObj = 
[{
    "author": "austen",
    "firstname": "Jane",
    "books": [
        {"title": "Mansfield Park", "published": 1814},
        {"title": "Stolz und Vorurteil", "published": 1813},
        {"title": "Emma", "published": 1816}
    ]
}, {
    "author": "Pratchett",
    "firstname": "Terry",
    "books": [
        {"title": "Total verhext", "published": 1991},
        {"title": "Lords and Ladys", "published": 1992},
        {"title": "Ruhig Blut", "published": 1996}
    ]
}]
```

Nun haben wir eine Kommagetrennte Liste mit JSON.Objekten.
Jeder Wert selbst kann wieder ein Objekt oder ein array sein.

### 9.2 JSON-Objekte in Strings umwandeln

#### JSON.parse()

JSON kommt meist über die url eines API oder liegt als Datei als Folge von Zeichen.
Zwecks Datenaustausch muss JavaScript diesen gelieferten String mit JSON.parse() in eine JSON Struktur umwandeln.
Umgekehrt sendes ein Skript Daten mit JSON.stringify() als String an die Anwendung auf dem Server.


JSON -> JSON.parse() -> JavaScript Objekt
JavaScript Objekt -> JSON.stringify() -> JSON

String
`{"author": "austen","firstname": "Jane","books": [{"title": "Mansfield Park", "published": 1814},{"title": "Stolz und Vorurteil", "published": 1813},{"title": "Emma", "published": 1816},]}`

Objekt
{
    "author": "austen",
    "firstname": "Jane",
    "books": [
        {"title": "Mansfield Park", "published": 1814},
        {"title": "Stolz und Vorurteil", "published": 1813},
        {"title": "Emma", "published": 1816},
    ]
}
JSON gibt es über alle Sprachen hinweg, wobei JavaScipt unnd Python über native Bordmittel verfügen, während andere Sprachen wie Java zusätzliche Bibliotheken benötigen um mit JSON umzugehen.
#### Datenfluss
Oft kommen die Daten aus einer Datenbank auf dem Server und werden von einer PHP Anwendung als JSON-String aufbereitet.
Die Anwendung auf der Webseite holt die Daten z.B. mit einem
XMLHttpRequest oder einem Fetch-API und wandelt sie mit JSON.Parse() in ein Objekt um.

Grundprinzip: String wird an eine hilfsmethode übergeen, die eine Datenstruktur zurückgibt.
```JSON
const books = `[{"author": "austen","firstname": "Jane","books": [{"title": "Mansfield Park", "published": 1814},{"title": "Stolz und Vorurteil", "published": 1813},{"title": "Emma", "published": 1816}]}, {"author": "Pratchett","firstname": "Terry","books": [{"title": "Total verhext", "published": 1991},{"title": "Lords and Ladys", "published": 1992},{"title": "Ruhig Blut", "published": 1996}]}]`;
const booksParsed = JSON.parse(books);
console.log(booksParsed);

console.log(booksParsed[1].author);
console.log(`${booksParsed[1].firstname} ${booksParsed[1].author}`);
```
JSON.parse() hat in dem String automatisch das array von Objekten erkennt.


#### JSON.stringify()

Wenn das Sktipt Daten an den Server sendet oder im Browser des users speichert, müssen diese Daten as String gesendet / gespeichert werden.
JSON.stringify() sorgt dafür, es konvertiert Daten in eine JSON-formtierte Zeichenkette.
