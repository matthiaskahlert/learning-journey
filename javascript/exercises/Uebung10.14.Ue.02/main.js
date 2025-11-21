/* 

Entwickle ein kleines JavaScript-Projekt, das folgende Anforderungen erfüllt: 

a) Erstelle eine Klasse Buch, die Eigenschaften wie titel, autor, isbn und veröffentlicht 
(Jahr der Veröffentlichung) besitzt. Der Konstruktor der Klasse soll alle diese Eigenschaften initialisieren. 

b) Erweitere die Klasse Buch um eine Methode info(), 
die eine Zeichenkette zurückgibt, die den Titel, den Autor und das Jahr der Veröffentlichung enthält. 

c) Erstelle ein Array bibliothek, das mehrere Buch-Objekte enthält. 

d) Nutze die DOM-Methoden, um eine Tabelle im HTML-Dokument zu erstellen, 
die die Informationen jedes Buches aus dem Array bibliothek anzeigt. 
Verwende dabei document.createElement, innerHTML oder innerText und füge die 
Tabelle in ein bestehendes Element mit der ID buchListe ein. 

e) Füge CSS-Stile hinzu, um die Tabelle ansprechend zu gestalten. Verwende document.querySelector 
oder document.querySelectorAll, um Zugriff auf die Tabelle oder deren Zellen zu bekommen 
und ändere die Hintergrundfarbe der Zeilen abwechselnd, um die Lesbarkeit zu verbessern.

 */

const container = document.querySelector("#buch-container");


class Buch {
    constructor(titel, autor, isbn, veröffentlicht) {
        this.titel = titel;
        this.autor = autor;
        this.isbn = isbn;
        this.veröffentlicht = veröffentlicht;
    }
    info() {
        console.log(`Der Titel des Buchs ist "${this.titel}", 
            geschrieben wurde es von :"${this.autor}",
            und veröffentlicht im Jahr "${this.veröffentlicht}".`);
    };

}
const bibliothek = [
    new Buch("Dune", "Frank Herbert", "978-0441013593", 1965),
    new Buch("Dune Messiah", "Frank Herbert", "978-0441172696", 1969),
    new Buch("Children of Dune", "Frank Herbert", "978-0441104024", 1976),
    new Buch("God Emperor of Dune", "Frank Herbert", "978-0441172696", 1981),
    new Buch("Heretics of Dune", "Frank Herbert", "978-0441104031", 1984),
    new Buch("Chapterhouse: Dune", "Frank Herbert", "978-0441104055", 1985)
];

// Beispiel: alle Bücher in der Konsole ausgeben
bibliothek.forEach(buch => buch.info());


bibliothek.forEach(buch => {
    const li = document.createElement("li");
    li.innerText = `${buch.titel} - ${buch.autor} (${buch.veröffentlicht})`;
    container.appendChild(li);
});


/* <table>
  <tr>
    <th>Titel</th>
    <th>Autor</th>
    <th>Jahr</th>
  </tr>
  <tr>
    <td>Dune</td>
    <td>Frank Herbert</td>
    <td>1965</td>
  </tr>
  <tr>
    <td>Dune Messiah</td>
    <td>Frank Herbert</td>
    <td>1969</td>
  </tr>
</table> */
// d) Nutze die DOM-Methoden, um eine Tabelle im HTML-Dokument zu erstellen, die die Informationen jedes Buches aus dem Array bibliothek anzeigt. Verwende dabei document.createElement, innerHTML oder innerText und füge die Tabelle in ein bestehendes Element mit der ID buchListe ein.

const table = document.createElement("table");
const headerRow = document.createElement("tr");
headerRow.innerHTML = ` 
    <th>Titel</th>
    <th>Autor</th>
    <th>Jahr</th>
`;
table.appendChild(headerRow);   
bibliothek.forEach(buch => {
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${buch.titel}</td>  
        <td>${buch.autor}</td>
        <td>${buch.veröffentlicht}</td>
    `;
    table.appendChild(row);
});
// e) Füge CSS-Stile hinzu, um die Tabelle ansprechend zu gestalten. Verwende document.querySelector oder document.querySelectorAll, um Zugriff auf die Tabelle oder deren Zellen zu bekommen und ändere die Hintergrundfarbe der Zeilen abwechselnd, um die Lesbarkeit zu verbessern.
table.style.borderCollapse = "collapse";
table.style.width = "80%";

table.querySelectorAll("th, td").forEach(cell => {
    cell.style.border = "1px solid #000";
    cell.style.padding = "0.1rem";
    cell.style.textAlign = "center";
    });
table.querySelectorAll("th").forEach(th => {
    th.style.backgroundColor = "#b1b1b1ff";
    th.style.fontWeight = "bold";
});
table.querySelectorAll("td").forEach(td => {
      td.style.backgroundColor = "#b8f7ffff";
})
container.appendChild(table);
