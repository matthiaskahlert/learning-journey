/* Aufgabe: Funktionen


Entwickle ein kleines JavaScript-Programm, das folgende Anforderungen erfüllt: 

a) Definiere eine Funktion berechneQuadrat, die einen Parameter entgegennimmt und das Quadrat dieses Parameters zurückgibt. 
Verwende dabei den Funktionsausdruck.  

b) Erstelle eine Variable nummer im globalen Gültigkeitsbereich und weise ihr einen Wert zu. 

c) Rufe die Funktion berechneQuadrat mit der Variable nummer als Argument auf und speichere das Ergebnis in einer neuen Variable ergebnis. 

d) Verwende eine if-else-Struktur, um zu überprüfen, ob das ergebnis größer als 100 ist. 
Wenn ja, gib eine Meldung aus, die besagt, dass das Ergebnis größer als 100 ist. 
Andernfalls gib eine Meldung aus, die besagt, dass das Ergebnis kleiner oder gleich 100 ist. 

e) Verwende eine for-Schleife, um die Zahlen von 1 bis 5 auszugeben. 

f) Innerhalb der for-Schleife, verwende den ternären Operator, um zu überprüfen, ob die aktuelle Zahl ungerade ist. 
Gib für ungerade Zahlen "Ungerade" und für gerade Zahlen "Gerade" aus. */

//a)
function berechneQuadrat(a){
    const resultat = Math.pow(a,2);
    console.log(`Die Berechnung ergibt:${resultat}`);
    return resultat;

}


berechneQuadrat(12);


// b)
let nummer = 5;
// c)
berechneQuadrat(nummer);

const ergebnis = berechneQuadrat(nummer);
console.log("Die Funktion wurde mit Variable als Parameter aufgerufen und ergab das Ergebnis:", ergebnis);

if(ergebnis > 100){
    console.log(`Das Ergebnis ${ergebnis} ist größer als 100`);
} else {
    console.log(`Das Ergebnis ${ergebnis} ist kleiner oder gleich 100`);
}
//e und f)
for (let i=1; i<=5; i++){
    
    const ausgabe = (i%2==0) ? "gerade":"ungerade";
    console.log(`Der Wert ${i} ist ${ausgabe}!`);
}


// Globale Variable
let global = 10;

console.log("Global vor Funktion:", global); // 10

function testeÜberschattung() {
    // Lokale Variable mit gleichem Namen
    let global = 5; // nur innerhalb der Funktion sichtbar
    console.log("Global in Funktion:", global); // 5
}

testeÜberschattung();

console.log("Global nach Funktion:", global); // 10, unverändert