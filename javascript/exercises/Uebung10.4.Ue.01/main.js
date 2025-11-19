/* Aufgabe: DOM
Erstelle eine JavaScript-Funktion filterAndModify, die ein Array von Objekten als Parameter annimmt. 
Jedes Objekt im Array hat die Eigenschaften name (ein String), age (eine Zahl) und email (ein String). 
Die Funktion soll folgendes tun: 

a) Filtere alle Objekte heraus, deren age größer als 18 ist.  

b) Modifiziere die gefilterten Objekte, indem du eine neue Eigenschaft adult hinzufügst, 
die true ist, wenn das Alter größer als 18 ist, ansonsten false.  

c) Verwende querySelector um ein div-Element mit der ID results im DOM zu finden 
und füge für jedes gefilterte und modifizierte Objekt einen neuen Paragraphen (<p>) hinzu, 
der den Namen und das Alter aus dem Objekt in der Form "Name: [name], Alter: [age]" darstellt. 

d) Stelle sicher, dass deine Funktion keine Fehler wirft, wenn das Array leer ist oder null/undefined übergeben wird.  

e) Verwende Arrow-Funktionen, wo immer es möglich ist.   */


const filterAndModify = [
    { name: "Max Mustermann", age: 17, email: "Max@mail.de" },
    { name: "Laura Hoffmann", age: 19, email: "Laura@mail.de" },
    { name: "Tobias Klein", age: 12, email: "Tobias@mail.de" },
    { name: "Erika Elaniak", age: 33, email: "Erika@mail.de" }
];

const results = document.getElementById("results"); // elem ist nun eine Referenz auf das DOM element <div id="results">
if (results && Array.isArray(filterAndModify) && filterAndModify.length > 0) {
    results.style.cssText += `box-shadow: 5px 10px 5px silver; text-align: center;`;

    filterAndModify
        .filter(obj => obj.age > 18)           // nur über 18
        .forEach(obj => {
            obj.adult = true;                  // neue Eigenschaft hinzufügen
            const p = document.createElement("p"); // "p" ist einfach der Tag-Name. Browser macht daraus: <p></p>
            p.innerText = `Name: ${obj.name}, Alter: ${obj.age}`;
            results.appendChild(p); //ohne appendChild würde das <p> nie auf der Seite sichtbar werden, weil es nur im Speicher existiert.
        });
      }








