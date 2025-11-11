/* a) Erstelle ein Array mit Namen gemischteListe, das verschiedene Datentypen enthält 
(mindestens ein String, eine Zahl, ein Boolean, ein Objekt mit mindestens zwei Eigenschaften, 
ein Array mit mindestens zwei Elementen und eine Funktion, die eine einfache Ausgabe in die Konsole macht). 

b) Füge dem Array gemischteListe zwei weitere Elemente hinzu: Ein weiteres Objekt und ein Datum-Objekt mit dem aktuellen Datum. 

c) Durchlaufe das Array gemischteListe mit einer Schleife deiner Wahl 
und gib für jedes Element den Typ (mittels typeof oder einer anderen Methode, wenn nötig) in der Konsole aus. 

d) Verwende die if-else oder switch Kontrollstruktur, um für jedes Element im Array eine spezielle Nachricht in der Konsole auszugeben, 
basierend auf dem Typ des Elements (z.B. "Dies ist ein String: [Wert des Strings]"). 

e) Entferne das letzte und das erste Element aus dem Array gemischteListe 
und gib das veränderte Array in der Konsole aus. 

f) Erstelle eine Funktion, die ein Array als Parameter akzeptiert 
und die Länge des Arrays sowie die Elemente in umgekehrter Reihenfolge in der Konsole ausgibt. 

g) Nutze diese Funktion, um das Array gemischteListe zu bearbeiten und das Ergebnis auszugeben.   */

//a)
const gemischteListe = [
    { city: "Hamburg", bl: "Hamburg", einwohner: 1862565 }, // Objekt
    "Das Tor zurwelt",  //String
    2025,   //Zahl
    rainy = true, //boolean
    ["Mehr Brücken als", "Venedig"],    //array
    function(){
        console.log("Hamburg ist die zweitgrößte Stadt Deutschlands!");
        return;
    } //Funktion

];
//b)
const zeit = new Date().toLocaleDateString();
console.log(zeit);
gemischteListe.push(zeit);

const obj2 = gemischteListe.push({
    fakt1: "Die Elbphilharmonie ist schön, war aber teuer!",
    fakt2: "Die Elbphilharmonie ist weltbekannt!"
});
console.log(gemischteListe);
//c)
const l = gemischteListe.length;
for (let i = 0; i<l; i++){
    console.log(`${gemischteListe[i]}, hat den Typ " ${typeof gemischteListe[i]}"`);
}
// d)

// typeof ist ein Operator, der Datentypen wie string, number, boolean, function erkennt
// Arrays sind aber Objekte, deshalb braucht man die separate Funktion Array.isArray()
for (let i = 0; i<l; i++){
    if (Array.isArray(gemischteListe[i])){      // es eteht ganz oben, da die arrays sonst als objekte ausgegeben werden.
        console.log("Dies ist ein Datentyp array:", gemischteListe[i]);
    } else {
    if (typeof gemischteListe[i] === "string"){
        console.log("Dies ist ein Datentyp String:", gemischteListe[i]);
     } else {
    if (typeof gemischteListe[i] === "boolean"){
        console.log("Dies ist ein Datentyp boolean:", gemischteListe[i]);
     } else
    if (typeof gemischteListe[i] === "number"){
        console.log("Dies ist ein Datentyp number:", gemischteListe[i]);
     } else
    if (typeof gemischteListe[i] === "function"){
        console.log("Dies ist ein Datentyp function:", gemischteListe[i]);
     } else 
    if (typeof gemischteListe[i] === "object"){
        console.log("Dies ist ein Datentyp object:", gemischteListe[i]);       
    }
}
}
}

// e) Entferne das letzte und das erste Element aus dem Array gemischteListe 
// und gib das veränderte Array in der Konsole aus.
// array.pop() - entfernt letzten eintrag und gibt ihn aus
// array.shift() - Erstes Element Löschen


const letztes = gemischteListe.pop(); // entfernt letzten eintrag und gibt ihn aus
console.log("Entferntes letztes Element:", letztes);
const erstes = gemischteListe.shift(); // Erstes Element Löschen
console.log("Entferntes erstes  Element:", erstes);

console.log("Array nach Entfernen von erstem und letztem Element:");
for (let i = 0; i < gemischteListe.length; i++) {
    console.log(gemischteListe[i]);
}

// f)Erstelle eine Funktion, die ein Array als Parameter akzeptiert 
// und die Länge des Arrays sowie die Elemente in umgekehrter Reihenfolge in der Konsole ausgibt. 

const testArray = [1,2,3,4,5];
const x = function(arr){
        console.log(`Die Länge des Arrays ist ${arr.length}
            Das Array in umhgekehrter Reihenfolge ist ${arr.reverse()}`);

 }
 x(testArray);

 //g) Nutze diese Funktion, um das Array gemischteListe zu bearbeiten und das Ergebnis auszugeben.
 x(gemischteListe);
