// vibe coding für darkmode, um body klassen zu verstehen
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















const menu = document.getElementById("menu"); // document.getElementById() ist eine DOM-Methode, 
// mit der ich ein bestimmtes HTML-Element über seinen eindeutigen id-Wert auswähle
// alles zwischen den backticks wird in das nav Element geschrieben    
menu.innerHTML = ` 
    <ul>
        <li><a href="page1">Seite 1</a></li>
        <li><a href="page1">Seite 2</a></li>
    </ul>`;

    const regal = document.getElementById("regal");
    console.log(regal.innerHTML);

    const ps = document.getElementsByTagName("p");
    console.log("ps", ps);
    const items = document.getElementsByClassName("item"); // Die collection enthält alle Elemente mit der Klasse "item"
    console.log("items", items);

    const id = regal.id;
    console.log("regal", id);
    const className = regal.className;
    console.log("className", className);
    const attr = regal.getAttribute("class");
    console.log("attr", attr);
    regal.setAttribute("class", "cart");
    

    regal.style.color = "#000000ff";
    regal.style.backgroundColor = "lavender";
    regal.style.backgroundImage = "url('images/flowers-01.avif')";
    regal.style.border = "3px solid green";
    regal.style.boxShadow = "10px 20px 15px silver";
    regal.style.fontSize = "2rem"
    regal.style.height = "200px";
    regal.style.maxWidth = "96%";
    regal.style.opacity = "0.8";
    regal.style.padding = "1rem";
    regal.style.textAlign = "center";

    const elem = document.getElementById("get-set"); // elem ist nun eine Referenz auf das DOM element <div id="get-set"> 
    const getSet = elem.style.cssText; // elem.style.cssText enthält alle Inline-Styles, die direkt im style="" des Elements stehen
    // also enthält elem.style.cssText hier aus der index.html: style="background: seashell; border: 2px solid orange">
    console.log("getSet", getSet);


    // nun wird noch ein style hinzugefügt. 
    elem.style.cssText += // Die Kombination von +und = konkateniert die vorhandenen Stile mit dem neuen String, sprich, es führt die Strings zusammen.
        `box-shadow: 5px 10px 5px silver;
        text-align: center`;
/* der background stil sieht nach der konkatenation nun so aus:
style="background: seashell; border: 2px solid orange; 
       box-shadow: 5px 10px 5px silver; text-align: center;"
 */
const item = document.getElementById("item");
console.log("item", item); // log: item null
// Wenn item nicht existiert, gibt die zuweisung null zurück
if (item !== null){
    item.style.cssText = "font-size: 2rem";
    
}
const header = document.querySelector("header");
console.log(header);

// const li = document.querySelector("nav li:nth-child(2)"); // "nav li:nth-child(2)" bedeutet: gehe ins nav element, suche dort alle <li elemente, nimm das zweite <li> (nth-child(2)). 
// const li = document.querySelector("nav li:nth-of-type(2)");
// const link = li.querySelector("a");
const link1 = document.querySelector("nav li a[href='cd.html']"); // hier wird direkt das <a>-Element mit dem href="cd.html" ausgewählt!
link1.innerText = "Css Datei" ;

console.log("link", link1);


const elem2 = document.querySelector(".selector");
console.log("elem", elem2);

const listElems = document.querySelectorAll(".list li"); // finde alle <li> in einem Element mit class="list"
console.log("listElems", listElems);

listElems.forEach( item => console.log(item.innerText));
console.log("listElems[2]", listElems[2].innerText); // listElems[2] Der Herr der Ringe Zum Warenkorb


// Dom Navigation

const parent = document.querySelector(".parent");

 // parent.children [1].firstElementChild erreicht das Bild unter dem mittleren figure-Element
console.log(parent.children [1].firstElementChild);
 // parent.children [1].firstElementChild erreicht mit lastElementChild das figcaption Element
parent.children [1].lastElementChild.innerText = "Poster 2: eine große runde Dose";

const block = parent.parentElement;
console.log("block", block.className);


const p = document.querySelector("#innertext p");
console.log("innerText", p.innerText);
console.log("textContent", p.textContent);

listElems[2].innerHTML = `Ab die Post <button id="b4">Zum Warenkorb</button>`;
const style =
`background: green;
color: white;`;
listElems[2].querySelector ("#b4").style.cssText = style;

// element einfügen: Das Skript setzt das Bild mit insertBefore(img, figcaption) vor die Bildunterschrift.



const figcaption = document.querySelector(".stifte figcaption");

const img = document.createElement('img');
img.setAttribute ("src", "images/stifte-03.avif");
img.setAttribute ("width", "70%");
img.setAttribute ("height", "70%");

figcaption.parentElement.insertBefore(img,figcaption);

// aufgabe ein array aus Objekten in das html einfügen:

const vasen = [
  {"src": "images/vase-01.jpg", "name": "Hohe Tonvase"},
  {"src": "images/vase-02.jpg", "name": "Weiße Keramik"},
  {"src": "images/vase-03.jpg", "name": "Cracked Porzellan"}
];

// Ein Array als »Zwischenspeicher« - Statt die Elemente sofort ins DOM zu setzen, bauen wir sie zuerst in JS auf.
const lis = [];

// In der forEach-Schleife die Elemente zusammensetzen
// und im Array lis ablegen.

vasen.forEach((elem) => {
  const li = document.createElement("li");
  const img = document.createElement("img");
  img.src = elem.src;
  img.alt = elem.name;
  li.append(img);
  lis.push(li);
});

document.querySelector(".target").prepend(...lis); // sucht das erste Element mit der Klasse .target, spread operator teils lis auf und übergibt jedes <li> einzeln.


// einfacherer Weg
const imgs = [
  `<img src="images/vase-04.jpg" alt="Steingutvase" />`,
  `<img src="images/vase-05.jpg" alt="Rote Porzellanvase" />`
]

for (const item of imgs) {
    const li = document.createElement ("li");
    li.innerHTML = item;
    document.querySelector(".target").append (li);
}


// Das Skript nutzt das umfassende HTML-Element mit id="trio" und erreicht das 
// vorhandene img-Element mit dem Selektor #trio img.

const trio = document.querySelector("#trio img");

const img02 = document.createElement("img");
img02.src = "images/stifte-02.png";
img02.width = 500;
img02.height = 540;

const img03 = document.createElement("img");
img03.src = "images/stifte-03.avif";
img03.width = 500;
img03.height = 540;

trio.before(img02);
trio.after(img03);



// Übung 10.8 Elemente im DOM einbinden
/* Füge ein neues Element Geranien vor dem Eintrag Lilien in die Liste ein sowie
einen Eintrag Nelken vor dem gerade eingefügten Element Geranien. Nutze zwei
verschiedene Methoden, z.B. insertBefore() und before().

"Rosen", "Magnolien", "Lilien", "Flieder"

Beispiel: man möchte "Orange" vor "Banane" einfügen:
```html
<ul id="fruits">
  <li>Apfel</li>
  <li>Banane</li>
</ul>
```
```js
// 1. Eltern-Element auswählen
const ul = document.getElementById("fruits");

// 2. Referenz-Element auswählen (vor welchem Element soll das neue stehen?)
const banana = ul.children[1]; // das zweite <li> = Banane

// 3. Neues Element erstellen
const orange = document.createElement("li");
orange.innerText = "Orange";

// 4. Neues Element einfügen
ul.insertBefore(orange, banana);

    <ul class="blumen">
        <li>
            <p>Rosen</p>
        </li>
        <li>
            <p>Magnolien</p>
        </li>
        <li>
            <p>Lilien</p>
        </li>
        <li>
            <p>Flieder</p>
        </li>
    </ul>
*/

const uList = document.getElementById("blumen");
const lilien = uList.children[2];
const geranien = document.createElement("li");
geranien.innerText = "Geranien";
uList.insertBefore(geranien, lilien);

const neueBlumeLi = document.createElement("li"); // erzeuge ein leeres <li> als Element
const neueBlume = document.createElement("p");  // erzeuge ein leeres <p> als Inhaltselement
neueBlume.innerText="Nelken";   // erzeuge den Text für die Liste
neueBlumeLi.appendChild(neueBlume);  // inhalt ins ElternElement stecken also <p> mit dem neuen Text ins <li>
geranien.before(neueBlumeLi);

// Praxisbeispiel 10.9

const bücher = [
    {   
        "title": "Alice in Wunderland",
        "autor": "Carroll, Lewis",
        "jahr": "1865",
        "img": "alice-in-wunderland.jpg",
        "link": "alice.html"
    },

    {   
        "title": "Accidental Empires",
        "autor": "Cringely, Robert X.",
        "jahr": "1992",
        "img": "accidental-empires.jpg",
        "link": "accidental-empires.html"
    },

    {   
        "title": "Mummenschanz",
        "autor": "Achternbusch, Herbert",
        "jahr": "1972",
        "img": "mummenschanz.jpg",
        "link": "mummenschanz.html"
    },

    {   
        "title": "Verzauberter April",
        "autor": "von Arnim, Elizabeth",
        "jahr": "1922",
        "img": "verzauberter-april.jpg",
        "link": "verzauberter-april.html"
    }
];


const regal2 = document.getElementById("regal2");


for (const buch of bücher) {
    const container = document.createElement("div");
    container.className = "buch";

    console.log(container); // vier div elemente sind sichtbar, aber noch leer

    const title = document.createElement("p");
    title.className = "title";
    title.innerHTML = `${buch.title}<br>${buch.autor}`; //buchtitel und autor sind durch einen zeilenumbruch getrennt
    container.appendChild (title); //p element wird in das div element gehängt

    const jahr = document.createElement("time");
    jahr.innerHTML = `Erschienen ${buch.jahr}`; //text für das time element
    container.appendChild (jahr);

    const img = document.createElement("img")
    img.src = `images/${buch.img}`; // nimmt den img namen aus dem JSON array
    img.alt = `Titelbild von ${buch.title}`;
    img.loading = "lazy"; //lädt erst wenn sichtbar
    container.appendChild(img);

    let link = document.createElement("p");
    a = document.createElement("a");
    a.href = buch.link;
    a.innerText = "Link zur Buchbesprechung";
    link.appendChild(a);
    container.appendChild(link);

    regal2.appendChild(container); // Container unter den vorhandenen Inhalt hängen
}

// replaceChild 
// aus der Liste ul class?"target" in der die Vase images SVGAnimatedNumber, soll ein Child ersetzt 
// der querySelector erfasst Elemente in diesem beispiel anhand eines Attribut Selektors.

const imgages = document.querySelectorAll("img");       // Alle Bilder im DOM
const old1 = Array.from(imgages).find(img => img.alt.includes("Steingutvase"));  // sucht nach dem String

if (old1) {
    console.log("Gefundenes Bild:", old1);
} else {
    console.log("Kein Bild mit 'Steingutvase' im alt-Attribut gefunden.");
}


const old = document.querySelector("img[alt=Steingutvase]");

const newImage = document.createElement("img");
newImage.src = "images/vase-03.jpg";
newImage.alt = "Cracked Porzellan";
const fragment = old.parentElement.replaceChild(newImage, old); // altes bild wird durch neues ersetzt



// wenn man möchte kann man das entfernte fragment an anderer stelle erneut einfügen

{
    
let elem = document.querySelector("section");
if (!elem) {
    // Tu was wenn elem nicht da
    // Element existiert nicht → erstellen
    elem = document.createElement("section");
    document.body.appendChild(elem); 
    console.log("Kein Element gefunden. Neues Element erstellt!");
} else {
    // tu was mit elem    
    console.log("Element gefunden!");
    document.appendChild(fragment); 
    console.log("Fragment eingefügt!");

}

}

const parent2 = newImage.parentElement;
    if (parent2) {
        parent2.removeChild(newImage);
        console.log("Neues Bild wieder entfernt!");
    
} else {
    console.log("Kein Bild gefunden.");
}

//remove()
newImage.remove(); // entfernt newImage direkt aus dem DOM
console.log(`Das element ${newImage.src} wurde entfernt!`);



// replace with
const galerie = document.querySelector(`a[href="galerie"]`);
if (galerie) {
    const link3 = document.createElement("a");
    link3.href = "neu";
    link3.innerText = "Neue Galerie";
    galerie.replaceWith(link3);
    console.log("Link ersetzt!");
} else {
    console.log("Kein Link gefunden!");
}
// etwas mit outerHTML ersetzen

const figure = document.querySelector(".card figure" );
figure.outerHTML =
    `<figure class="ersatz">
        <img src="images/imac-on-white.jpg"
        width="2300" height="1644" alt="camera-on-blue" />
    <figcaption>Tausche Computer gegen Kamera</figcaption>
    </figure>`;