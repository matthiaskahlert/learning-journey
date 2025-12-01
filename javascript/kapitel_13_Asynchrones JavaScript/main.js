setTimeout(function() {
    const t = new Date();
    console.log(
        "Timeout",
        `${t.getHours()}:${t.getMinutes()}:${t.getSeconds()}`
    );
}, 5000);

const t = new Date();
console.log(
    "Im globalen Bereich",
    `${t.getHours()}:${t.getMinutes()}:${t.getSeconds()}`
);

// countdown beispiel
const countStart = document.querySelector("#countStart");
const countCancel = document.querySelector("#countCancel");

const start = 10;
document.querySelector(".circle").textContent = 10;

let timer; // globale Timer-Variable

function countdown(time, hue) {
    document.querySelector(".circle").textContent = time;
    document.querySelector(".circle").setAttribute(
        "style",
        `border-color: hsl(${hue},85%,60%); color: hsl(${hue},85%,60%)`
    );

    time -= 1;
    hue += 60;

    if (time >= 0) {
        timer = setTimeout(countdown, 1000, time, hue); // Timer global speichern
    }
}

countStart.addEventListener("click", function() {
    countdown(start, 30);
});

countCancel.addEventListener("click", function() {
    clearTimeout(timer);
});

// beispiel für requestAnimationFrame()
const animationCircle = document.querySelector(".animationCircle");
let pos = 0; // Startposition

function animate(timestamp) {
    pos += 2; // Geschwindigkeit: 2px pro Frame
    animationCircle.style.left = pos + "px";

    if (pos < window.innerWidth - 50) {
        requestAnimationFrame(animate); // nächsten Frame anfordern
    }
}

// Animation starten
requestAnimationFrame(animate);

// openthesaurus API anfrage
const button = document.querySelector("#btn");

button.addEventListener("click", function() {
    document.querySelector("#alt").innerHTML = ""; // leert die Ergebnisliste
    const thesaurus = document.querySelector("#thesaurus"); // liest das eingabefeld aus
    const word = encodeURI(thesaurus.value); // macht den eingegebenen Text URL -sicher
    const xhr = new XMLHttpRequest(); // Neues XMLHttpRequest-Objekt erzeugen

    const url = `https://www.openthesaurus.de/synonyme/search?q=${word}&format=application/json`;
    xhr.open("GET", url); // Request vorbereiten: GET-Methode, URL
    xhr.onreadystatechange = function() { // Event-Handler, der auf Änderungen des Request-Status reagiert
        if (this.readyState === 4 && this.status == 200) { // Prüfen, ob die Anfrage fertig ist (readyState === 4) und erfolgreich (status == 200)
            const data = JSON.parse(this.responseText); // Antwort vom Server als JSON parsen
            console.log("data", data);
            resolve(data);  // Funktion aufrufen, um die Synonyme in die Seite einzufügen
        }
    };
    xhr.send(); // Anfrage abschicken
});

function resolve(data) { // Funktion, die die erhaltenen Synonyme in die Seite einfügt
    data.synsets.forEach(item => { // Durch alle Synset-Gruppen iterieren
      // Synsets sind thematisch oder bedeutungsmäßig zusammengehörige Wortgruppen, die als Einheit von OpenThesaurus zurückgegeben werden
        item.terms.forEach(e => {
            const li = document.createElement("li");
            li.textContent = e.term;
            document.querySelector("#alt").append(li); // Listenelement in die Ergebnisliste (#alt) einfügen
        });
    });
}

/* Kurze Zusammenfassung der Schritte:

1. Klick auf Button → Event wird ausgelöst.
2. Eingabefeld auslesen und URL-encode durchführen.
3. XMLHttpRequest erzeugen, URL öffnen, Event-Handler setzen.
4. Anfrage absenden (xhr.send()).
5. Wenn Antwort kommt (readyState 4 + status 200), JSON parsen.
6. Synonyme aus den Daten extrahieren und als <li> in die Seite einfügen. */


// beispiel mit fetch:
fetch(`https://www.openthesaurus.de/synonyme/search?q=Programmierung&format=application/json`)
.then ((response) => { return response.json() })
.then ((data) =>{ console.log(data)});


// REST API Beispiel

const button1 = document.querySelector("#loadPosts");
const list = document.querySelector("#postList");

button1.addEventListener("click", function() {
  list.innerHTML = ""; // alte Inhalte löschen
  fetch("https://wordpress.org/news/wp-json/wp/v2/posts")
    .then(response => response.json()) // JSON auslesen
    .then(posts => { // posts ist jetzt das Array
      posts.forEach(post => {
        const li = document.createElement("li");
        li.textContent = post.title.rendered; // nur den Titel
        list.appendChild(li);
      });
    })
    .catch(error => console.error("Fehler beim Laden:", error));
});

/* Erklärung der Schritte:

Klick auf den Button → Event-Listener wird ausgelöst.

Liste leeren, damit alte Einträge verschwinden.

fetch() ruft die REST-API auf.

.then(response => response.json()) wandelt die Antwort in ein JS-Objekt/Array um.

.then(posts => …) iteriert über das Array der Posts.

Für jeden Post wird ein <li> erzeugt und in die Liste eingefügt.

.catch() fängt Fehler ab, z. B. Netzwerkprobleme. */

// beispiel JSON-fetch von dummyjson.com
// prüfen welche daten verfügbar sind und eins davon näher betrachten

const selection = document.querySelector("#products");
const output = document.querySelector("#output");

function fetchProducts (){
  fetch("https://dummyjson.com/products/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      console.log(data.products[15]);
      generateOptions(data.products);
  return data.products;
})
.then ((products) => {
showProduct(products [1]);
selection.addEventListener("change", (e) => {
const id = e.target.value;
showProduct(products [id-1]);

})
    })  
}
fetchProducts();
function showProduct(product) {
  output.innerHTML = `
    <h3>${product.title}</h3>
    <img src="${product.thumbnail}" alt="${product.title}" style="max-width:200px;">
    <p>${product.description}</p>
    <strong>Preis: ${product.price} €</strong>
  `;
}

function generateOptions(data) {
  data.forEach((item) => {
    const option = document.createElement("option");
    option.innerText = item.title;
    option.value = item.id;
    selection.append(option);
  });
}
