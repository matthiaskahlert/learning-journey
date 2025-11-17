/* Aufgabe: DOM
- [x] Erstelle eine JavaScript-Funktion, die eine Liste von Objekten durchgeht, die jeweils einen Mitarbeiter repräsentieren. 
- [x] Jedes Objekt enthält den Namen, die Abteilung und das Gehalt des Mitarbeiters. 
- [x] Die Funktion sollte das Gesamtgehalt aller Mitarbeiter in der IT-Abteilung berechnen und zurückgeben. 
Verwende dabei Schleifen, Bedingungen und die entsprechenden DOM-Methoden, um auf die Daten zuzugreifen. 
Gehe davon aus, dass die Daten in einem Array von Objekten vorliegen 
- [x] und die HTML-Seite ein leeres div-Element mit der id "ergebnis" enthält, 
in das das Gesamtgehalt eingefügt werden soll.   */

const mitarbeiter = [
    { name: "Max Mustermann", position: "IT", gehalt: 72000 },
    { name: "Laura Hoffmann", position: "IT", gehalt: 65000 },
    { name: "Tobias Klein", position: "IT", gehalt: 82000 },
    { name: "Erika Elaniak", position: "BeachBeauties", gehalt: 71999 }
];
function gesamtGehalt(mitarbeiterArray) {
  let summe = 0;
  for (const m of mitarbeiterArray) {
    if (m.position === "IT") summe += m.gehalt;
  }
  return summe;
}

console.log("Gesamtgehalt:", gesamtGehalt(mitarbeiter)); //log: Gesamtgehalt: 219000
const gehaltsBerechnung = gesamtGehalt(mitarbeiter)
const ergebnis = document.getElementById("ergebnis"); // elem ist nun eine Referenz auf das DOM element <div id="ergebnis">
ergebnis.style.cssText += // Die Kombination von +und = konkateniert die vorhandenen Stile mit dem neuen String, sprich, es führt die Strings zusammen.
        `box-shadow: 5px 10px 5px silver;
        text-align: center`; 
ergebnis.innerText = `${gehaltsBerechnung} €`;

