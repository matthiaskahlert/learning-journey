/* Erstelle ein JavaScript-Programm, das folgende Funktionen ausführt: 

a) Definiere ein Array gemischteElemente, das verschiedene Datentypen enthält 
(mindestens einen String, eine Zahl, ein Boolean, ein Objekt mit mindestens zwei Eigenschaften, 
eine Funktion, die eine einfache Berechnung durchführt, 
und ein weiteres Array mit mindestens drei Elementen). 

b) Füge dem Array gemischteElemente am Ende zwei neue Elemente hinzu: einen weiteren String und eine Zahl. 
Verwende dafür die Methode push(). 

c) Entferne das erste Element des Arrays und speichere es in einer Variablen erstesElement. 

d) Erstelle eine for-Schleife, die über das Array gemischteElemente iteriert und für jedes Element seinen Typ in der Konsole ausgibt. 

e) Definiere eine Funktion findeStrings, die das Array gemischteElemente durchläuft und alle Elemente, die Strings sind, in einem neuen Array sammelt und dieses zurückgibt. 

f) Erstelle ein Objekt person mit den Eigenschaften name, alter und einer Methode vorstellen, die eine Begrüßungsnachricht in der Konsole ausgibt, die den Namen und das Alter der Person enthält. 

g) Verwende eine for-in-Schleife, um alle Eigenschaften und Werte des Objekts person in der Konsole auszugeben.   */


const gemischteElemente = [
     

        2025,   //Zahl
        "Das Tor zurwelt",  //String
        true, //boolean
        {city: "Hamburg", bl: "Hamburg", einwohner: 1862565 }, // Objekt
        function(){
            console.log("Hamburg ist die zweitgrößte Stadt Deutschlands!");
            return;
        }, //Funktion
        ["Mehr Brücken als", "Venedig"]   //array

];
const arr2 = ["Hamburg ist", "eine grüne Stadt"];
const zahl = 2

gemischteElemente.push(arr2);
gemischteElemente.push(zahl);
erstesElement = gemischteElemente.shift();
console.log("Erstes Element", erstesElement);
for (let i = 0; i < gemischteElemente.length; i++) {
    let typ;
    
    if (Array.isArray(gemischteElemente[i])) {
        typ = "array"; // spezieller Typ für Arrays
    } else {
        typ = typeof gemischteElemente[i];
    }
    
    console.log(`${gemischteElemente[i]} hat den Typ "${typ}"`);
}
// ) Definiere eine Funktion findeStrings, die das Array gemischteElemente durchläuft 
// und alle Elemente, die Strings sind, in einem neuen Array sammelt und dieses zurückgibt. 
function findeStrings(arr){
    return arr.filter(function(element){
        return typeof element ==="string";
});
}
console.log(findeStrings(gemischteElemente));
//Erstelle ein Objekt person mit den Eigenschaften name, alter und einer Methode vorstellen, 
// die eine Begrüßungsnachricht in der Konsole ausgibt, die den Namen und das Alter der Person enthält. 

const person = {
name: "Max Mustermann", 
alter: 38, 
vorstellen:  function(){
    console.log(`Hallo, mein name ist ${this.name} und ich bin ${this.alter} Jahre alt.`)
    return;
}
}
person.vorstellen();

// g) Verwende eine for-in-Schleife, um alle Eigenschaften und Werte des Objekts person in der Konsole auszugeben.
for (const key in person) {
    console.log(`${key}, ${person[key]}`);
}