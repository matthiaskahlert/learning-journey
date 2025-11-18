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

// Button auswählen
const toggleBtn = document.getElementById("toggle-mode");

// Klick-Event zum Umschalten
toggleBtn.addEventListener("click", () => {
    const body = document.body;

    // Prüfen, ob dark vorhanden ist
    if (body.classList.contains("dark")) {
        body.classList.remove("dark");
        body.classList.add("light");
    } else {
        body.classList.remove("light");
        body.classList.add("dark");
    }

    console.log("Aktuelle Body-Klasse:", body.className);
});
/* Seite startet hell (class="light").

Klick auf „Dark Mode ein/aus“ → wechselt zu class="dark".

Klick nochmal → wieder class="light".

CSS verändert automatisch Hintergrund und Textfarbe, weil wir unterschiedliche Klassen definiert haben. */


