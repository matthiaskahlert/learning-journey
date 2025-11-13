/* Entwickle ein kleines JavaScript-Programm, das folgende Anforderungen erfüllt: 

a) Definiere eine Klasse Buch, die Eigenschaften wie titel, autor, veroeffentlichungsjahr und genre hat. 
Der Konstruktor der Klasse soll alle diese Eigenschaften initialisieren. 

b) Erstelle eine Methode innerhalb der Klasse Buch, die das Buchobjekt in ein JSON-Objekt umwandelt
 und dieses als String zurückgibt. Verwende dafür JSON.stringify(). 

c) Schreibe eine Funktion buecherLaden, die einen JSON-String akzeptiert, der ein Array von Buch-Objekten repräsentiert. 
Die Funktion soll das JSON-Array parsen und jedes Buchobjekt in eine Instanz der Klasse Buch umwandeln. 
Verwende dafür JSON.parse() und gib das resultierende Array von Buch-Instanzen zurück. 

d) Implementiere eine Funktion sucheNachJahr, die ein Array von Buch-Instanzen und ein Jahr als Parameter nimmt. 
Die Funktion soll alle Bücher zurückgeben, die nach dem gegebenen Jahr veröffentlicht wurden. 
Verwende eine Schleife, um durch das Array zu iterieren und eine if-Bedingung, um die Bücher zu filtern. 

e) Erstelle ein Array von Buch-JSON-Strings (mindestens zwei Bücher) und wandle dieses Array in einen JSON-String um. 
Lade dann die Bücher mit der Funktion buecherLaden 
und verwende sucheNachJahr, um alle Bücher zu finden, die nach 2000 veröffentlicht wurden. 
Gib das Ergebnis auf der Konsole aus.  */


//a) 

class Buch {
    constructor(titel, autor, veröffentlichungsjahr, genre) {
        this.titel = titel;
        this.autor = autor;
        this.veröffentlichungsjahr = veröffentlichungsjahr;
        this.genre = genre;
    }
// b)
    jsonObj(){
        return JSON.stringify(this); // this bezieht sich auf das ganze Objekt!
    }
}
// testausgaben in browserkonsole
// const meinBuch = new Buch("1984", "George Orwell", 1949, "Dystopie");
// console.log(meinBuch.jsonObj());


//c)
// folgende Konstante bildet ein array aus objekten die Buch instanzen enthalten
const bibliothek = [ 
    new Buch("Der Herr der Ringe", "JRR Tolkien", 1954, "Fantasy"),
    new Buch("1984", "George Orwell", 1949, "Dystopie"),
    new Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 1997, "Fantasy"),
    new Buch("Der Alchimist", "Paulo Coelho", 1988, "Philosophie"),
];

console.log(bibliothek[2].jsonObj()); // testausgabe zeigt, dass die methode mit angelegt ist

console.log(JSON.stringify(bibliothek));


const buecherLaden = function(jsonString){
    // const encodedString = encodeURIComponent(jsonString); // wird nur gebraucht wenn ich das ergebnis via url verschicken will.
    const result = JSON.parse(jsonString);
    // return result.map(b => new Buch(b.titel, b.autor, b.veröffentlichungsjahr, b.genre));
    return result.map(function(obj){
         return new Buch(obj.titel, obj.autor, obj.veröffentlichungsjahr, obj.genre)
     })
}


const parsedString = buecherLaden(JSON.stringify(bibliothek))

console.log(parsedString); // testausgabe ob die methoden mitgeliefert wurden

console.log(parsedString[2].jsonObj()); 

//d)
const sucheNachJahr = function (arr, jahr){
    let gefunden = false
    for (const buch of arr) {
        if (buch.veröffentlichungsjahr > jahr) {
            console.log(`"${buch.titel}" wurde nach dem Jahr ${jahr} veröffentlicht und zwar im Jahr "${buch.veröffentlichungsjahr}"`);
            gefunden = true;
            
        }
    }
if (!gefunden) {console.log(`Keine Bücher der Bibliothek sind nach dem Jahr ${jahr} veröffentlicht worden.`);}
}
sucheNachJahr(bibliothek, 1991);

//e)
const buchArray = [
    {titel: "Der kleine Prinz", autor: "Antoine de Saint-Exupéry", veröffentlichungsjahr: 2001, genre: "Märchen"},
    {titel: "Twilight", autor: "Stephenie Meyer", veröffentlichungsjahr: 2005, genre: "Fantasy"}
];
const jsonString = JSON.stringify(buchArray);
const geladeneBuecher = buecherLaden(jsonString);

sucheNachJahr(geladeneBuecher, 2000);
console.log(geladeneBuecher[0].jsonObj());

