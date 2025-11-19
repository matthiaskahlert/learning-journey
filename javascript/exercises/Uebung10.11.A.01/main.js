/* Erstelle eine JavaScript-Funktion createGallery, die ein Array von Bild-URLs entgegennimmt 
und eine Bildergalerie im DOM erzeugt. Jedes Bild soll in einem div-Element mit der Klasse gallery-item eingebettet sein. 
Verwende dazu die Methode document.createElement für jedes Bild und document.querySelector um das Element auszuwählen, 
in das die Galerie eingefügt werden soll. 
Die Funktion soll auch überprüfen, ob das übergebene Array leer ist. 
In diesem Fall soll ein p-Element mit dem Text "Keine Bilder verfügbar" in das Ziel-Element eingefügt werden. 
Nutze Arrow-Funktionen, wo immer es möglich ist, und achte darauf, dass du let oder const für Variablendeklarationen verwendest. 
Verwende keine externen Bibliotheken oder Frameworks.   */

const galerieContainer = document.querySelector("#galerie"); // hier werden später die div.gallery-item eingefügt


const beispielarray = 
[
    "images/vase-01.jpg", 
    "images/vvase-02.jpg", 
    "images/vvase-03.jpg", 
    "images/vvase-04.jpg", 
    "images/vvase-05.jpg"
];

// prüfen ob das array ist mit beispielarray.length === 0
// jedes bild kommt als <img> element in die <div id="galerie"> wenn das array nicht leer ist


const createGallery = (beispielarray) => {
    if (beispielarray.length === 0) { // prüfen, ob das Array leer ist,
        const keinBild = document.createElement("p");
        keinBild.innerText = "Keine Bilder verfügbar";
        galerieContainer.appendChild(keinBild);
        return;
    } else {
        // dann einer Schleife über das Array gehen und die einzelnen Bilder erstellen
        beispielarray.forEach()
    }
};
/*  
bilderUrls.forEach(url => {
  const item = document.createElement("div");
  item.classList.add("gallery-item");

  const img = document.createElement("img");
  img.src = url;

  item.appendChild(img);
  galerieContainer.appendChild(item);
});*/
