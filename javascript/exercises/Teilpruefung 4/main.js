/*Du arbeitest an einem Webprojekt für einen Online-Shop, der spezialisiert ist auf den Verkauf von handgefertigten Dekorationsartikeln. 
Deine Aufgabe ist es, eine interaktive Produktgalerie zu erstellen. 
Die Galerie soll folgende Funktionalitäten haben: 

a) Lade die Produktinformationen aus einem JSON-String, der Produktname, Preis und eine URL zum Bild jedes Produkts enthält. 
Parse diesen JSON-String zu einem JavaScript-Objekt. 

b) Erstelle für jedes Produkt in der Liste ein neues DOM-Element, das ein Bild (img), den Produktnamen (h3) und den Preis (p) enthält. 
Setze die entsprechenden Werte aus dem JSON-Objekt. 

c) Platziere jedes dieser neuen Elemente in einem Container-Element auf der Webseite. 

d) Füge jedem Produkt eine Schaltfläche hinzu, die es ermöglicht, das Produkt zum "Warenkorb" hinzuzufügen. 
Bei Klick auf diese Schaltfläche soll eine Funktion aufgerufen werden, 
die den Namen und den Preis des Produkts in der Konsole ausgibt, 
als Simulation, dass das Produkt zum Warenkorb hinzugefügt wurde.  
 */
//a)
const produkteJSON =`
[
{"produktname":"Vase orange", "preis":19.99, "url":"images/vase-01.jpg"},
{"produktname":"Vase weiß", "preis":24.99, "url":"images/vase-02.jpg"},
{"produktname":"Vase rund", "preis":15.99, "url":"images/vase-03.jpg"},
{"produktname":"Vase lila", "preis":16.99, "url":"images/vase-04.jpg"},
{"produktname":"Vase rot", "preis":17.99, "url":"images/vase-05.jpg"}
]
`;
const produkte = JSON.parse(produkteJSON);
// console.log(produkte); log zur kontrolle

// c) 
const container = document.querySelector("#produkt-container");


//b)
produkte.forEach(produkt=> {
    const produktDiv = document.createElement("div");
    produktDiv.classList.add("produkt"); // für eine kleine styleanpassung
    const img = document.createElement("img") // bild
    img.src = produkt.url

    const h3 = document.createElement("h3"); // name
    h3.innerText = produkt.produktname;

    const p = document.createElement("p"); // preis
    p.innerText = `${produkt.preis} €`;

   // d
   const button = document.createElement("button");
   button.innerText = "Zum Warenkorb";
   button.addEventListener("click", ()=>{
    console.log(`${produkt.produktname} für ${produkt.preis} € wurde zum Warenkorb hinzugefügt!`);
   });

   

    container.appendChild(produktDiv);
    produktDiv.appendChild(img);
    produktDiv.appendChild(h3);
    produktDiv.appendChild(p);
    produktDiv.appendChild(button);

})
