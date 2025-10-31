const x = 100
const y = 400

if (x>=y) {
    let z = x + y; 
} else {
    const z = y - x;

}
 //   console.log(z); //log:main.js:10 Uncaught ReferenceError: z is not defined denn der Gültigkeitsbereich der Variablen ist nur innerhalb der geschweiften Klammern!


 // Wenn nur eine Anweisung vorliegt, muss sie nicht in geschweifte Klammer gesetzt werden!
if (x>=y) console.log(`${x}>=${y}`);
else console.log(`${x} ist nicht >= ${y}`);

const width = 360;
const max = 480;

if (width>max) {
    console.log(`${width} ist größer als ${max}`);
} else if (width<=max) {
    console.log(`${width} ist kleiner oder gleich ${max}`);
}   if (width<max) {
    console.log(`${width} ist kleiner als ${max}`);
} else {
    console.log(`Ein unvorhergesehener Fehler ist aufgetreten.`);  //Dies kann abfangen wenn z.b. keiner der Fälle eintritt, beispielsweise wenn width ein String wäre.
}

const min = 200
if (width < max && width > min){
    console.log(`${width} liegt zwischen ${max} und ${min} `);
}


const width2 = 22;
const max2 = 48;
const min2 = 20;
if (width2 === max2 || width2 > min2 ) {
    console.log(`${width2} ist gleich ${max2} oder größer als ${min2}`);
    } else {
        console.log(`${width2} ist nicht gleich ${max2} und nicht größer als ${min2}`);
    }

    
const country = "Frankreich";
switch (country) {
    case "Deutschland":
        console.log("Deutschland");
        break;

    case "Frankreich":
        console.log("Frankreich");
        break;

    case "Irland":
        console.log("Irland");
        break;

    default:
        console.log(`Weder Deutschland, Frankreich oder Irland`);
}

const auswahl = "Apfelsinen";
switch(auswahl) {
    case "Birnen":
        {
        const wahl = "Birnen";
        console.log(`${wahl}`);
        }
        break;
    case "Äpfel":
        {
        const wahl = "Äpfel";
        console.log(`${wahl}`);
        }
        break;
    default:
        console.log(`${auswahl} nicht im Angebot`); // log: Uncaught SyntaxError: Identifier 'wahl' has already been declared
    }

    // Übung 5.4
    // Die Aufgabe ist es, einen Stundenplan mit switch cases zu erstellen, die Stunde soll den Datentyp Float haben, z.B. const hour = 17.18
    // es sollen sieben case Fälle sein (und ein default wenn kein Unterricht ist).
    // bei 2. soll man die pausen mit logischem oder umsetzen. 3. Teil der aufgabe ist es, den Stundenplan mit of/else umzusetzen.
//1.
const hour = 8.01
//mein ursprünglicher ansatz war, den ausdruck hour zu wählen also switch(hour). dies hat nicht funktioniert, der code ist immer zum default gesprungen.
//  dann habe ich festgestellt, dass das label der cases keine bedingungen sondern nur werte mit dem ausdruck vergleichen kann.
// " switch vergleicht den Wert der Bedingung" also des Ausdrucks! " mit dem Wert, der neben jeder case-Marke aufgeführt ist "
// daher prüft meine lösung nun ob die bedingung des ausdrucks true ist mit switch(true), so kann ich bedingungen im case label haben.
switch(true) { 
    case (hour >=8.00 && hour <=10.00): // HTML lernen
        {
        const fach = "HTML lernen";
        console.log(`${fach}`);
        }
        break;
    case (hour >=11.01 && hour <=12.00): // CSS lernen
        {
        const fach = "CSS lernen";
        console.log(`${fach}`);
        }
        break;
    case (hour >=13.01 && hour <=15.00): // JavaScript lernen
        {
        const fach = "JavaScript lernen";
        console.log(`${fach}`);
        }
        break;
    case (hour >=16.01 && hour <=17.00): //Übungen
        {
        const fach = "Übungen";
        console.log(`${fach}`);
        }
        break;
/*     case (hour >=10.01 && hour <=11.00): // Pause
        {
        const fach = "Pause";
        console.log(`${fach}`);
        }
        break;
    case (hour >=12.01 && hour <=13.00): // Pause
        {
        const fach = "Pause";
        console.log(`${fach}`);
        }
        break;
    case (hour >=15.01 && hour <=16.00): // Pause
        {
        const fach = "Pause";
        console.log(`${fach}`);
        }
        break; */



    //2.
        case ((hour >=10.01 && hour <=11.00) || (hour >=12.01 && hour <=13.00) ||(hour >=15.01 && hour <=16.00)): // Pause
        {
        const fach = "Pause";
        console.log(`${fach}`);
        }
        break;
    default:
        console.log(`Kein Unterricht!`); //log:Kein Unterricht!
    }
//3.
if (hour >=8.00 && hour <=10.00){     // HTML lernen   
        const fach = "HTML lernen";
        console.log(`${fach}`);        
    } else if (hour >=11.01 && hour <=12.00) {// CSS lernen        
            const fach = "CSS lernen";
            console.log(`${fach}`);
    } else if (hour >=13.01 && hour <=15.00){ // JavaScript lernen        
            const fach = "JavaScript lernen";
            console.log(`${fach}`);
    } else if (hour >=16.01 && hour <=17.00) { //Übungen        
            const fach = "Übungen";
            console.log(`${fach}`);
    } else if ((hour >=10.01 && hour <=11.00) || (hour >=12.01 && hour <=13.00) ||(hour >=15.01 && hour <=16.00)){ // Pause        
            const fach = "Pause";
            console.log(`${fach}`);
    } else {
    console.log(`Kein Unterricht!`); //log:Kein Unterricht!
}

// Schleifen:

const step = 5
for (let i = 1; i<=20; i+=step) {
    const result = i * 17;
    console.log("result", `${i} * 17 = ${result}`);
}

const farbton = [14, 28, 95]
const saettigung = [50, 100]

for (let i =0; i<farbton.length; i++) {
    console.log(`${i}. Farbe: ${farbton[i]}`)
    for (let j=0; j<saettigung.length; j++) {
        console.log(`Farbe hsl(${farbton[i]}, ${saettigung[j]}%, 100%)`) // hsl steht für Hue, Saturation, Lightness, also Farbton, Sättigung, Helligkeit.
    }
}


/* log Ausgabe: 
0. Farbe: 14
main.js:182 Farbe hsl(14, 50%, 100%)
main.js:182 Farbe hsl(14, 100%, 100%)
main.js:180 1. Farbe: 28
main.js:182 Farbe hsl(28, 50%, 100%)
main.js:182 Farbe hsl(28, 100%, 100%)
main.js:180 2. Farbe: 95
main.js:182 Farbe hsl(95, 50%, 100%)
main.js:182 Farbe hsl(95, 100%, 100%) */

for (let i = 0; i<12; i++){
    console.log(i);
    if (i===8) {
        console.log("Schleife abbrechen");
        break;
    }
}
for (let i = 0; i<12; i++){
    if (i===5 || i === 10){
        console.log(`${i} überspringen`); 
        continue;   // hier sagt continue:"ich bin fertig mit dem durchlauf", also bei index 5 und 10 wird die else anweisung übersprungen.
    } else {
        console.log(`${i}`);
    }
}


// while schleife
let i = 0;
while (i<10){
    console.log(`${i} ist i.`)
    i++;
}

// verschachtelte while schleifen
{
let i = 0
while (i<=4){
            console.log(`i ist ${i}`);
            let j = 10;
                while (j>5) {
                    const result = i * j;
                    console.log(`${i} * ${j} = ${result}`);
                    j--;
                            }
            i++;
            }
}

let summe = 0
let a;
outerloop:
while (true){
        a = 1

        while (a<3){
                summe +=a; //addiert 1 oder 2
                if (summe > 12) {
                    break outerloop; // beendet die öußere Schleife
                }
                console.log(`summe = ${summe} (a=${a})`);
                a++;
            }
    }
/* summe = 1 (a=1)
main.js:248 summe = 3 (a=2)
main.js:248 summe = 4 (a=1)
main.js:248 summe = 6 (a=2)
main.js:248 summe = 7 (a=1)
main.js:248 summe = 9 (a=2)
main.js:248 summe = 10 (a=1)
main.js:248 summe = 12 (a=2) */

{
    outerLoop: // <-- Labelname
    for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        console.log(`i=${i}, j=${j}`);
        if (i === 1 && j === 1) {
        console.log("Beide Schleifen abbrechen!");
        break outerLoop; // <-- beendet die äußere Schleife
        }
    }
    }

console.log("Fertig!");
}

/* Übung 5.7
Gib die Zahlen von 1 bis 100 aus: Dabei sollen alle Vielfachen von 3 zusätzlich Fizz
und alle Vielfachen von 5 Buzz ausgeben und am Ende auch noch FizzBuzz bei
allen Vielfachen von 3 und 5. Löse die Aufgabe mit einer for-Schleife und mit einer
while-Schleife. Der Modulo-Operator % prüft, ob eine Zahl ein Vielfaches einer
Zahl ist. 

Für die wirklich ambitionierten Programmierer: Kann die Aufgabe mit
einer einzigen Zeile gelöst werden? Tipp: Nutze den Ternary-Operator – eine
kompakte Schreibweise für eine bedingte Zuweisung. */