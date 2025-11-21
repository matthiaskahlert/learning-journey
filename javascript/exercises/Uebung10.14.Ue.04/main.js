/* Entwickle eine JavaScript-Funktion, die eine Liste von Produktnamen und deren Preise als Array von Objekten entgegennimmt. 
Die Funktion soll dann ein neues DOM-Element für jedes Produkt erstellen, 
das den Produktnamen und den Preis in einem <div>-Element anzeigt. 
Verwende dabei folgende Kriterien: 

a) Nutze eine Schleife, um über das Array zu iterieren. 

b) Für jedes Produkt soll ein neues <div>-Element erstellt werden, das den Namen und Preis des Produkts enthält. 
Nutze dabei Template Strings, um die Inhalte einzufügen. 

c) Füge jedes <div>-Element einem vorher im HTML-Dokument definierten Container-Element hinzu. 
Verwende dafür einen CSS-Selektor, um auf den Container zuzugreifen. 

d) Stelle sicher, dass deine Funktion auch prüft, ob der Container im DOM existiert, bevor sie versucht, Elemente hinzuzufügen. 

e) Optional: Setze CSS-Styles über JavaScript, um den neu erstellten <div>-Elementen ein einheitliches Aussehen zu geben. */


const produktArray =
[
{produktname:"Vase orange", preis:19.99},
{produktname:"Vase weiß", preis:24.99},
{produktname:"Vase rund", preis:15.99},
{produktname:"Vase lila", preis:16.99},
{produktname:"Vase rot", preis:17.99}
];


 

function createProducts (productArray) {
  
const container = document.querySelector("#produkt-container");
  if (!container) {
      console.error("Container nicht gefunden!");
      return;
  }

produktArray.forEach(produkt=> {
  const produktDiv = document.createElement("div");
  produktDiv.classList.add("produkt"); 

  const h3 = document.createElement("h3");
  h3.innerText = produkt.produktname;

  const p = document.createElement("p");
  p.innerText = `${produkt.preis} €`; //templatestring

 
  container.appendChild(produktDiv);
  produktDiv.appendChild(h3);
  produktDiv.appendChild(p);
  produktDiv.style.backgroundColor = "#f5f5f5"; // style per js, rest per css


})
}
createProducts(produktArray);