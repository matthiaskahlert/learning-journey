const arr = [123,1234,465,27635];
const arr2 = ["Foo", 234, arr, "bar", true];

const stoff = new Array("Leinen", "Baumwolle", "Seide");
// zugriff auf den ersten indes vom array stoff
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