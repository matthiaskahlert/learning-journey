/* Entwickle ein kleines Programm in JavaScript, das folgende Funktionalitäten umfasst: 

a) Erstelle eine Klasse Buch, die Eigenschaften wie titel, autor, veröffentlichungsjahr und genre besitzt. 
Der Konstruktor der Klasse soll alle diese Eigenschaften initialisieren. 

b) Füge der Klasse Buch eine Methode beschreibung hinzu, die eine Zeichenkette zurückgibt, welche den Titel, den Autor, 
das Veröffentlichungsjahr und das Genre des Buches in einem schönen Satz zusammenfasst. 

c) Erstelle ein Array bibliothek, das mehrere Instanzen der Klasse Buch enthält. 
Nutze verschiedene Genres und Veröffentlichungsjahre. 

d) Schreibe eine Funktion sucheNachGenre, die als Parameter ein Genre annimmt und alle Bücher dieses Genres aus dem Array bibliothek in der Konsole ausgibt. 
Verwende dazu eine Schleife. 

e) Implementiere eine Funktion neuestesBuch, die das Buch mit dem neuesten Veröffentlichungsjahr aus dem Array bibliothek findet 
und dessen Beschreibung mithilfe der Methode beschreibung in der Konsole ausgibt.   */

class Buch {                                            // definiert die Klasse, Klassenname per Konvention Uppercase
    constructor(titel, autor, jahr, genre) {           // definiert die Konstruktorparameter (Die Methode beschreibung ist kein teil dessen)
        this.titel = titel;                           // legt fest, dass jedes Objekt eine eigenschaft titel... usw bekommt bekommt
        this.autor = autor;                          // das this bezieht sich auf das noch zu erzeugende Objekt
        this.jahr = jahr;
        this.genre = genre;
    }
        beschreibung(){                          // fügt jedem Objekt eine eigene Methode zu - alles, was in einer Klasse als Name + Klammern {} steht, ist eine Methode, auch ohne function davor.
            return `Der Titel des Buches ist: "${this.titel}", 
        geschrieben wurde es vom Autor: "${this.autor}", 
        erschienen ist es im Veröffentlichungsjahr: "${this.jahr}",
        es gehört dem Genre: "${this.genre}" an.`;
        }

}

const bibliothek = [
    new Buch("Der Herr der Ringe", "JRR Tolkien", 1954, "Fantasy"),
    new Buch("1984", "George Orwell", 1949, "Dystopie"),
    new Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 1997, "Fantasy"),
    new Buch("Der Alchimist", "Paulo Coelho", 1988, "Philosophie"),
];


console.log(bibliothek[0].beschreibung()); // einzelnne buch beschreibung

for (const buch of bibliothek) {
    console.log(buch.beschreibung());
}


// d) Schreibe eine Funktion sucheNachGenre, die als Parameter ein Genre annimmt 
// und alle Bücher dieses Genres aus dem Array bibliothek in der Konsole ausgibt. 
// Verwende dazu eine Schleife. 
const sucheNachGenre = function(genre) {
    let gefunden = false
    for (const buch of bibliothek) {
        if (buch.genre === genre) {
            console.log(`${buch.titel} hat das Genre "${genre}"`);
            gefunden = true;
            
        }
    }
if (!gefunden) {console.log(`Keine Bücher mit dem Genre "${genre}" gefunden`);}
}
sucheNachGenre("Fantasy");


//e) Implementiere eine Funktion neuestesBuch, die das Buch mit dem neuesten Veröffentlichungsjahr aus dem Array bibliothek findet 
// und dessen Beschreibung mithilfe der Methode beschreibung in der Konsole ausgibt.   */

const sortiertAbsteigend = [...bibliothek].sort((a, b) => b.jahr - a.jahr); ///... erzeugt eine kopie von bibliothek und sortiert absteigend
console.log(`Das neuste der Bibliothek Buch ist "${sortiertAbsteigend[0].titel}" mit dem Veröffentlichungsjahr von ${sortiertAbsteigend[0].jahr}!
    Die Beschreibung lautet: 
    
    ${sortiertAbsteigend[0].beschreibung()}; `); //das erste element ist das jüngste buch

/* const juengstesBuch = bibliothek.reduce((juengstes, buch) => 
    buch.jahr > juengstes.jahr ? buch : juengstes
);

console.log(`Das jüngste Buch ist "${juengstesBuch.titel}" (${juengstesBuch.jahr}).`); */
