/* Entwickle ein kleines Spiel, das "Rate die Zahl" heißt. 
-[x] Das Spiel generiert eine zufällige Zahl zwischen 1 und 100, und der Spieler muss diese Zahl erraten. 
-[x] Der Spieler hat dafür unbegrenzte Versuche. 
-[x] Nach jedem Versuch soll das Spiel dem Spieler mitteilen, ob die geratene Zahl zu hoch, zu niedrig oder korrekt ist. 
-[x] Nutze dabei die Kontrollstrukturen if-else und Schleifen, um die Logik des Spiels zu implementieren. 
-[x] Du sollst auch Variablen und Datentypen verwenden, um die geratene Zahl und die zufällig generierte Zahl zu speichern. 
-[x] Implementiere zusätzlich eine Möglichkeit, wie der Spieler das Spiel beenden kann, bevor die Zahl erraten wurde, indem er z.B. 'exit' eingibt.*/



// Zahl wird generiert
let zufall = Math.trunc(Math.random()*100) +1; //Math.random() generiert eine Zahl zwischen 0 und 1, Math.trunc entfernt die Nachkommastellen, *100 skaliert auf 0-99, +1 verschiebt auf 1-100
// console.log(`Die erzeugte Zahl ist ${zufall}`); // kontrolle als unit test
let input = prompt(`Bitte vor der ersten Zahleneingabe mit f12 die Browserkonsole öffnen!
    Errate die Zahl zwischen 1 und 100 oder gib exit ein um das Spiel zu beendem!`); // Nutzereingabe über prompt, als string
// input = 50; // unit test ohne prompt eingabe für die geratene Zahl
// console.log(typeof input); // Kontrolle des Datentyps der Eingabe

while (input !== "exit") {
    let gerateneZahl = parseInt(input); //für den Zahlenvergleich brauchen wir ein Integer
    if (gerateneZahl === zufall){
        console.log(`Herzlichen Glückwunsch, du hast richtig geraten! Deine Eingabe ${gerateneZahl} entspricht der generierten Zahl ${zufall}!
            Ich hoffe es hat Spaß gemacht, vielen Dank für das Spiel!`);
        break; // Spiel beenden, wenn Zahl erraten
    } else { if (gerateneZahl > zufall){
        console.log(`Deine Eingabe ${gerateneZahl} entspricht nicht der generierten Zahl, sie ist zu hoch!`);
    } else if (gerateneZahl < zufall){
        console.log(`Deine Eingabe ${gerateneZahl} entspricht nicht der generierten Zahl, sie ist zu niedrig!`);
    } 
input = prompt("Neue Eingabe oder tipp exit ein um das Spiel zu beendem!"); // neue Nutzereingabe
} if (input==="exit") {
console.log("Du hast exit eingegeben. Ich hoffe es hat Spaß gemacht, vielen Dank für das Spiel!");
}

}