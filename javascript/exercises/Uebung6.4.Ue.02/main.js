/* Aufgabe: Funktionen


Entwickle eine Funktion berechneSteuern, die zwei Parameter annimmt: einkommen und status. Der status kann entweder 'einzeln' oder 'verheiratet' sein. Die Funktion soll die Steuern basierend auf dem Einkommen und dem Status berechnen. Für den Status 'einzeln' gelten folgende Steuersätze: Einkommen bis 12.000 Euro - 12%, Einkommen über 12.000 Euro - 22%. Für den Status 'verheiratet' gelten: Einkommen bis 24.000 Euro - 10%, Einkommen über 24.000 Euro - 20%. Die Funktion soll das Ergebnis zurückgeben. 

a) Formuliere die Funktion berechneSteuern. 

b) Rufe die Funktion mit einem einkommen von 30.000 Euro und dem Status 'einzeln' auf und speichere das Ergebnis in einer Variablen. 

c) Rufe die Funktion mit einem einkommen von 30.000 Euro und dem Status 'verheiratet' auf und speichere das Ergebnis in einer Variablen. 

d) Gib beide Ergebnisse mit console.log aus.   */
//a)
function berechneSteuern (einkommen,status){
    let steuern;
    let berechnung;
    switch (status) {
        case "einzeln":
            if (einkommen<=12000){
                steuern = 12;
            } else {steuern = 22

            } break;        

        case "verheiratet":
            if (einkommen<=24000){
                steuern = 10;
            } else {steuern = 20

            }break;

        default:
            console.log("Status ungültig, bitte 'einzeln' oder 'verheiratet' angeben.");
            return;
    }
    berechnung = einkommen * steuern / 100;
    console.log(`Die zu zahlenden Steuern betragen ${berechnung} €.`);
    return berechnung;
}
//b)
let ergebnisB= berechneSteuern(30000,"einzeln");
//c)
let ergebnisC = berechneSteuern(30000,"verheiratet");

//d)
console.log("Ergebnis Einzeln:", ergebnisB);
console.log("Ergebnis Verheiratet:", ergebnisC);