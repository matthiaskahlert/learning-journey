const menu = document.getElementById("menu"); // document.getElementById() ist eine DOM-Methode, mit der ich ein bestimmtes HTML-Element über seinen eindeutigen id-Wert auswähl
// alles zwischen den backticks wird in das nav Element geschrieben    
menu.innerHTML = ` 
    <u1>
        <li><a href="page1">Seite 1</a></li>
        <li><a href="page1">Seite 2</a></li>
    </u1>`;

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
    

    regal.style.color = "#4A884D";
    regal.style.backgroundColor = "lavender";
    regal.style.backgroundImage = "url('images/flowers-01.webp')";
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
const link = document.querySelector("nav li a[href='cd.html']"); // hier wird direkt das <a>-Element mit dem href="cd.html" ausgewählt!
link.innerText = "Css Datei" ;

console.log("link", link);


const elem2 = document.querySelector(".selector");
console.log("elem", elem2);

const listElems = document.querySelectorAll(".list li"); // finde alle <li> in einem Element mit class="list"
console.log("listElems", listElems);

listElems.forEach( item => console.log(item.innerText));
console.log("listElems[2]", listElems[2].innerText); // listElems[2] Der Herr der Ringe Zum Warenkorb
