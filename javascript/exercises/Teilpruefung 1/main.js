/* Entwickle ein kleines Spiel, das "Rate die Zahl" heißt. 
-[x] Das Spiel generiert eine zufällige Zahl zwischen 1 und 100, und der Spieler muss diese Zahl erraten. 
-[ ] Der Spieler hat dafür unbegrenzte Versuche. 
-[x] Nach jedem Versuch soll das Spiel dem Spieler mitteilen, ob die geratene Zahl zu hoch, zu niedrig oder korrekt ist. 
-[x] Nutze dabei die Kontrollstrukturen if-else und Schleifen, um die Logik des Spiels zu implementieren. 
-[ ] Du sollst auch Variablen und Datentypen verwenden, um die geratene Zahl und die zufällig generierte Zahl zu speichern. 
-[ ] Implementiere zusätzlich eine Möglichkeit, wie der Spieler das Spiel beenden kann, bevor die Zahl erraten wurde, indem er z.B. 'exit' eingibt.*/



// Zahl wird generiert
let zufall = Math.trunc(Math.random()*100);
let input; // Eingabe über Formular, man bräuchte eigentlich ein Eingabeformular.
// Da wir das nicht haben, kann eine while schleife die eingaben simulieren, bis das spiel gewonnwn oder beendet ist.
input = 50;

intInput = parseInt(input);
let i = intInput;

while (i != "exit") {
    if (input == zufall){
        console.log(`Herzlichen Glückwunsch, du hast richtig geraten! Deine Eingabe ${input} entspricht der generierten Zahl ${zufall}
                    Versuche es erneut oder tipp exit ein, um das Spiel zu verlassen!`);
        console.log(`Die erzeugte Zahl ist ${zufall}`);
    } else { if (input > zufall){
        console.log(`Deine Eingabe ${input} entspricht nicht der generierten Zahl, sie ist zu hoch!
            Versuche es erneut oder tipp exit ein, um das Spiel zu verlassen!`);
    } else if (input < zufall){
        console.log(`Deine Eingabe ${input} entspricht nicht der generierten Zahl, sie ist zu niedrig!
            Versuche es erneut oder tipp exit ein, um das Spiel zu verlassen!`);
    } 

}
console.log("Du hast exit eingegeben. Ich hoffe es hat Spaß gemacht, vielen Dank für das Spiel!");
}


/* {
const fizz = 3
const buzz = 5
const fizzbuzz = fizz * buzz
let i = 0

while (i<=100) {
    if (i % fizzbuzz===0 && i !=0){
        console.log(`FizzBuzz! ${i} ist ein ganzzahliges Vielfaches von ${fizz} und ${buzz}`);
    } else {if (i % buzz ===0 && i !=0){
                console.log(`Buzz! ${i} ist ein ganzzahliges Vielfaches von ${buzz}`);
    } else {if(i % fizz===0 && i !=0){
                console.log(`Fizz! ${i} ist ein ganzzahliges Vielfaches von ${fizz}`);                               
    } else {console.log(i);} //Wenn ich nur eine Ausgabe pro Zahl will, muss ich das console.log(i) in ein else packen, das nur greift, wenn keine Fizz/Buzz/FizzBuzz-Bedingung zutrifft
    } 
    } i++;
}
console.log("Fertig!");
}
 */
