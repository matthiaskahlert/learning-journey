/* Erstelle ein JavaScript-Programm, das folgende Aufgaben in einer Datei löst: 

- [x] a) Deklariere eine Variable alter und weise ihr dein Alter zu. Verwende eine if-else-Struktur, um zu überprüfen, ob du volljährig bist. Gib eine entsprechende Nachricht in der Konsole aus. 

- [x] b) Verwende eine for-Schleife, um die Zahlen von 1 bis 10 zu durchlaufen. Multipliziere jede Zahl mit 2 und gib das Ergebnis in der Konsole aus. 

- [x] c) Erstelle eine Variable farben mit einem Array, das die Strings "Rot", "Grün" und "Blau" enthält. 
Verwende eine while-Schleife, um alle Farben in der Konsole auszugeben. 

- [x] d) Benutze den Ternary Operator, um zu überprüfen, ob die Zahl 7 größer als 5 ist. Gib "Ja, 7 ist größer als 5" oder "Nein, 7 ist nicht größer als 5" in der Konsole aus. 

- [x] e) Erstelle eine Variable wochentag und weise ihr einen Tag der Woche als String zu (z.B. "Montag"). 
Verwende eine switch-Anweisung, um zu überprüfen, ob es sich um einen Werktag oder ein Wochenende handelt. 
Gib eine entsprechende Nachricht in der Konsole aus. */

//a)
const alter = 45
if (alter >=18){
    console.log(`Nutzer ist volljährig, das alter ${alter} Jahre liegt über dem alter von 18 Jahren!`)
} else {
    console.log(`Nutzer ist nicht volljährig, das alter ${alter} Jahre liegt unter dem alter von 18 Jahren!`)
}
//b)
for (let i = 0; i<= 10; i++) {
    zahl = i * 2
    console.log(zahl);
}

//c)
{ // blockScope für i
let i = 0
const farben = ["Rot", "Grün", "Blau"]

while (i<farben.length){
console.log(`${i+1}. Farbe: ${farben[i]}`)
i++;
}

}

//d)
const zahl1 = 7
const zahl2 = 5
const foo = (zahl1 > zahl2) ? console.log("Ja, 7 ist größer als 5") : console.log("Nein, 7 ist nicht größer als 5");

//d)
const wochentag = "Dienstag";
const tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]

switch(true) { 
    case (tage.includes(wochentag)): 
        
        console.log(`${wochentag} ist ein Werktag!`);
        break;

     default:
        console.log(`Kein Werktag.`);
        
    }
