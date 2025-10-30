// ein Objekt kann mehr als einen Wert speichern, zb einen String, Number und Boolean.
//Man erkennt das objekt an den geschweiften Klammern
const kurs = { 
    title:      "Stricken für Anfänger",
    coach:      "Julia",
    places:     12,
    started:    true,
    location:   "Hamburg",
}

kurs.places = 14;
kurs.title = "Stricken für Anfänger - Teil II";
console.log("kurs", kurs, typeof kurs);


//Das Objekt Math kann man direkt verwenden z.B. um eine Variable wie PI zu erzeugen:
const pi = Math.PI;
console.log("pi",pi); //log:pi 3.141592653589793
console.log("Math", Object.getOwnPropertyNames(Math));


// Würfelspiel mit Math.random() mit for-Schleife
// Ein Würfelspiel braucht Zahlen zwischen 1 und 6. Math.random() * 6 erzeugt eine Zahl zwischen 0 und 5,99. 
// um die Zahlen zwischen 0 und 1 zu entfernen, wird eine 1 dazugezählt. Math-trunc entfernt die Nachkommastellen.
for (let i=0; i<12; i++) {    //Variable i wird erstellt, sie darf nicht größer als 12 sein, ohne diese Begrenzung würde die schleife nicht stoppen, und i++ zählt immer einen rauf
    console.log("Math Random", Math.trunc(Math.random()*6)+1);
}

// Übungen: 
// 1. Welche Methode gibt die größte der Zahlen 20,5,110 zurück
// 2. Wie kann math die ganze Zehl von 2,7 zurückgeben
// 3. Welche Methode berechnet die Quadratwurzel von 2


//1.
console.log("Übung 1:",Math.max(20,5,110))
// 2.
let zwei = 2.7
console.log("Übung 2:", Math.trunc(zwei)); //ich benutze Math.trunc - es nimmt nur den Wert vor dem Komma, Math.floor ginge auch, dort würde ABgerundet werden, was bei Negativen Zahlenn zur kleineren Zahl führen würde, also -2.7 würde zu -3 werden
//3
console.log("Übung 3_1:", Math.SQRT2); // Konstante wird abgerufen
console.log("Übung 3_2:", Math.sqrt(2)); // Hier wird berechnet

// folgend ein performance test ob das berechnen oder das abrufen der konstante schneller ist

let summe=0
console.time("Math.sqrt(235567)")
for (let i = 0; i <100000000; i++){summe+= Math.sqrt(235567)}
console.timeEnd("Math.sqrt(235567)"); //log: Math.sqrt(235567): 1146.843017578125 ms
summe=0
console.time("Math.SQRT2")
for (let i = 0; i <100000000; i++){summe+= Math.SQRT2}
console.timeEnd("Math.SQRT2"); //log:Math.SQRT2: 1057.427001953125 ms



// Zuweisungen
let x = 42
console.log("Einfach zuweisen", x);
x+=8;
console.log("x+=8:", x); // x+=8: 50
x-=10;
console.log("x-=10:", x); //x-=10: 40
x*=10;
console.log("x*=10:", x); //*=10: 400
x/=16;
console.log("x/=16:", x); //x/=16: 25
x%=7
console.log("x%=7:", x); //x%=7: 4
x**=3;
console.log("x**=3:", x); //x**=3: 64

// Vergleichsoperatoren

let y1 = 5;
let y2 = `5`;
console.log(y1==y2); //true - es wird auf den selben wert geprüft, obwohl eine der variablen ein string ist
console.log(y1===y2); //false - es wird auf wert und datentyp geprüft
console.log(y1!=y2); //false - es wird geprüft ob der wert von y1 nicht dem wert von y2 entspricht, beide werte sind aber gleich daher ein `false`
console.log(y1!==y2); //true - es wird geprüft ob der wert und der datentyp von y1 und y2 nicht gleich sind, werte stimmen überein, datentypen aber nicht, daher sind sie unterschiedlich und somoit `true`


let x1 = 128 >100
console.log("x = 128 >100", x1); //x = 128 >100 true
x1 = 200 < 100
console.log("x1 = 200 < 100", x1); //x1 = 200 < 100 false
x1 = 100 >= 50;
console.log("x1 = 100 >= 50;", x1); //x1 = 100 >= 50; true
x1 = 20 <= 20;
console.log("x1 = 20 <= 20", x1); //x1 = 20 <= 20 true

// Modulo zur prüfung ob Zahl gerade

const num = 23
if (num % 2 === 0) {
    console.log(`${num} ist eine gerade Zahl`)
} else {
    console.log(`${num} ist eine ungerade Zahl`)
} //23 ist eine ungerade Zahl


const winkel = 1171;
const grad = winkel % 360;
console.log ("Winkel im Wertebereich von 0 - 360", grad); //teils durch 360, rest ist 91


// Übung Modulo zu einer Liste von blogbeiträgen, wieviele Beiträge bleiben übrig?
const results = 57;
const group = 12;
anzahlBeiträge = Math.floor(results/group);
let rest = results % group;
if (rest > 0){
    console.log(`${rest} Beiträge bleiben übrig! Jeder darf ${anzahlBeiträge} Beiträge schreiben!`);
} else {console.log(`Es bleiben keine beiträge übrig! Jeder darf ${anzahlBeiträge} Beiträge schreiben!`);

}
// kurzer test im parseInt abrudet: 
y3 = 10 / 0.11;
console.log(y3, "Mit parseInt umgewandelt:", parseInt(y3)); //log: 90.9090909090909 'Mit parseInt umgewandelt:' 90

// Stringlänge

const str1 = "Matthias Kahlert"
const stringLänge = str1.length;
console.log(` Der String ${str1} hat die Stringlänge von ${stringLänge}.`);

const a1 = str1[0]; //JavaScript erreicht jedes Zeichen im String mit einem index aus eckigen Klammern. es Beginnt bei 0 zu zählen. 
console.log(`Das 1. Zeichen des Strings ist ${a1}.`);

console.log("String", str1.__proto__); //zeigt die Methoden und eigenschaften zum bearbeiten von Strings

//suchen innerhalb eines Strings
const randomQuote = "Aller Anfang ist schwer!";
console.log(randomQuote.includes("Anfang")); //log: true
console.log(randomQuote.indexOf("!")); // es zeigt den ersten Index des gesuchten Zeichens. 

const teilString = randomQuote.substring(5);
console.log("Teilstring", teilString); //Teilstring  Anfang ist schwer!
const teilString2 = randomQuote.substring(5,13); //start und ende des teilstrings mit den indizies start 5 und ende 13
console.log("Teilstring 2", teilString2); //Teilstring 2  Anfang 
const teilString3 = randomQuote.substr(5,13); //Substr(start,count) gibt vom startwert an die werte bis zum count
console.log("Teilstring 3", teilString3); //Teilstring 3  Anfang ist s

// nun mit string.replace() wobei in der Klammer zwei Argumente sind, ein suchpattern und die zeichen die eingesetzt werden sollen
const replaceString = randomQuote.replace("!",", aber es lohnt sich!");
console.log(replaceString); //log: Aller Anfang ist schwer, aber es lohnt sich!
// es gibt auch ein replaceAll()

const kursTermin = "Freitags dindet kein Nähkurs statt, aber samstags gibt es gleich zwei Nähkurse!";
const replaceAll = kursTermin.replaceAll("Nähkurs", "JavaScript-Kurs");
console.log(replaceAll);

// Umwandlung in GROß oder kleinbuchstaben mit string.toLowerCase()
const spruch = "DIES IST EIN TOLLER TEXT!";
console.log(spruch.toLowerCase()); //log:dies ist ein toller text!
console.log(spruch.toLowerCase().includes("toll")); // hier werden zwei Methoden miteinander auf einen string angewendet! JavaScript entwickelt den String von links nach rechts.


//Übung Strings ersetzen - man beachte, es wird nur in dem console.log ersetzt, die variable bleibt unberührt (ist ja auch eine konstante)
//1 Wort erseten, Erscheinung durch Fata Morgana
const far = "Am Horizont sahen die eine Erscheinung";
console.log(far.replace("Erscheinung", "Fata Morgana")); //Am Horizont sahen die eine Fata Morgana
console.log(far); //Am Horizont sahen die eine Erscheinung

//2. Text in Großbuchstaben setzen
const game = "Lara Croft - Tomb Raider";
console.log(game.toUpperCase()); //LARA CROFT - TOMB RAIDER

// Zeichen an einem Index zurückgeben
console.log(game.charAt(0)); //L
console.log(game.match("C")); //log:'C', index: 5, input: 'Lara Croft - Tomb Raider', groups: undefined]

// Anwendung von string.sort() 
// Wenn strings sortiert werden gibt es arrays, hier wird das array arr angelegt und soll sortiert werden.
const arr = ["5Code", "Übach", "Anna", "Code", "Cäsar"];
document.querySelector(".simplesort").innerHTML=arr.sort(); //Auf der html seite steht nun: 5Code,Anna,Code,Cäsar,Übach - es wurde nach dem Unicode Wert sortiert.
// um diese querySelector Methode zu nutzen musste ich in der html datei <div class="simplesort"></div> eingeben.

// Anwendung von string.localeCompare()
const ts = ["101", "Oma", "Foo","Bar", "Übergriff", "Chaos", "666"].sort( 
    function(w1, w2){
    return w1.localeCompare(
        w2,'de-DE-u-kn-true');
});
console.log("ts", ts); //Browserkonsole gibt zurück: (7) ['101', '666', 'Bar', 'Chaos', 'Foo', 'Oma', 'Übergriff']
/* man sieht, dass innerhalb des string.sort eine function angewendet wird, welche die beiden strings erstellt, die verglichen werden sollen. diese funktion gibt das ergebnis als localeCompare zurück */


// StringSplit

const satz = "Jene Bemühungen, welche mit ernsthaft vorangetrieben werden, werden oft von Erfolg gekrönt sein!";
console.log(satz.split(","));
//string.trim()
const trim1 = "           JOHOHO           ", trim2 = "               und ne Buddel voll Rum!     ";
console.log(trim1.trim(), trim2.trim());  //log:JOHOHO und ne Buddel voll Rum!


// Übungen 4.9 - gib das wort Liebling zurück
const text2 = "Saras Lieblingskleid ist rot";
console.log(text2.slice(6,14)); //Liebling