const kinofilm = {
    title:     "Der Herr der Ringe",
    actor:      "Cate Blanchett",
    published:  2001,
    "Erster Teil":  "Die Gefährten",
    buch:           {
        title:      "Der Herr der Ringe",
        author:     "JRR Tolkien"
    },
    play:       function(){
        console.log(`Der Film "${this.title}" entstand nach dem Buch "${this.buch.title}" von "${this.buch.author}".`);
    }
}

// Eigenschaft aus Objekt löschen

delete kinofilm.published;
// Eigenschaft hinzufügen
kinofilm.hasOscae = true;
// Eigenschaft ändern

kinofilm.title = kinofilm.title + " Teil 1";

console.log(kinofilm)
kinofilm.play();


// for-in Schleife

const imgObj = {
    src:    "/media/image.jpg",
    width:  1060,
    height: 720,
    alt: "Ein Bild"
}

for (const key in imgObj){
    console.log("Object key", key); // gibt die Schlüssel des Objekts aus Object key src, key width, key height, key alt
}

for (const key in imgObj){
    console.log("Object value", imgObj[key]);
}

// for..in in arrays

const imgArr = [1060, 1280, 1440, 1980];
for (const key in imgArr){
    console.log(`${key}, ${imgArr[key]}`);
}

// Document Object Model
const head = document.head;
const body = document.body;
console.log(head)

const images = document.images; // sammelt alle images der webseite

const result = document.createElement("div");   // methode des DOM, erzeugt ein HTML-Element div
body.append(result)    // fügt das Objekt result als letztes element in das body Objekt ein

    for (let i = 0; i<images.length; i++){          // diese Schleife fügt in das result object an jedes Zeilenende ein <br>
        result.innerHTML += images[i].src + "<br>";
    }


console.log(body)
// Konstruktor Funktionen

function Produkt(kategorie, name, bild, showImage) {     // definiert die Konstruktorfunktion
    this.kategorie = kategorie;                         // legt fest, dass jedes Objekt eine eigenschaft kategorie bekommt
    this.name = name;
    this.bild=bild
    this.showImage = function(){                        //fügt jedem Objekt eine eigene Methode hunzu
        console.log(`img src="${this.bild}"
        alt="${this.name}">`);
    }
}

// Erst das erzeugen mit dem Schlüsselwort new vor dem aufruf der Konstruktor Funktion weist den eigenschaften den Wert zu.

const p1 = new Produkt("Haushalt",
"Bürste Minimale",
"product-01.jpg");
const p2 = new Produkt("Elektronik", "Föhn","product-01.jpg");
p1.showImage(); // soll dies ausgeben: <img src="product-01.jpg" alt="Bürste Mini"> aus
console.log(p2);
console.log(Produkt)

console.log(Object.getPrototypeOf(p1));

// Klassen
class Cake {
    constructor(flavor, time, deco, eggs){
        this.flavor = flavor;
        this.time = time;
        this.deco = deco;
        this.eggs = eggs;
    }
    cakeRecipe(){
        return `Dieser Cupcake wird mit ${this.flavor} und
    ${this.eggs} Eiern zubereitet, 
    ${this.time} min gebacken und
     mit ${this.deco} serviert.`;
    }
}

const schoko = new Cake("Schokostreussel", 15, "Sahne", 4);
console.log(schoko.cakeRecipe());
const mohn = new Cake("Mohn", 10, "Haselnüsse", 3);
console.log(mohn.cakeRecipe());
const quark = new Cake("Quark", 20, "Beeren", 2);
console.log(quark.cakeRecipe());



// Date Objekt

const heute = new Date();
console.log(heute);
const dateGestern = new Date(2024,0,1,1,12,55,123);
console.log(dateGestern);

const meeting = new Date().toLocaleString();
console.log("Meeting", meeting);        //Meeting 5.11.2025, 14:19:50
const weekS = new Date().toLocaleString("de-DE", {weekday: "short"});
const monthS = new Date().toLocaleString("de-DE", {month: "short"});

let d = new Date();
console.log(d);     //Wed Nov 05 2025 14:30:37 GMT+0100 (Mitteleuropäische Normalzeit)
d=new Date().toISOString();
console.log(d);     //2025-11-05T13:30:37.610Z
d=new Date().toLocaleDateString();
console.log(d);     //5.11.2025
d=new Date().toUTCString();
console.log(d);     //Wed, 05 Nov 2025 13:30:37 GMT
d=new Date().getTimezoneOffset();   
console.log(d);     //-60


let termin = new Date();

termin.getMonth();
termin.getFullYear();
termin.getDate();
termin.getDay(); // Wochentag startet am Sonntag mit 0
termin.getHours();
termin.getMinutes();
termin.getSeconds();

const full = new Date(document.querySelector("time").getAttribute("datetime"));
 // =`${weekS}, den ${full.getDate()}.${monthS}, ${full.getFullYear()}`;



const formatter = new Intl.DateTimeFormat("de-DE", {
  timeZoneName: "long"
});

const timezone = formatter.resolvedOptions().timeZone;

console.log("Aktuelle Zeitzone:", timezone); // Aktuelle Zeitzone: Europe/Budapest


const jetzt = Date.now();
console.log (jetzt); // 1762351635290 Millisekunden seit dem 1.1.1970
const timestampToDate = new Date(jetzt);
console.log(timestampToDate);

// Math.floor verwandelt die Millisekunden in Sekungen, Stunden oder Jahre.

const jahre = Math.floor(jetzt / (1000*60*60*24*365));
console.log(jahre); // 55 Jahre seit dem 1.1.1970

const von = 1762351635290;
const bis = 1762351848168;
const zeit = (bis-von)/1000 +" sek"; 
console.log(zeit) //212.878 sek


// Übung 7.7 Date und time
/* Auf welchen Wochentag fällt der 24. Dezember 2024? Und welcher Wochentag
war am 1.1.1970? */


// Und welcher Wochentag war am 1.1.1970? -> Donnerstag!
const tage = Math.floor(jetzt / (1000*60*60 * 24)) 
console.log(tage); // 20397
console.log(tage%7); // 6, also 6 tage zurücl von heute? heute ist Mittwoch, also war dies ein Donnerstag!

const weihnachten2024 = new Date(2024,11,24);
console.log(weihnachten2024); // Tue Dec 24 2024 00:00:00 GMT+0100 (Mitteleuropäische Normalzeit) 
// es war offenbar ein Dienstag.
const wochentag = weihnachten2024.getDay();
console.log(wochentag); 

const tag1 = new Date(1970, 0,1)
console.log(tag1);





