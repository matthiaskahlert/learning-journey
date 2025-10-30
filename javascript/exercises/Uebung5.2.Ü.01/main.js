/* Aufgabe: Kontrollstrukturen



Erstelle ein JavaScript-Programm, das folgende Aufgaben ausführt: 

a) Deklariere zwei Variablen alter und begleitet. 
Die Variable alter soll eine Zahl sein, die das Alter einer Person repräsentiert, 
begleitet soll ein boolescher Wert sein, der angibt, ob die Person von einem Erwachsenen begleitet wird oder nicht. 

b) Schreibe eine if-else-Struktur, die überprüft, ob die Person alleine einen Film ab 16 Jahren im Kino sehen darf. 
Die Regeln sind wie folgt: Personen ab 16 Jahren dürfen den Film alleine sehen. 
Personen unter 16 Jahren dürfen den Film nur sehen, wenn sie von einem Erwachsenen begleitet werden. 
Wenn keine der Bedingungen erfüllt ist, darf die Person den Film nicht sehen. 

c) Gib eine Nachricht auf der Konsole aus, die besagt, ob die Person den Film sehen darf oder nicht. 
Verwende für jede Bedingung eine eigene Nachricht.

 */

//a)
let alter = 16
let begleitet = true

//b)
if (alter>=16) {
    begleitet=false;
    console.log(`Die Person darf den film sehen`);
}
