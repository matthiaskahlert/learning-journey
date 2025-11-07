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
