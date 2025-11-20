/* Erstelle eine JavaScript-Funktion createGallery, die ein Array von Bild-URLs entgegennimmt 
und eine Bildergalerie im DOM erzeugt. Jedes Bild soll in einem div-Element mit der Klasse gallery-item eingebettet sein. 
Verwende dazu die Methode document.createElement für jedes Bild und document.querySelector um das Element auszuwählen, 
in das die Galerie eingefügt werden soll. 
Die Funktion soll auch überprüfen, ob das übergebene Array leer ist. 
In diesem Fall soll ein p-Element mit dem Text "Keine Bilder verfügbar" in das Ziel-Element eingefügt werden. 
Nutze Arrow-Funktionen, wo immer es möglich ist, und achte darauf, dass du let oder const für Variablendeklarationen verwendest. 
Verwende keine externen Bibliotheken oder Frameworks.   */

const galerieContainer = document.querySelector("#galerie"); // hier werden später die div.gallery-item eingefügt so kann man ggfls allen items leichter einen style geben


const bilderArray = 
[
    "images/vase-01.jpg", 
    "images/vase-02.jpg", 
    "images/vase-03.jpg", 
    "images/vase-04.jpg", 
    "images/vase-05.jpg"
];
const leerArray = [];
// prüfen ob das array leer ist mit beispielarray.length === 0
// jedes bild kommt als <img> element in die <div class="gallery-item"> wenn das array nicht leer ist


const createGallery = beispielarray => {

    galerieContainer.innerHTML = ""; // damit der inhalt des containers geleert wird bevor neue bilder reinkommen

    if (beispielarray.length === 0) { // prüfen, ob das Array leer ist,
        const keinBild = document.createElement("p");
        keinBild.innerText = "Keine Bilder verfügbar";
        galerieContainer.appendChild(keinBild);
        return;
    } 
     else {
        // dann einer Schleife über das Array gehen und die einzelnen Bilder erstellen
        beispielarray.forEach (url => {
            const item = document.createElement("div");
            item.classList.add("gallery-item"); //wird zu <div class="gallery-item"></div>
            const img = document.createElement("img");
            img.src = url; // führt im HTML zu <img src="url"> ABER in JavaScript setzt man die eigenschaften mit =. Also url ist die Variable, die bei jedem Schleifendurchlauf den aktuellen Wert aus dem Array enthält.
            galerieContainer.appendChild(item); // das div wird in den container eingefügt
            item.appendChild(img); // das img wird in das div.gallery-item eingefügt
        });
    }
};
createGallery(leerArray); // test für das array ohne bilder  
createGallery(bilderArray);
