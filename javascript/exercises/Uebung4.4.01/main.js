
/* Erstelle eine JavaScript-Datei, die folgende Aufgaben erfüllt:  

a) Definiere eine Variable kursDetails als Objekt, das die Eigenschaften name, teilnehmerzahl und ort enthält. 
Initialisiere diese Eigenschaften mit den Werten "JavaScript Einführungskurs", 15 und "Berlin". 

b) Erhöhe die teilnehmerzahl um 5, ohne den Wert direkt zu überschreiben, und speichere das Ergebnis in der gleichen Eigenschaft. 

c) Berechne das Verhältnis der aktuellen teilnehmerzahl zur maximalen Teilnehmerzahl von 30 und speichere dieses Verhältnis in einer neuen Variable auslastung als Fließkommazahl. 

d) Verwende das Math-Objekt, um die auslastung auf zwei Nachkommastellen zu runden und gib das Ergebnis in der Konsole aus.   */
//a)
const kursDetails = {
        kursName:           "JavaScript Einführungskurs",
        teilnehmerzahl:     15,
        ort:                "Berlin",
}

//b) Meine Idee ist es mit einer for schleife hochzuzählen, bis der wert 15 erreicht ist, dazu muss ich auf kursDetails.teilnehmerzahl zugreifen
for (kursDetails.teilnehmerzahl=15; kursDetails.teilnehmerzahl<20; kursDetails.teilnehmerzahl++) {
    console.log(kursDetails.teilnehmerzahl);
}
console.log(kursDetails);

// leichtere Lösung: kursDetails.teilnehmerzahl += 5; 
//c)
kursDetails.auslastung = kursDetails.teilnehmerzahl/30;
console.log(kursDetails);

//d)
kursDetails.auslastung=Math.round(kursDetails.auslastung * 100) / 100;
console.log(`Die Auslastung des Kurses beträgt gerundet ${kursDetails.auslastung}`);