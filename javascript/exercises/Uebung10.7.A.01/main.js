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

// a) Produkte Array
const produkte = [
    { id: 1, name: "Apfel", preis: 0.5, kategorie: "Obst" },
    { id: 2, name: "Brot", preis: 1.2, kategorie: "Backwaren" },
    { id: 3, name: "Milch", preis: 0.8, kategorie: "Getränke" },
    { id: 4, name: "Käse", preis: 2.5, kategorie: "Milchprodukte" },
    { id: 5, name: "Karotte", preis: 0.3, kategorie: "Gemüse" }
];

// DOM-Elemente müssen vor dem aufruf der funktionen bereit stehen
const produktListe = document.getElementById("produkt-liste"); //b)
const suchInput = document.getElementById("such-input"); //c)
const suchButton = document.getElementById("such-button"); //c)
const sortAscButton = document.getElementById("sort-asc-button"); //d)
const sortDescButton = document.getElementById("sort-desc-button"); //d)
const entfernenInput = document.getElementById("entfernen-input"); //e)
const entfernenButton = document.getElementById("entfernen-button"); //e)

// b) Produkte anzeigen
function zeigeProdukte(array) {     // zeigt das array das man der funktion gibt
    produktListe.innerHTML = "";    // <div id="produkt-liste"> wird leer geräumt, damit nicht alte Produkte stehen bleiben.
    array.forEach(produkt => {      // für jedes produkt aus dem array...
        const produktDiv = document.createElement("div");   //...erzeuge ein neues HTML Element: produktDiv = <div></div>
        produktDiv.classList.add("produkt");        //classList fügt dem Element (produktDiv) die Klasse produkt hinzu. <div class="produkt"></div>

        produktDiv.innerHTML = `           
            <p>ID: ${produkt.id}</p>
            <p>Name: ${produkt.name}</p>
            <p>Preis: €${produkt.preis.toFixed(2)}</p>
            <p>Kategorie: ${produkt.kategorie}</p>
        `;      // HTML inhalte werden in das neue div eingefügt
        produktListe.appendChild(produktDiv);       //der erzeugte HTML Block wird an die Produktliste angehängt
    });
}

// Funktion ausführen zum anzeigen der Produkte
zeigeProdukte(produkte);

// c) Suche
function sucheProdukte() {
    const suchBegriff = suchInput.value.toLowerCase();
    const gefilterteProdukte = produkte.filter(p => p.name.toLowerCase().includes(suchBegriff));
    zeigeProdukte(gefilterteProdukte); // zeigt die gefilterten produkte an, die funktion entfernt vorherige produkte aus der anzeige.
}

// Suchbutton klicken
suchButton.addEventListener("click", sucheProdukte);

// Enter-Taste im Suchfeld
suchInput.addEventListener("keyup", e => {
    if (e.key === "Enter") sucheProdukte();
});

// d) Sortieren
sortAscButton.addEventListener("click", () => {
    zeigeProdukte([...produkte].sort((a, b) => a.preis - b.preis));
});

sortDescButton.addEventListener("click", () => {
    zeigeProdukte([...produkte].sort((a, b) => b.preis - a.preis));
});

// e) Entfernen
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


/* Lösung 10.7.A.01

a) Das Array von Produktobjekten könnte wie folgt aussehen: 

const produkte = [ 
  { id: 1, name: "Tasse", preis: 9.99, kategorie: "Küchenutensilien" }, 
  { id: 2, name: "Teller", preis: 14.99, kategorie: "Küchenutensilien" }, 
  { id: 3, name: "Messer", preis: 19.99, kategorie: "Küchenutensilien" }, 
  { id: 4, name: "Gabel", preis: 5.99, kategorie: "Küchenutensilien" }, 
  { id: 5, name: "Löffel", preis: 3.99, kategorie: "Küchenutensilien" } 
]; 
 

b) Funktion zum Einbinden aller Produkte ins DOM: 

function produkteAnzeigen() { 
  const produktContainer = document.getElementById('produktContainer'); 
  produktContainer.innerHTML = ''; // Vorherige Inhalte löschen 
  produkte.forEach(produkt => { 
    const produktDiv = document.createElement('div'); 
    produktDiv.innerHTML = `<h3>${produkt.name}</h3><p>ID: ${produkt.id}</p><p>Preis: ${produkt.preis}€</p><p>Kategorie: ${produkt.kategorie}</p>`; 
    produktContainer.appendChild(produktDiv); 
  }); 
} 
 

c) Suchfunktion: 

function produkteSuchen() { 
  const suchText = document.getElementById('suche').value.toLowerCase(); 
  const gefilterteProdukte = produkte.filter(produkt => produkt.name.toLowerCase().includes(suchText)); 
  // Anzeige der gefilterten Produkte 
  produkteAnzeigen(gefilterteProdukte); 
} 
 

d) Sortierfunktion: 

function produkteSortieren(nach, aufsteigend = true) { 
  produkte.sort((a, b) => { 
    if (aufsteigend) return a[nach] - b[nach]; 
    else return b[nach] - a[nach]; 
  }); 
  produkteAnzeigen(); 
} 
 

e) Funktion zum Entfernen eines Produkts: 

function produktEntfernen(produktId) { 
  const index = produkte.findIndex(produkt => produkt.id === produktId); 
  if (index > -1) { 
    produkte.splice(index, 1); 
    produkteAnzeigen(); 
  } 
}  */