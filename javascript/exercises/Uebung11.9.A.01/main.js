/* Entwickle eine interaktive Webanwendung, die folgende Funktionalitäten umfasst: 

a) Erstelle eine HTML-Seite mit einem leeren div-Element. 
Verwende JavaScript, um dynamisch eine Liste von Produkten (mindestens 5 verschiedene Produkte) in diesem div anzuzeigen. 
Jedes Produkt soll aus einem Namen, einer Beschreibung und einem Preis bestehen. 
Nutze Arrays und Objekte, um die Produktdaten zu speichern.  

b) Füge eine Suchfunktion hinzu, die es ermöglicht, die Liste der Produkte nach Namen zu filtern. 
Nutze dabei ein Eingabefeld und einen Button. 
Die Filterung soll in Echtzeit erfolgen, sobald der Nutzer den Button klickt. 

c) Implementiere eine Funktion, die es erlaubt, Produkte nach ihrem Preis zu sortieren (aufsteigend und absteigend). 
Füge zwei Buttons hinzu, um die Sortierrichtung auszuwählen. 

d) Erstelle ein Feature, bei dem Nutzer auf ein Produkt klicken können, 
um eine detaillierte Ansicht dieses Produkts in einem neuen div-Element anzuzeigen. 
Dies soll das Bild des Produkts (verwende eine URL als Platzhalter), den Namen, die Beschreibung und den Preis beinhalten. 

e) Implementiere ein einfaches Bewertungssystem, bei dem Nutzer Produkte mit Sternen (1 bis 5) bewerten können. 
Speichere die Bewertungen in einem Array und zeige den Durchschnitt der Bewertungen neben dem Produktnamen an. 

f) Nutze das window-object, um die Größe des Browserfensters zu überwachen. 
Wenn das Fenster eine bestimmte Größe unterschreitet, passe die Anzeige der Produkte automatisch an 
(z.B. weniger Spalten in der Produktliste). */

// a) Produkte Array
const produkte = [
    { name: "Apfel", preis: 0.5, beschreibung: "Ein Apfel hat die Kategorie Obst", bewertungen: [] },
    { name: "Brot", preis: 1.2, beschreibung: "Ein Brot gehört zur Kategorie Backwaren", bewertungen: [] },
    { name: "Milch", preis: 0.8, beschreibung: "Milch wird unter der Kategorie Getränke geführt", bewertungen: [] },
    { name: "Käse", preis: 2.5, beschreibung: "Käse lässt sich als Milchprodukt beschreiben.", bewertungen: [] },
    { name: "Karotte", preis: 0.3, beschreibung: "Eine Karotte ist ein Gemüse", bewertungen: [] }
];

// DOM-Elemente müssen vor dem Aufruf der Funktion bereit stehen
const produktListe = document.getElementById("produkt-container"); 
const suchInput = document.getElementById("such-input");
const suchButton = document.getElementById("such-button");
const sortAscButton = document.getElementById("sort-asc-button");
const sortDescButton = document.getElementById("sort-desc-button");
const detailContainer = document.getElementById("detail-container");

// Hilfsfunktion: Durchschnitt einer Produktbewertung berechnen
function durchschnitt(produkt) {
    if (produkt.bewertungen.length === 0) return 0;
    const sum = produkt.bewertungen.reduce((a, b) => a + b, 0);
    return sum / produkt.bewertungen.length;
}

// Hilfsfunktion: Sternebild setzen
function setStarImage(starsImg, rating) {
    const r = Math.round(rating);
    starsImg.src = `images/stars-${r}.png`;
}

// Produkte anzeigen
function zeigeProdukte(array) {
    produktListe.innerHTML = ""; // Alte Produkte entfernen
    array.forEach((produkt, index) => {
        const produktDiv = document.createElement("div");  
        produktDiv.classList.add("produkt");  
        const bildPfad = `images/vase-${index + 1}.jpg`;

        // Produkt HTML inkl. Durchschnittsbewertung und Sternbild
        produktDiv.innerHTML = `           
            <p><strong>Produktname: </strong>${produkt.name}</p>
            <p><strong>Preis:</strong> €${produkt.preis.toFixed(2)}</p>
            <p><strong>Produktbeschreibung:</strong> ${produkt.beschreibung}</p>
            <p><strong>Durchschnittsbewertung:</strong> <span class="avg-rating">${durchschnitt(produkt).toFixed(1)}</span> Sterne</p>
            <img src="images/stars-0.png" class="stars" style="width:200px; cursor:pointer;" alt="Bewertung">
        `;

        // Sternebild auf aktuellen Durchschnitt setzen
        const starsImg = produktDiv.querySelector(".stars");
        const avgSpan = produktDiv.querySelector(".avg-rating");
        setStarImage(starsImg, durchschnitt(produkt));

        produktListe.appendChild(produktDiv);

        // Sterne Hover / Click Event
        starsImg.addEventListener("mousemove", evt => {
            const width = starsImg.width;
            const pos = evt.offsetX;
            let hoverRating = 1;
            if (pos > width / 5 * 4) hoverRating = 5;
            else if (pos > width / 5 * 3) hoverRating = 4;
            else if (pos > width / 5 * 2) hoverRating = 3;
            else if (pos > width / 5) hoverRating = 2;

            setStarImage(starsImg, hoverRating);
        });

        starsImg.addEventListener("mouseout", () => {
            setStarImage(starsImg, durchschnitt(produkt));
        });

        starsImg.addEventListener("click", evt => {
            const width = starsImg.width;
            const pos = evt.offsetX;
            let rating = 1;
            if (pos > width / 5 * 4) rating = 5;
            else if (pos > width / 5 * 3) rating = 4;
            else if (pos > width / 5 * 2) rating = 3;
            else if (pos > width / 5) rating = 2;

            produkt.bewertungen.push(rating);
            setStarImage(starsImg, durchschnitt(produkt));
            avgSpan.textContent = durchschnitt(produkt).toFixed(1);
        });

        // Detailansicht bei Klick
        produktDiv.addEventListener("click", () => {
            detailContainer.innerHTML = `
                <div class="detail-box">
                    <img src="${bildPfad}" class="zoomit" style="width:150px; border-radius: 10px;">
                    <h2>${produkt.name}</h2>
                    <p><strong>Preis:</strong> €${produkt.preis.toFixed(2)}</p>
                    <p>${produkt.beschreibung}</p>
                    <p><strong>Durchschnitt:</strong> <span class="avg-detail">${durchschnitt(produkt).toFixed(1)}</span> Sterne</p>
                    <img src="images/stars-${Math.round(durchschnitt(produkt))}.png" class="stars-detail" style="width:200px; cursor:pointer;">
                </div>
            `;

            // Zoom Feature auf Detailansicht Image
            const zoomImg = detailContainer.querySelector(".zoomit");
            if (zoomImg) {
                zoomImg.onmouseover = () => zoomImg.classList.add("zoomIn");
                zoomImg.onmouseout = () => zoomImg.classList.remove("zoomIn");
                zoomImg.ontouchend = () => zoomImg.classList.toggle("zoomIn");
            }

            // Detailfenster scrollen
            detailContainer.scrollIntoView({ behavior: "smooth", block: "start" });

            // Detailbereich Sterne Events
            const starsDetail = detailContainer.querySelector(".stars-detail");
            const avgDetailSpan = detailContainer.querySelector(".avg-detail");

            starsDetail.addEventListener("mousemove", evt => {
                const width = starsDetail.width;
                const pos = evt.offsetX;
                let hoverRating = 1;
                if (pos > width / 5 * 4) hoverRating = 5;
                else if (pos > width / 5 * 3) hoverRating = 4;
                else if (pos > width / 5 * 2) hoverRating = 3;
                else if (pos > width / 5) hoverRating = 2;
                setStarImage(starsDetail, hoverRating);
            });

            starsDetail.addEventListener("mouseout", () => {
                setStarImage(starsDetail, durchschnitt(produkt));
            });

            starsDetail.addEventListener("click", evt => {
                const width = starsDetail.width;
                const pos = evt.offsetX;
                let rating = 1;
                if (pos > width / 5 * 4) rating = 5;
                else if (pos > width / 5 * 3) rating = 4;
                else if (pos > width / 5 * 2) rating = 3;
                else if (pos > width / 5) rating = 2;

                produkt.bewertungen.push(rating);
                setStarImage(starsDetail, durchschnitt(produkt));
                avgDetailSpan.textContent = durchschnitt(produkt).toFixed(1);

                // Optional auch Durchschnitt in Produktliste aktualisieren
                const avgSpanList = produktDiv.querySelector(".avg-rating");
                avgSpanList.textContent = durchschnitt(produkt).toFixed(1);
            });
        });
    });
}

// Funktion ausführen zum Anzeigen der Produkte
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
