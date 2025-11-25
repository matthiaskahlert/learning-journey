/* Aufgabe: Events
Erstelle ein JavaScript-Skript, das folgende Funktionalitäten umsetzt: 

a) Definiere eine Funktion createGallery, die ein Array von Bild-Objekten entgegennimmt. 
Jedes Bild-Objekt soll zwei Eigenschaften haben: src (den Pfad zur Bilddatei) und title (den Titel des Bildes). 
Die Funktion soll für jedes Bild-Objekt im Array ein neues <img>-Element im DOM unter einem vorher definierten <div>-Element mit der ID gallery erstellen. 
Jedes <img>-Element soll die src- und title-Attribute entsprechend den Eigenschaften des Bild-Objekts setzen. 

b) Füge jedem <img>-Element einen mouseover-Event-Handler hinzu, der das Bild beim Darüberfahren mit der Maus auf die doppelte Größe skaliert. 
Beim Verlassen des Bildes mit der Maus (mouseout) soll das Bild wieder auf seine ursprüngliche Größe zurückgesetzt werden. 

c) Erstelle eine Funktion toggleTheme, die das Farbschema der Webseite zwischen einem hellen und einem dunklen Modus wechselt, 
indem sie die Klasse dark-theme zum <body>-Tag hinzufügt oder entfernt. 
Verknüpfe diese Funktion mit einem Tastatur-Event, das ausgelöst wird, wenn der Nutzer die Taste D drückt. */

const galerieContainer = document.querySelector("#galerie"); // hier werden später die div.gallery-item eingefügt so kann man ggfls allen items leichter einen style geben


const bilderArray = 
[
    { src: "images/vase-1.jpg", title: "vase01" }, 
    { src: "images/vase-2.jpg", title: "vase02" },
    { src: "images/vase-3.jpg", title: "vase03" },
    { src: "images/vase-4.jpg", title: "vase04" },
    { src: "images/vase-5.jpg", title: "vase05" }

];
const leerArray = [];
// prüfen ob das array leer ist mit beispielarray.length === 0
// jedes bild kommt als <img> element in die <div class="gallery-item"> wenn das array nicht leer ist


const createGallery = (beispielarray) => {

    galerieContainer.innerHTML = ""; // alten Inhalt löschen

    // Wenn Array leer - Meldung anzeigen
    if (beispielarray.length === 0) {
        const keinBild = document.createElement("p");
        keinBild.innerText = "Keine Bilder verfügbar";
        galerieContainer.appendChild(keinBild);
        return;
    }

    // Galerie erzeugen
    beispielarray.forEach(imgObj => {

        const item = document.createElement("div");
        item.classList.add("gallery-item");

        const img = document.createElement("img");
        img.src = imgObj.src;
        img.alt = imgObj.title;
        img.title = imgObj.title;

        // Zoom-Effekte (Aufgabe b)
        img.addEventListener("mouseover", () => {
            img.style.transform = "scale(2)";
            img.style.transition = "1s";
        });

        img.addEventListener("mouseout", () => {
            img.style.transform = "scale(1)";
        });

        item.appendChild(img);
        galerieContainer.appendChild(item);
    });
};

createGallery(leerArray); // test für das array ohne bilder  
createGallery(bilderArray);

function toggleTheme() {
    document.body.classList.toggle("dark-theme");
}

// taste D zum Theme umschalten
document.addEventListener("keydown", (e) => {
    if (e.key.toLowerCase() === "d") {
        toggleTheme();
    }
});

