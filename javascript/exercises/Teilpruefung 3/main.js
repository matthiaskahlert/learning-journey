/*Du arbeitest als Entwickler*in in einem Unternehmen, das eine Webanwendung für ein Buchverwaltungssystem entwickelt. 
Deine Aufgabe ist es, eine JavaScript-Funktion zu entwickeln, die eine Liste von Büchern als JSON-String erhält. 
Diese Liste soll anschließend analysiert und bearbeitet werden, um verschiedene Informationen und Statistiken zu den Büchern zu erzeugen. 
Die Funktion soll folgende Aufgaben erfüllen: 

-[x] a) Konvertiere den JSON-String in ein JavaScript-Objekt. 

-[x] b) Zähle die Anzahl der Bücher und gib diese aus. 

-[x] c) Finde das Buch mit der höchsten Seitenanzahl und gib dessen Titel und Seitenanzahl aus. 

-[x] d) Erstelle ein neues Array, das nur die Titel der Bücher enthält, die vor dem Jahr 2000 veröffentlicht wurden. 

-[x] e) Sortiere dieses Array alphabetisch und gib es aus. 

-[x] f) Konvertiere das resultierende Array zurück in einen JSON-String und gib diesen aus. 

 

Nutze folgenden JSON-String als Eingabedaten: 

[ 
    {"titel": "Mansfield Park", "veröffentlicht": 1814, "seiten": 480}, 
    {"titel": "Stolz und Vorurteil", "veröffentlicht": 1813, "seiten": 432}, 
    {"titel": "Emma", "veröffentlicht": 1816, "seiten": 392}, 
    {"titel": "Der große Gatsby", "veröffentlicht": 1925, "seiten": 180}, 
    {"titel": "1984", "veröffentlicht": 1949, "seiten": 328} 
]  
 */
//a) Konvertiere den JSON-String in ein JavaScript-Objekt
const jsonString = `[{"titel": "Mansfield Park", "veröffentlicht": 1814, "seiten": 480},{"titel": "Stolz und Vorurteil", "veröffentlicht": 1813, "seiten": 432},{"titel": "Emma", "veröffentlicht": 1816, "seiten": 392},{"titel": "Der große Gatsby", "veröffentlicht": 1925, "seiten": 180},{"titel": "1984", "veröffentlicht": 1949, "seiten": 328}]`;
const jsonParsed = JSON.parse(jsonString);


//b) Zähle die Anzahl der Bücher und gib diese aus.
console.log(`Die Anzahl der Bücher beträgt: ${jsonParsed.length}`); // gibt die anzahl der bücher aus


//c)) Finde das Buch mit der höchsten Seitenanzahl und gib dessen Titel und Seitenanzahl aus. 
const seitenSortiert = jsonParsed.sort((a, b) => b.seiten - a.seiten);
console.log(`Das Buch mit den meisten Seiten heißt "${seitenSortiert[0].titel}" und hat eine Seitenanzahl von:${seitenSortiert[0].seiten} Seiten.`); 


//d) Erstelle ein neues Array, das nur die Titel der Bücher enthält, die vor dem Jahr 2000 veröffentlicht wurden. 
const newArr = jsonParsed.filter(jsonParsed => jsonParsed.veröffentlicht<2000).map((jsonParsed => jsonParsed.titel)); // hier reduziere ich auf die Titel der Bücher, welche vor dem Jahr 2000 veröffentlicht wurden, Seitenanzahl und Veröffentlichungsjahr fallen weg per aufgabenstellung "nur die Titel der Bücher..."


//e) Sortiere dieses Array alphabetisch und gib es aus. 
const sortiert = newArr.sort();    
console.log(sortiert);


//f) Konvertiere das resultierende Array zurück in einen JSON-String und gib diesen aus. 
const resultArray = JSON.stringify(newArr);
console.log(`DerJSON String der alphabetisch sortierten Titel lautet: ${resultArray}`);