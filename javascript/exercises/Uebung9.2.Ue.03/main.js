/* Entwickle ein kleines JavaScript-Programm, das folgende Anforderungen erfüllt: 

a) Definiere ein JSON-Objekt, das Informationen über drei verschiedene Bücher enthält. 
Jedes Buch soll folgende Eigenschaften haben: Titel, Autor, Veröffentlichungsjahr und eine Liste von Stichworten. 

b) Wandle das JSON-Objekt in einen String um und gib diesen String in der Konsole aus. 

c) Parse den String zurück in ein JavaScript-Objekt. 

d) Verwende eine for-Schleife, um über die Bücher zu iterieren. 
Für jedes Buch sollst du das Veröffentlichungsjahr überprüfen. 
Wenn das Buch vor dem Jahr 2000 veröffentlicht wurde, gib den Titel und das Veröffentlichungsjahr in der Konsole aus. 

e) Erstelle eine Funktion, die für jedes Buch überprüft, ob ein bestimmtes Stichwort (z.B. "Abenteuer") in der Liste der Stichworte enthalten ist. 
Wenn ja, gib den Titel des Buches aus.   */


//a)
const jsonObjekt = 
[
  {
    "titel": "Mansfield Park",
    "autor": "Jane Austen",
    "veröffentlichungsjahr": 1814,
    "stichworte": ["Romantik", "Gesellschaft", "England"]
  },
  {
    "titel": "Stolz und Vorurteil",
    "autor": "Jane Austen",
    "veröffentlichungsjahr": 1813,
    "stichworte": ["Romantik", "Liebe", "Gesellschaft"]
  },
  {
    "titel": "Emma",
    "autor": "Jane Austen",
    "veröffentlichungsjahr": 1816,
    "stichworte": ["Romantik", "Gesellschaft", "Intrigen"]
  } 
]

//b)
const jsonString = JSON.stringify(jsonObjekt);
console.log(jsonString);

//c)
const jsonParsed = JSON.parse(jsonString);
console.log(jsonParsed);

//d) Verwende eine for-Schleife, um über die Bücher zu iterieren.
for (const buch of jsonParsed){
  if (buch.veröffentlichungsjahr<2000) {
    console.log(`Alte Bücher: ${buch.titel}, ${buch.veröffentlichungsjahr}`);
  }
}


//e)funktion mit Stichwortsuche, wenn true dann, gib den Titel des Buches aus
const stichworte = function(wort){
  for (const buch of jsonParsed){
    if (buch.stichworte.includes(wort)) {
      console.log(`Buchtitel mit gewünschtem Stichwort "${wort}": ${buch.titel}`);
    }
  }
}
stichworte("England");
stichworte("Romantik");
stichworte("Gesellschaft");