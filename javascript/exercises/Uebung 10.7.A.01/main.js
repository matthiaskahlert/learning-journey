/* Entwickle eine kleine Webanwendung, die eine Liste von Produkten anzeigt. 
Jedes Produkt soll in einem Objekt gespeichert werden, das folgende Eigenschaften hat: 
id (Nummer), name (String), preis (Nummer), und kategorie (String). 
Die Anwendung soll folgende Funktionalitäten umfassen: 

a) Erstelle ein Array von Produktobjekten mit mindestens fünf verschiedenen Produkten. 

b) Implementiere eine Funktion, die alle Produkte in das DOM einbindet. 
Verwende dazu document.createElement(), innerText und Methoden zur DOM-Navigation, 
um jedes Produkt als ein div-Element mit Unterelementen für id, name, preis, und kategorie anzuzeigen. 

c) Füge eine Suchfunktion hinzu, die es ermöglicht, Produkte nach Namen zu filtern. 
Nutze dabei ein Input-Feld und einen Button. Die Suchergebnisse sollen im DOM aktualisiert werden. 

d) Implementiere eine Funktion, die es erlaubt, Produkte nach Preis auf- oder absteigend zu sortieren. 
Füge entsprechende Buttons hinzu, um die Sortierrichtung auszuwählen. 

e) Erstelle eine Funktion, die ein Produkt nach seiner id sucht und dieses Produkt aus dem Array entfernt. 
Füge ein Eingabefeld für die id und einen Button zum Entfernen hinzu.   */

// Dark Mode
const toggleBtn = document.getElementById("toggle-mode");
toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");
    console.log("Aktuelle Body-Klasse:", document.body.className);
});

// Produkte Array
const produkte = [
    { id: 1, name: "Apfel", preis: 0.5, kategorie: "Obst" },
    { id: 2, name: "Brot", preis: 1.2, kategorie: "Backwaren" },
    { id: 3, name: "Milch", preis: 0.8, kategorie: "Getränke" },
    { id: 4, name: "Käse", preis: 2.5, kategorie: "Milchprodukte" },
    { id: 5, name: "Karotte", preis: 0.3, kategorie: "Gemüse" }
];

// DOM-Elemente
const produktListe = document.getElementById("produkt-liste");
const suchInput = document.getElementById("such-input");
const suchButton = document.getElementById("such-button");
const sortAscButton = document.getElementById("sort-asc-button");
const sortDescButton = document.getElementById("sort-desc-button");
const entfernenInput = document.getElementById("entfernen-input");
const entfernenButton = document.getElementById("entfernen-button");

// Produkte anzeigen
function zeigeProdukte(array) {
    produktListe.innerHTML = "";
    array.forEach(produkt => {
        const produktDiv = document.createElement("div");
        produktDiv.classList.add("produkt");

        produktDiv.innerHTML = `
            <p>ID: ${produkt.id}</p>
            <p>Name: ${produkt.name}</p>
            <p>Preis: €${produkt.preis.toFixed(2)}</p>
            <p>Kategorie: ${produkt.kategorie}</p>
        `;
        produktListe.appendChild(produktDiv);
    });
}

// Initial anzeigen
zeigeProdukte(produkte);

// Suche
function sucheProdukte() {
    const suchBegriff = suchInput.value.toLowerCase();
    const gefilterteProdukte = produkte.filter(p => p.name.toLowerCase().includes(suchBegriff));
    zeigeProdukte(gefilterteProdukte);
}

// Suchbutton klicken
suchButton.addEventListener("click", sucheProdukte);

// Enter-Taste im Suchfeld
suchInput.addEventListener("keyup", e => {
    if (e.key === "Enter") sucheProdukte();
});

// Sortieren
sortAscButton.addEventListener("click", () => {
    zeigeProdukte([...produkte].sort((a, b) => a.preis - b.preis));
});

sortDescButton.addEventListener("click", () => {
    zeigeProdukte([...produkte].sort((a, b) => b.preis - a.preis));
});

// Entfernen
entfernenButton.addEventListener("click", () => {
    const id = parseInt(entfernenInput.value);
    const index = produkte.findIndex(p => p.id === id);
    if (index !== -1) {
        produkte.splice(index, 1);
        zeigeProdukte(produkte);
        entfernenInput.value = "";
    } else {
        alert("Produkt mit dieser ID nicht gefunden.");
    }
});

// Enter-Taste im Entfernen-Feld
entfernenInput.addEventListener("keyup", e => {
    if (e.key === "Enter") entfernenButton.click();
});
