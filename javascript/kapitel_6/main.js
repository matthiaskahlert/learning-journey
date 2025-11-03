
function rechnen (a,b){
    const ergebnis = a - b

    console.log(`Es wird berechnet, wieviel ${a} -${b} ist.
    Das Ergebnis ist ${ergebnis}.`);
            return ergebnis;
}

rechnen(500,234);

function multi42 (x) {
    return x * 42;
}

console.log(multi42(1337)); // log:56154


/* const berechnung = magic()
berechnung(1337) */

function teilen (a,b){
    const wert = a / b;
    return wert;
    console.log("wert", wert);
}
const divi = teilen(110,700);  
console.log("divi", divi, typeof divi); // ohne den rückgabewert wäre divi undefined.


function publishPost(titel) {
    return `Besuchen sie unsere Ausstellung: ${titel}.`;
    }
console.log(publishPost("Ausstellungstitel")); //Besuchen sie unsere Ausstellung Ausstellungstitel.
console.log(publishPost()); // "Besuchen sie unsere Ausstellung undefined."  Wenn kein Argument übergeben wird. Dies wird so umgangen:


function publishPost2(titel2) {
    if (!titel2){ // Wenn kein Argument gegeben, dann ...
        titel2="Bilder des Tages"; // ... wird ein Default wert bzw fallback gesetzt.
    }
    return `Besuchen sie unsere Ausstellung: ${titel2}.`;
    }

console.log(publishPost2());

// Eine schlankere Lösung bietet das setzen eines Platzhalters
function publishPost3(titel3 = "Caspar David Friedrichs schönste Werke"){
    return  `Besuchen sie unsere Ausstellung: ${titel3}.`;
}

console.log(publishPost3());

console.log(publishPost3("Franz Marc´s blaue Pferde"));


const global = 100

function local(){
    const global = 10;
    console.log("Im Funktionsscope:", global);
}


local();


console.log("Im globalen scope:", global);

function aussen(){
    const aussenStr = "Hallo von aussen";
    function innen(){
        const innenStr = " Hallo von innen!";
        console.log(aussenStr);
        console.log(innenStr);
    }
    innen()
    // console.log("Aufruf von aussen", innenStr); // log: innenStr not defined - man kann von aussen nicht auf die Variable der inneren Funktion zugreifen
}

aussen();

// Wenn man die innere Funktion von aussen zugreifbar machen, muss man sie zurückgeben:

function outer() {
  function inner() {
    console.log("Ich bin jetzt von außen aufrufbar!");
  }

  return inner; // gibt die Funktion selbst zurück als Wert
}

const innerFunction = outer(); // die Variable innerFunction bekommt den Rückgabewert von outer() zugewiesen,  outer() wird ausgeführt, inner() wird zurückgegeben
innerFunction(); //  funktioniert jetzt von außen



// Übung 6.3: Globaler Scope, Block-Scope und Funktions-Scope
// Rechne die Werte der Variablen der beiden Funktionen überall dort aus, wo
// console.log(?) aufgerufen wird.
{
const global = 400;                                 // 0. globaler scope, für alle funktionen sichtbar

function ausgabe() {
    let loc = 2.5;                                  // 2. loc ist hier mit dem Wert 2.5
    let func = 100 + local(global+loc);             // 3. func ist hier 100+funktionsaufruf, der interpreter springt also in 3. die andere funktion :local(402.5)
                                                    // 8. rückgabewert von local(global+loc) ist intern also 1402.5, daher ist func nun gleich 1502.5
    func = func +loc;                               // 9. func ist hier ergebnis von func aus zeile zuvor + 2.5 also 1505
    console.log("Funktion ausgabe", loc, func);     // 10. Funktion ausgabe 2.5 1505
}

function local(loc){                                // folgend von 3. local von loc, wobei loc = 402.5 denn: local(global+loc) aus funktion ausgabe
    let global = 1000;                              // 4. global ist hier im funktionsscope mit dem Wert 1000
    intern = loc + global;                          // 5. intern ist hier 402.5 + 1000 (überschattung von global und loc aus local(loc) -> local(402.5))
    console.log("Funktion local", global, intern);  // 6. log: Funktion local 1000 1402.5
    return intern;                                  // 7. intern wird als wert zurückgegeben
}

ausgabe();                                          //1. Funktuion ausgabe() wird ausgeführt.
console.log("intern", intern); //intern 1402.5      // 11. da intern nicht mit var const oder let deklariert wurde ist sie zur globalen variable geworden.

}
 // Was passiert mit der Variablen intern, die weder mit var, noch mit const oder let eklariert ist? 
 // Ist intern am Ende des Skripts bekannt?

 // intern ist eine globale Varible geworden und daher auch von ausserhalb zugänglich, da intern nicht mit let oder const deklariert wurde.

 // Function Expressions

function brutto(betrag, satz){
    const mwst = betrag * satz / 100;
    return betrag + mwst;
}
const summe = brutto (500, 19);
console.log("Summe:", summe);

// arrow function
const euro = x => x + " €";
console.log(euro(15));

// arrow mit objekt als rückgabewert

// Objekte sitzen in geschweiften Klammern arrows aber auch (man schreibt sie ja nur nicht mit)

const kurs = { 
    title:      "Stricken für Anfänger",
    coach:      "Julia",
    places:     12,
    started:    true,
    location:   "Hamburg",
}
// Daher muss man bei arrows mit Objekten zusätzliche runde Klammern setzen:

const returnObject = () =>({
    city: " Hamburg",
    einwohner: 2000000
});

console.log(returnObject);

// Exkurs zu Arrays
const counter = [1,2,3,4,5];
counter.forEach(function(n){ // forEach ist eine Array-Methode, die für jedes Element des Arrays einmal die Funktion aufruft.
    console.log(n);
});
// Kurze Schreibweise
counter.forEach(n => console.log(n));

counter.forEach(n => console.log(n * 2)); // gibt 2,4,6,8,10 aus - Man kann jedes Element des Arrays weiter verarbeiten.

// 6.7 Übungen funktionen
// 1. Celsius in Fahrenheit umrechnen
// Die funktion bekommt als parameter die temparatur in celsius
/* Temperatur
Umrechnung Celsius in Fahrenheit: °F = °C x 1,8 + 32.
Umrechnung Fahrenheit in Celsius: °C = (°F - 32) / 1,8.

function temparatur(celsius) {
    return (celsius * 1.8) + 32;
 }

 */

const temparatur = celsius => (celsius * 1.8) + 32;

x = 25

// console.log(temparatur(x))

console.log(`${x}°C sind umgerechnet ${temparatur(x)}°F`);

// Arrow-Funktion und Arrays
/* Schreibe eine Funktion, der ein Array mit Zahlen übergeben wird und die ein Objekt mit der kleinsten und größten Zahl zurückgibt. 
Schreibe die Funktion als Arrow-Funktion in einer Zeile */

const zähler = [13,2,33,4,55];
function uebungArray(zähler) {

    const max = Math.max(...zähler);
    const min = Math.min(...zähler);
    return {min:min, max:max}  // man erkennt das Objekt an den geschweiften Klammern, min und max sind die Eigenschaften des Objekts, siehe auch Kapitel 3, zusammengesetzte Datentypen

}
const objekt = uebungArray(zähler);
console.log(objekt);
{
const uebungArray = (zähler) => ({max: Math.max(...zähler), min: Math.min(...zähler)})

const ergebnis = uebungArray(zähler);
console.log(ergebnis);
}



// Ausgabe von Werten beim Laden der Seite
// Aus Breite und Höhe eines Rechtecks die Fläche berechnen und beim Laden der Seite direkt in der Konsole des Browsers ausgeben.
// Mit den Werten Breite 30 und Höhe 20

function fläche(breite,höhe){
    fläche = breite * höhe
    console.log(`Die Fläche eines Rechtecks mit einer Breite von ${breite} und einer Höhe von ${höhe} ist ${fläche}`)
}
fläche(30,20);