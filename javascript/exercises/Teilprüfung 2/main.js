/* Entwickle ein kleines JavaScript-Programm, das folgende Anforderungen erfüllt:


a) Erstelle eine Klasse Buch, 
die Konstruktorparameter für den Titel (String), den Autor (String), das Veröffentlichungsjahr (Number) 
und ob das Buch einen Preis gewonnen hat (Boolean) akzeptiert. 
Die Klasse soll auch eine Methode beschreibung haben, die eine Zeichenkette zurückgibt, 
die den Titel, den Autor und das Veröffentlichungsjahr enthält.


b) Erstelle ein Objekt dieser Klasse für "Der Herr der Ringe", geschrieben von "JRR Tolkien", 
veröffentlicht im Jahr 1954, das keinen Preis gewonnen hat.


c) Verwende eine for-in-Schleife, um über die Eigenschaften des Buchobjekts zu iterieren und jede Eigenschaft und ihren Wert in der Konsole auszugeben.


d) Füge dem Buchobjekt eine neue Eigenschaft genre hinzu, die den Wert "Fantasy" hat, ohne die Klasse Buch zu modifizieren. 
Gib das aktualisierte Objekt in der Konsole aus.


e) Schreibe eine Funktion aktuellesDatum, die das aktuelle Datum und die Uhrzeit als Zeichenkette im Format "TT.MM.JJJJ, HH:MM:SS" zurückgibt. 
Verwende diese Funktion, um das aktuelle Datum und die Uhrzeit in der Konsole auszugeben.


f) Demonstriere die Verwendung von mindestens zwei unterschiedlichen String-Methoden anhand des Titels des Buches.


g) Implementiere eine einfache Fehlerbehandlung für den Fall, dass der Titel des Buches nicht als String übergeben wird. 
Gib eine entsprechende Fehlermeldung in der Konsole aus. */



//a)
class Buch {                                            // definiert die Klasse, Klassenname per Konvention Uppercase
    constructor(titel, autor, jahr, preis) {           // definiert die Konstruktorparameter (Die Methode beschreibung ist kein teil dessen)
        this.titel = titel;                           // legt fest, dass jedes Objekt eine eigenschaft titel... usw bekommt bekommt
        this.autor = autor;                          // das this bezieht sich auf das noch zu erzeugende Objekt
        this.jahr = jahr;
        this.preis = preis;
    }
        beschreibung(){                          // fügt jedem Objekt eine eigene Methode zu - alles, was in einer Klasse als Name + Klammern {} steht, ist eine Methode, auch ohne function davor.
            return `Titel: "${this.titel}", 
        Autor: "${this.autor}", 
        Veröffentlichungsjahr: "${this.jahr}".`;
        }

}
//b) 

const buch1 = new Buch("Der Herr der Ringe", "JRR Tolkien", 1954, false);
// console.log(buch1.beschreibung()); // Testausgabe der Methode
// console.log(buch1); Testausgabe des Objekts

// c) 

for (const key in buch1){
        console.log(`${key}: ${buch1[key]}`);
        }
//d)
buch1.genre = "Fantasy";
console.log(buch1);


//e) 
function aktuellesDatum(){
    const datum = new Date().toLocaleString();
    return datum;       // Die Funktion braucht einen Rückgabewert, sonst undefined
}
console.log(aktuellesDatum()); //log: 7.11.2025, 12:45:18

//f) 
console.log(`Ich wende nun unterschiedliche Stringmethoden auf den folgenden String an:"${buch1.titel}"`);
// Ich wende string.length an um die Stringlänge zu bestimmen.
const stringLänge = buch1.titel.length;
console.log(` Der String "${buch1.titel}" hat die Stringlänge von ${stringLänge} Zeichen.`);


// nun mit string.replace() wobei in der Klammer zwei Argumente sind, ein suchpattern und die zeichen die eingesetzt werden sollen
const replaceString = buch1.titel.replace("Ringe","Fliegen");
console.log(`Der Titel "${buch1.titel}"wurde genutzt um die Stringmethode replaceString anzuwenden.
Diese funktioniert wie folgt:
- replace(searchValue, replaceValue) ersetzt das erste Vorkommen von searchValue durch replaceValue.
 Wenn man nun buch1.titel.replace("Ringe","Fliegen")auf "${buch1.titel}" anwendet,  
ergibt dies: "${buch1.titel.replace("Ringe","Fliegen")}". `);


// g) 

try {
  buch1.titel = 123456;
  if (typeof buch1.titel !== "string"){
    throw new Error(`Ungültiger wert: Es sind nur Strings erlaubt!`)
  }
} catch (error) {
  console.error(error.message);
  buch1.titel = "Unbekannt";        // Fallback wird gesetzt. Theoretisch könnte man auch den neuen Titel über eine Variable einspielen und dann mit toString umwandeln, aber in diesem Fall wollte ich mal ein Fallback ausprobieren.
  console.log(` Fallbacktitel wurde gesetzt: "${buch1.titel}"`);
}

if (typeof buch1.titel !== "string") {
  console.error("Test fehlgeschlagen: Der Datentyp des Titels ist kein String!.");
} else {
  console.log("Test bestanden: Der Datentyp des Titels ist ein String")
}
