/* Aufgabe: Zusammengesetzte Datentypen


Erstelle ein JavaScript-Programm, das folgende Aufgaben löst: 

a) Definiere eine Variable text mit dem Wert "Heute ist ein wunderschöner Tag, um programmieren zu lernen.". 

b) Gib die Länge des Strings in text aus, indem du die Eigenschaft length verwendest. 

c) Verwende die Methode indexOf(), um den Index des Wortes "programmieren" in text zu finden und gib diesen Index aus. 

d) Ersetze das Wort "programmieren" durch "coden" mit Hilfe der Methode replace() und gib den neuen String aus. 

e) Teile den String in text an jedem Leerzeichen, sodass du ein Array von Wörtern erhältst. Verwende dafür die Methode split() und gib das resultierende Array aus. 

f) Verwende die Methode toUpperCase(), um den gesamten String in text in Großbuchstaben umzuwandeln und gib das Ergebnis aus. */

//a)
let text = "Heute ist ein wunderschöner Tag, um programmieren zu lernen.";

//b)
const stringLänge = text.length;
console.log(` Der String "${text}" hat die Stringlänge von ${stringLänge}.`);

//c)
// - indexOf() - gibt den ersten gefundenen index des Zeichens des strings zurück. 

console.log(text.indexOf("programmieren")); // es zeigt den ersten Index des gesuchten Zeichens. 

//d)

// nun mit string.replace() wobei in der Klammer zwei Argumente sind, ein suchpattern und die zeichen die eingesetzt werden sollen
const replaceString = text.replace("programmieren","coden");
console.log(replaceString);

//e)
console.log(replaceString.split(" "));

// f)

console.log(replaceString.toUpperCase());