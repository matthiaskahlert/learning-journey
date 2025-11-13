/* Erstelle ein JavaScript-Programm, das folgende Aufgaben erfüllt: 

a) Definiere ein Array von Objekten, wobei jedes Objekt einen Mitarbeiter darstellt. 
Jedes Mitarbeiterobjekt soll die Eigenschaften name, position, startDatum (als String im Format YYYY-MM-DD) und gehalt enthalten. 
Füge mindestens drei Mitarbeiter in das Array ein. 

b) Schreibe eine Funktion, die das Array entgegennimmt und das durchschnittliche Gehalt der Mitarbeiter berechnet. 
Gib das Ergebnis auf der Konsole aus. 

c) Nutze die Array.prototype.sort() Methode, um die Mitarbeiter basierend auf ihrem Startdatum, 
vom ältesten zum neuesten, zu sortieren. 
Gib das sortierte Array auf der Konsole aus. 

d) Konvertiere das Mitarbeiter-Array in einen JSON-String und speichere diesen in einer Variablen. 
Verwende JSON.stringify() für die Konvertierung. 

e) Parse den JSON-String zurück in ein JavaScript-Objekt. 
Verwende JSON.parse() und speichere das Ergebnis in einer neuen Variablen. 
Überprüfe, ob das ursprüngliche Array und das geparste Objekt identisch sind, indem du das Ergebnis auf der Konsole ausgibst.   */

const mitarbeiter = [
  { name: "Max Mustermann", position: "Software Entwickler", startDatum: "2018-04-15", gehalt: 72000 },
  { name: "Laura Hoffmann", position: "UX Designer", startDatum: "2020-01-10", gehalt: 65000 },
  { name: "Tobias Klein", position: "Product Owner", startDatum: "2015-09-01", gehalt: 82000 }
];

//b)
function durchschnittsGehalt(mitarbeiterArray) {
  let summe = 0;
  for (const m of mitarbeiterArray) {
    summe += m.gehalt;
  }
  return summe / mitarbeiterArray.length;
}

console.log("Durchschnittsgehalt:", durchschnittsGehalt(mitarbeiter));


//c)
const sortiertNachStart = [...mitarbeiter].sort((a, b) => new Date(a.startDatum) - new Date(b.startDatum));
console.log("Startdatum, vom ältesten zum neuesten sortiert:", sortiertNachStart);

//d)
const jsonString = JSON.stringify(mitarbeiter);
console.log(jsonString);

//e)
const geparst = JSON.parse(jsonString);
console.log(geparst);
console.log("Sind sie identisch?", JSON.stringify(mitarbeiter) === JSON.stringify(geparst));

