/* Entwickle eine kleine Webanwendung, die eine Liste von Büchern anzeigt. Jedes Buch soll als ein Objekt repräsentiert werden, das folgende Eigenschaften hat: Titel, Autor, Jahr der Veröffentlichung und eine ID. Die Anwendung soll folgende Funktionalitäten umfassen:  

a) Erstelle eine Klasse Buch mit einem Konstruktor, der die oben genannten Eigenschaften initialisiert. 

b) Erstelle ein Array buecherListe, das mehrere Bücher enthält, welche mit der Klasse Buch erstellt wurden. 

c) Verwende DOM-Methoden, um jedes Buch aus der buecherListe in der Webseite anzuzeigen. Jedes Buch soll in einem eigenen <div>-Element angezeigt werden, das den Titel, den Autor und das Jahr der Veröffentlichung enthält. 

d) Füge jedem Buch-<div> ein <button> hinzu, der "Löschen" sagt. Wenn dieser Button geklickt wird, soll das Buch aus der buecherListe entfernt und die Anzeige aktualisiert werden. 

e) Implementiere eine Funktion aktualisiereAnzeige(), die die Anzeige aktualisiert, indem sie die Liste der Bücher neu aus dem buecherListe Array lädt und anzeigt. 

f) Nutze CSS-Selektoren, um jedem Buch-<div> einen einheitlichen Stil zu geben und die Lesbarkeit zu verbessern.   */

class Buch {
    constructor(titel, autor, veröffentlichungsjahr, id) {
        this.titel = titel;
        this.autor = autor;
        this.veröffentlichungsjahr = veröffentlichungsjahr;
        this.id = id;
    }
}

const buecherListe = [
    new Buch("Der Alchimist", "Paulo Coelho", 1988, 1),
    new Buch("1984", "George Orwell", 1949, 2),
    new Buch("Die Verwandlung", "Franz Kafka", 1915, 3),
    new Buch("Der kleine Prinz", "Antoine de Saint-Exupéry", 1943, 4)
];
const container = document.querySelector("#buch-container");

const aktualisiereAnzeige = () => {
    container.innerHTML = ""; // Container leeren

    buecherListe.forEach(buch => {
        const div = document.createElement("div");
        div.innerText = `${buch.titel} - ${buch.autor} - (${buch.veröffentlichungsjahr})`;
        
        const loeschenButton = document.createElement("button");
        loeschenButton.innerText = "Löschen";
            
        loeschenButton.addEventListener("click", () => {
            const index = buecherListe.findIndex(b => b.id === buch.id);
            if (index !== -1) buecherListe.splice(index, 1); // buch entfernen
                
            // anzeige aktualisieren
            aktualisiereAnzeige();
        });

        
        div.appendChild(loeschenButton);
        container.appendChild(div);
        
});


}
aktualisiereAnzeige();

//f) Nutze CSS-Selektoren, um jedem Buch-<div> einen einheitlichen Stil zu geben und die Lesbarkeit zu verbessern.
const style = document.createElement("style");
style.innerHTML = `
    #buch-container div {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px 0;
        background-color: #f9f9f9;
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: space-between; /* Text links, Button rechts */
        align-items: center;
        
    }
    #buch-container button {
        margin-left: 20px;
        padding: 5px 10px;
        background-color: #ff4d4d;
        color: white;   
        border: none;
        cursor: pointer;
    }
    #buch-container button:hover {
        background-color: #ff1a1a;
    }
    #buch-container div:nth-child(even) {
    background-color: #e9e9e9;
}

`;
document.head.appendChild(style);   

/* Musterlösung:
class Buch { 
  constructor(titel, autor, jahr, id) { 
    this.titel = titel; 
    this.autor = autor; 
    this.jahr = jahr; 
    this.id = id; 
  } 
} 
 
let buecherListe = [ 
  new Buch("Buch 1", "Autor 1", 2020, 1), 
  new Buch("Buch 2", "Autor 2", 2019, 2), 
  new Buch("Buch 3", "Autor 3", 2021, 3) 
]; 
 
function buchHinzufuegenZumDOM(buch) { 
  const div = document.createElement('div'); 
  div.className = 'buch'; 
  div.innerHTML = `<h2>${buch.titel}</h2><p>${buch.autor}</p><p>${buch.jahr}</p>`; 
  const loeschButton = document.createElement('button'); 
  loeschButton.textContent = 'Löschen'; 
  loeschButton.onclick = function() { 
    buecherListe = buecherListe.filter(b => b.id !== buch.id); 
    aktualisiereAnzeige(); 
  }; 
  div.appendChild(loeschButton); 
  document.body.appendChild(div); 
} 
 
function aktualisiereAnzeige() { 
  document.body.innerHTML = ''; 
  buecherListe.forEach(buch => buchHinzufuegenZumDOM(buch)); 
} 
 
aktualisiereAnzeige(); */