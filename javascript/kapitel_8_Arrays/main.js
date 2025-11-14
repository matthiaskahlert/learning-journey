const arr = [123,1234,465,27635];
const arr2 = ["Foo", 234, arr, "bar", true];

const stoff = new Array("Leinen", "Baumwolle", "Seide");
// zugriff auf den ersten index vom array stoff
const wahl = `Ich bevorzuge ${stoff[1]} für T-shirts`;
console.log("wahl: ", wahl); //wahl:  Ich bevorzuge Baumwolle für T-shirts
console.log(stoff.length); //3
// stoff.length zeigt mir nicht nur die anzahl der elemente (3) sondern auch den letzten Index nach dem letzten Element, da der index bei 0 beginnt.
stoff[3] = "Samt" // setzt es ans ende des Arrays, während stoff[2] = "Samt" den index von 2 überschreiben würde.
console.log("Stoff:", stoff);
console.log(Object.getPrototypeOf(stoff))

/* 
at()
concat()
Array()
copyWithin()
entries()
every()
fill()
filter()
find()
findIndex()
findLast()
findLastIndex()
flat()
flatMap()
forEach()
includes()
indexOf()
join()
keys()
lastIndexOf()
length
map()
pop()
push()
reduce()
educeRight()
reverse()
hift()
slice()
some()
sort()
splice()
toLocaleString()
toReversed()
toSorted()
toSpliced()
toString()
unshift()
values()
with()
values()
Symbol(Symbol.unscopables)
*/

const stoffLen = stoff.push("Viskose", "Jeans");
console.log("Stoff:", stoff);

const alt = stoff.pop(); //gibt das entfernte Element aus.
console.log("Aus stoff entfernt:",alt,"Neues array:", stoff);

console.log(arr);

arr.unshift(3);
console.log(arr);

const teilArray = stoff.slice(1,2);
console.log(teilArray);

console.log("Stoff:", stoff);
const umkehrStoff = stoff.reverse();
console.log("Umkehrstoff:", umkehrStoff);

if (stoff.includes("Seide")){
    console.log("Seide vorhanden");
} else{
    console.log("Keine Seide zur Hand");
}

const farben = ["grün", "blau", "rot", "gelb", "schwarz", "weiß"];
console.log(farben);
const str = farben.splice(2,5).reverse().toString();
console.log("str:", str);

const satz = ["Nutze", "den", "Tag!"];

console.log(satz.join(""));
console.log(satz.join("! "));
console.log(satz.join());
console.log(satz.toString());

// Destructure
const spieler = ["Schrödinger", 135, "Blau-Weiß", "Jever"];
const [name, punkte, ...rest] = spieler; // Hier bedeutet ...rest: Alle verbleibenden Elemente des Arrays kommen in eine neue Variable namens rest

console.log( "name", name);

console.log( "punkte", punkte);
console.log("rest", rest);
console.log("spieler", spieler)


// anderes destructure beispiel:

// Create an Object
const person = {
  firstName: "Max",
  lastName: "Mustermann",
  age: 50
};

// Destructuring
let {firstName, lastName, age: alter} = person;
console.log(alter) // 50


// Array.isArray()
const liste = [5,8,37, 45]
console.log("typeof person", typeof person); //object
console.log("person = Array?", Array.isArray(person)); // Array? false - denn person ist ein Objekt mit benannten Eigenschaften
console.log("typeof liste", typeof liste); //object
console.log("liste = Array?", Array.isArray(liste)); // Array? true - denn liste ist ein Array mit nummerierten Einträgen

console.log("spieler = Array?", Array.isArray(spieler)); // spieler = Array? true


// array.sort()

const sortier = ["Juwel", "über", "drei", "Ärger", 28, ".rose", "%"];
sortier.sort();
console.log("sortier ist", sortier);

const numerischesArray = [3,45,567456,34,13541345,6,468,2,234];
numerischesArray.sort();
console.log(numerischesArray); // [13541345, 2, 234, 3, 34, 45, 468, 567456, 6]
numerischesArray.sort((a,b) => a-b);
console.log((numerischesArray)); // [2, 3, 6, 34, 45, 234, 468, 567456, 13541345]

/* const numerischesArray = [3, 45, 567456, 34, 13541345, 6, 468, 2, 234];

let vergleichsZaehler = 0;

numerischesArray.sort((a, b) => {
  vergleichsZaehler++;
  return a - b;
});

console.log("Sortiertes Array:", numerischesArray);
console.log("Anzahl der Vergleichsschritte:", vergleichsZaehler); */

const sortiert = ['%', '.rose', 28, 'Juwel', 'drei', 'Ärger', 'über']
const namen = ["Edda", "Kjell", "Matze"]
sortiert.push(namen);
console.log(sortiert);

console.log(sortiert[7][2]); //Matze

const blumen = ["Rosen", "Vergissmeinicht"];
const pflanzen = ["Gänseblümchen", "Löwenzahn"];
const newArr = [blumen,pflanzen];
console.log(newArr);
console.log(newArr[1][1]); // Löwenzahn

//aneinanderreihing mit array.concat()
let x = blumen.concat(pflanzen);
console.log(x); // ['Rosen', 'Vergissmeinicht', 'Gänseblümchen', 'Löwenzahn']
let y =[...blumen, ...pflanzen];
console.log(y);

// mit spread funktionsagrumente füttern
function addiere (a,b,c){
    return a+b+c;
}
const zahlen = [3,4,5];

const ergebnis = addiere(...zahlen); // entspricht addiere(2, 5, 7)
console.log(ergebnis); // 12



// array.flat()
const arr4 = [100,86[17,200,3], [0,14], 200];
const newArr4 = arr4.flat(2);
console.log(newArr4);


/* Erstelle eine JavaScript-Funktion verwalteFilmSammlung, die ein Array von Filmobjekten verwaltet. 
Jedes Filmobjekt soll folgende Eigenschaften haben: titel, jahr, genre, bewertung. 
Die Funktion soll folgende Funktionalitäten bieten: 

a) Hinzufügen eines neuen Films. 

b) Aktualisieren der Bewertung eines Films durch den Titel. 

c) Löschen eines Films durch den Titel. 

d) Anzeigen aller Filme in der Konsole, sortiert nach dem Jahr der Veröffentlichung. 

e) Suchen eines Films durch den Titel und Anzeigen der Details in der Konsole. 

Verwende dabei Kontrollstrukturen, Schleifen, Bedingungen, und Objektmanipulationen, die du kennst. 
Nutze die Konsole zur Ausgabe von Informationen.  */
//a)  Hinzufügen eines neuen Films.
function verwalteFilmSammlung(){
    const filmSammlung = [];
    return {
        hinzufuegen: function(titel, jahr, genre, bewertung){
            const neuerFilm = {titel, jahr, genre, bewertung};  
            filmSammlung.push(neuerFilm);
            console.log(`Film "${titel}" hinzugefügt.`);
        },
        aktualisieren: function(titel, neueBewertung){
            const film = filmSammlung.find(f => f.titel === titel);   
            if(film){
                film.bewertung = neueBewertung;
                console.log(`Bewertung von "${titel}" aktualisiert auf ${neueBewertung}.`);
            } else {
                console.log(`Film "${titel}" nicht gefunden.`);
            }
        },
        loeschen: function(titel){
            const index = filmSammlung.findIndex(f => f.titel === titel);   
            if(index !== -1){
                filmSammlung.splice(index, 1);
                console.log(`Film "${titel}" gelöscht.`);
            } else {
                console.log(`Film "${titel}" nicht gefunden.`);
            } 
        },
        anzeigenAlle: function(){
            const sortierteFilme = [...filmSammlung].sort((a, b) => a.jahr - b.jahr); 
            console.log("Filme in der Sammlung:");
            sortierteFilme.forEach(film => {
                console.log(`${film.titel} (${film.jahr}) - Genre: ${film.genre}, Bewertung: ${film.bewertung}`);
            });
        },
        suchen: function(titel){
            const film = filmSammlung.find(f => f.titel === titel);
            if(film){
                console.log(`Details zu "${titel}": Jahr: ${film.jahr}, Genre: ${film.genre}, Bewertung: ${film.bewertung}`);
            } else {
                console.log(`Film "${titel}" nicht gefunden.`);
            }
        }
    };
} 
const meineFilme = verwalteFilmSammlung();
meineFilme.hinzufuegen("Inception", 2010, "Sci-Fi", 8.8);
meineFilme.hinzufuegen("The Matrix", 1999, "Action", 8.7);  
meineFilme.anzeigenAlle();
meineFilme.aktualisieren("Inception", 9.0); 
meineFilme.suchen("Inception"); 
meineFilme.loeschen("The Matrix"); 
meineFilme.anzeigenAlle();

{ // blockscope für Übung

const arr = ["Kirschen", "Pfirsiche", "Erdbeeren"];
const l = arr.length;
for (let i= 0; i<l; i++){
    console.log(arr[i]);
// for..of schleife
const lektion = ["Mathe", "Deutsch", "Physik", "Sport"];
for (const item of lektion){
    console.log(item);
}
}
const json = [
    {"author": "Austen, Jane", "book": "Mansfield Park"},
    {"author": "Pratchet, Terry", "book": "Total verhext"},
    {"author": "Arnim, Elizabth", "book": "Verzauberter April"}
];
for (const elem of json){
    console.log(`${elem.book} ist von ${elem.author}`);
    
}
const city = ["Amsterdam", "Berlin", "Göttingen", "Bielefeld", "Hannover"];
    for (const elem of city){
        console.log(elem);
      if (elem === "Göttingen"){
        console.log(`Bis hierhin und nicht weiter, ${city[3]} existiert nicht xD`);
        break;
    } 
}
}
// for..of mit Index: entries()
// arr.entries() verleiht der äußeren Schleife einen index, in der inneren Schleife ist key der index.
{ // block-scope
    const arr = [[128, 156],[32,33],[200,400]];
for (const [index, elem] of arr.entries()){ // [index, elem] ist destructure und teilt die werte den variablen zu
    console.log(`${index} . ${elem}`);      // output äußere Schleife 
    for (const [idx, item] of elem.entries() ){ // [idx, item] ist destructure, und speichert die Werte in den variablen idx und item
        console.log(`${index}.${idx}:${item}`); // output innere Schleife
    }
}

/* 
0 . 128,156     // arr.entries(); liefert einen Iterator der hier ausgepackt wird. index 0 und elem ist hier [128,156]
0.0:128             // index 0, idx 0, item 128
0.1:156             // index 0, idx 1, item 156
1 . 32,33       // arr.entries(); liefert einen Iterator der hier ausgepackt wird. index 1 und elem ist hier [32,33]
1.0:32              // index 1, idx 0, item 32
1.1:33              // index 1, idx 1, item 33
2 . 200,400     // arr.entries(); liefert einen Iterator der hier ausgepackt wird. index 2 und elem ist hier [200,400]
2.0:200             // index 2, idx 0, item 200
2.1:400             // index 2, idx 1, item 400
*/

arr.forEach((elem) => { console.log(" mit forEach", elem)});

const score = [17, 129, 27, 8, 51, 99, 12];
    score.forEach((elem)=>{
        if (elem>50) {
            console.log(elem)}
        }
    );

const namen = ["Anna", "Ben", "Chris"];

namen.forEach((name, index) => {
  console.log(`${index}: Hallo, ${name}!`);
});

const images = ["tulpe.jpg","rose.jpg","veilchen.jpg","nelke.jpg"];
images.forEach((elem, index)=>{
        const tag = `<img src="${elem}">` ;
        console.log(`i:${index}`, tag);
    });
}
// mit forEach über Arrays von Objekten iterieren
const imagesObj = [
    {path: "flowers-01.webp", width: 170 },
    {path: "flowers-02.webp", width: 170 },
    {path: "flowers-06.webp", width: 170 },
    {path: "flowers-04.webp", width: 170 }
];
imagesObj.forEach((obj)=>console.log(obj.path)); 

// array.map()

const preise = [3,22,11,30];
const mwst = preise.map(number=>number*19/100);
console.log("mwst", mwst); // mwst (4) [0.57, 4.18, 2.09, 5.7]

// array.map) mit index      -  jeder zweite wert bekommt andere berechnung
const geschenkt = preise.map((number,i)=>{
    if (i % 2 === 0){
        return (number * 9.5 / 100);
    } else {
        return (number * 19 / 100);
    }

});
console.log("geschenkt",  geschenkt); // geschenkt (4) [0.285, 4.18, 1.045, 5.7]
{ // block scope
const product = [
    {name:"Waschmaschine", preis: 399.00, lager: 117},
    {name:"Kühlschrank", preis: 459.00, lager: 32},
    {name:"Backofen", preis: 244.50, lager: 98},
    {name:"Mixer", preis: 199.00, lager: 7},
    {name:"Grill", preis: 80.00, lager: 64}

];

const deal = product.map((item, idx) => {
    const obj = {};     
    // ein neues objekt wird erstellt, dass die gleichen werte wie ds ursprüngliche erhält, weil man das orginalobjekt nicht verändern möchte. 
    // der deal ist nur temporär, nun kann man den preis modifizieren ohne das array product ändern zu müssen.
    obj.name = item.name;
    obj.preis = item.preis;
    obj.lager = item.lager;

    if (idx === 0 || idx === 2){
        obj.preis = (item.preis - item.preis * 25 / 100).toFixed(2);
        return obj;
    }
    return obj;
});
console.log("deal", deal);
console.log(product.map(obj=>obj.name));

}

{
// gleiches beispiel mit spread operator:
const product = [
    {name:"Waschmaschine", preis: 399.00, lager: 117},
    {name:"Kühlschrank", preis: 459.00, lager: 32},
    {name:"Backofen", preis: 244.50, lager: 98},
    {name:"Mixer", preis: 199.00, lager: 7},
    {name:"Grill", preis: 80.00, lager: 64}

];
const deal = product.map((item, idx) => ({
    ...item, // kopiert alle Eigenschaften von item
    preis: (idx === 0 || idx === 2) 
        ? (item.preis - item.preis * 25 / 100).toFixed(2) 
        : item.preis
}));
console.log("deal", deal);

const city = ["Amsterdam", "Berlin", "Göttingen", "Bielefeld", "Hannover", "Bonn", "Köln"];
const kurz = city.filter((name)=> name.length < 5);
console.log("Werte des Arrays mit weniger als 5 Zeichen", kurz) //Werte des Arrays mit weniger als 5 Zeichen (2) ['Bonn', 'Köln']
const kurzMitForEach = [];
city.forEach((elem) => {
    if (elem.length > 5){
        kurzMitForEach.push(elem)
    }
});

console.log("Nun umgekehrt also alle mit mehr als 5 mit forEach:", kurzMitForEach)


}
{
const preise = [68.50, 70, 120, 12, 7];

const mwst = preise.map((preis)=>preis*19/100);
console.log(mwst)

const output = preise.map(function(preis){
    return preis.toFixed(2) + " €";
});
console.log("Output:", output); // Output: (5) ['68.50 €', '70.00 €', '120.00 €', '12.00 €', '7.00 €']

}
const result = [];
preise.forEach((preis) => {
    result.push(preis.toFixed(2) + " €");
});
console.log("map result", result);
{

const punkte = [25,9,100,400,900];
const calculus = punkte
    .map(function(p) {
        return Math.sqrt(p);
    })
    .map(function(sqrt) {
        return sqrt * 2;
    })
    console.log("calculus", calculus); //calculus (5) [10, 6, 20, 40, 60]

    }

    {
        
const preise = [75,120,127,25,90,7,18,210];
const rabatt = preise
    .filter((preis) => preis >= 100)
    .map((over)=> (over - (0.1 * over)).toFixed(2));
    console.log("rabatt", rabatt);
    }

    {
const arr = [1,2,3,4,5,6,7,8,9,10];
const initialValue = 0
const summe = arr.reduce((previousValue, currentValue) =>
    previousValue + currentValue, initialValue
    );
console.log("summe", summe);

const summe2 = arr.reduce((prev, curr) =>
    prev + curr, 15
);
console.log("summe mit initialValue = 15", summe2);

}
{
    const produkte = [
    {"art": "Buch", "no":1724, "preis":"3.75", "lager":27},
    {"art": "Kalender", "no":475, "preis":"13.99", "lager":13},
    {"art": "Buch", "no":188, "preis":"14.05", "lager":28},
    {"art": "Spiel", "no":774, "preis":"22.99", "lager":4}
];

const buchwert = produkte
    .filter(function(obj){      // gibt bei jedem Schritt ein objekt zurück bei dem art ==="Buch" ist, also ein array mit zwei objekten
    if (obj.art === "Buch"){ // hier ginge alternativ auch return obj.art === "Buch";
        return obj;
    };
    }).map(function(obj){       // map berechnet den gesamtwert für jedes der beiden objekte
        return parseFloat(obj.preis) * obj.lager;
    }).reduce(function(prev, curr){ // reduce bildet die summe aus beiden werten
        return((parseFloat(prev) + parseFloat(curr)).toFixed(2))
    });
    console.log("buchwert", buchwert, typeof buchwert);
}



{
    const produkte = [
    {"art": "Buch", "no":1724, "preis":"3.75", "lager":27},
    {"art": "Kalender", "no":475, "preis":"13.99", "lager":13},
    {"art": "Buch", "no":188, "preis":"14.05", "lager":28},
    {"art": "Spiel", "no":774, "preis":"22.99", "lager":4}
];

const buchwert = produkte
    .filter(obj=>(obj.art ==="Buch"))
    .map(obj=>(parseFloat(obj.preis)*obj.lager))
    .reduce((prev,curr)=>((prev+curr).toFixed(2)));
    console.log("buchwert über arrow-function", buchwert, typeof buchwert);
}

{
    // Übung 8.7
const cities = [
	{ city: "Köln", bl: "Nordrhein-Westfalen", einwohner: 1000000 },
	{ city: "Quedlinburg", bl: "Sachsen-Anhalt", einwohner:  21500 },
	{ city: "Hannover", bl: "Niedersachsen", einwohner: 532000 },
	{ city: "Kiel", bl: "Schleswig-Holstein", einwohner: 249000 },
	{ city: "Frankfurt", bl: "Hessen", einwohner: 760000 },
	{ city: "Aachen", bl: "Nordrhein-Westfalen", einwohner:  250000 },
	{ city: "Darmstadt", bl: "Hessen", einwohner:  164000 },
	{ city: "Husum", bl: "Schleswig-Holstein", einwohner:  24000 },
	{ city: "Lübeck", bl: "Schleswig-Holstein", einwohner:  218000 },
	{ city: "Göttingen", bl: "Niedersachsen", einwohner:  119000 },
];
// Erzeuge ein neues Array von Objekten, in denen nur Städte aus Schleswig-Holstein und Hessen liegen.
const staedte = cities  
    .filter(obj=>(obj.bl==="Schleswig-Holstein" || obj.bl==="Hessen" ))
    console.log(staedte);

const einwohner = cities
    .filter(obj=>(obj.einwohner<200000 && obj.bl!=="Nordrhein-Westfalen"))
    console.log(einwohner);

// sparse arrays
const arr1 = [1,,3];
console.log(arr1[1]); // undefined

arr1[100]=200.96
console.log("arr1 mit Index100",arr1);
for (let i = 0; i<arr1.length; i++) {
    console.log (i, arr1[i]*19/100 + " ");
}
arr1.forEach((elem,index) => {
    console.log(index, elem * 19 / 100);
});
} 
