const books = `[{"author": "austen","firstname": "Jane","books": [{"title": "Mansfield Park", "published": 1814},{"title": "Stolz und Vorurteil", "published": 1813},{"title": "Emma", "published": 1816}]}, {"author": "Pratchett","firstname": "Terry","books": [{"title": "Total verhext", "published": 1991},{"title": "Lords and Ladys", "published": 1992},{"title": "Ruhig Blut", "published": 1996}]}]`;
const booksParsed = JSON.parse(books);
console.log(booksParsed);

console.log(booksParsed[1].author);
console.log(`${booksParsed[1].firstname} ${booksParsed[1].author}`);

const color = {
    number : 120,
    lightness : 73,
    saturation : 75,
    name : "lightgreen",
    description: "Helles Grün",
    kombi : function (elem) {
        elem.style = `background:   hsl(${this.number},
                                    ${this.saturation}%,
                                    ${this. lightness}%)`;
        }
    }


const myObjectString = JSON.stringify(color);
console. log("myObjectString", myObjectString);

// der nächste Schritt ist wichtig, z. B. wenn ich mein Objekt an eine Web-API per GET-Parameter übergeben will.
// const url = "https://example.com/api?data=" + encodeURIComponent(myObjectString);


console. log(encodeURIComponent(myObjectString)); // ersetzt Sonderzeichen (wie {, ", :, ,, ä, Leerzeichen usw.) durch Prozent-Kodierungen
// output:%7B%22number%22%3A120%2C%22lightness%22%3A73%
// %3A75%2C%22name%22%3A%22lightgreen%22%2C%22description%22%3A%22Helles%20Gr%C3%BCn%22%7D

// um es wieder lesbar zu machen kann man decodeURIComponent nutzen.
// dies ergibt dann wieder einen JSON String, den ich mit  JSON.parse(...) wieder in ein Objekt umwandeln kann.



// Uebung Objekte / JSON
// 1. lege blogListe wie beschrieben an

const blogListe = 
[{
    titel:  "titel1", 
    autor:  "Max",
    status: {veröffentlicht:false, entwurf : true, gelöscht: false}
},
{
    titel:  "titel2", 
    autor:  "Foo",
    status: {veröffentlicht:false, entwurf : true, gelöscht: false}
},
{
    titel:  "titel3", 
    autor:  "Bar",
    status: {veröffentlicht:false, entwurf : true, gelöscht: false}
}]
console.log(blogListe);
console.log(blogListe[1].autor);           // "Foo"
console.log(blogListe[2].status.entwurf);  // true´

// 2. setze mit dot-notation die Werte von veröffentlicht für alle drei Posts auf true und denjeweiligen Wert von entwurf auf false
for (i = 0; i<3; i++){
    blogListe[i].status.veröffentlicht = true
    blogListe[i].status.entwurf = false
}
console.log(blogListe[2].status.veröffentlicht);

// 3. Destrukturiere den Titel des Blogbeitrags und nenne die Variable post2
// const <DestructuringPattern> = <Value>;
const [{titel:post1}, {titel:post2}, {titel:post3}] = blogListe;
for (i = 0; i<3; i++){
console.log(blogListe[i].titel); 
}

//4. wandle es mit stringify um
console.log(JSON.stringify(blogListe)); // [{"titel":"titel1","autor":"Max","status":{"veröffentlicht":true,"entwurf":false,"gelöscht":false}},{"titel":"titel2","autor":"Foo","status":{"veröffentlicht":true,"entwurf":false,"gelöscht":false}},{"titel":"titel3","autor":"Bar","status":{"veröffentlicht":true,"entwurf":false,"gelöscht":false}}]

