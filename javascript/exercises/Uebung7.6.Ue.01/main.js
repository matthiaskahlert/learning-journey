/* Erstelle eine JavaScript-Funktion alterBerechnen, die das Geburtsjahr einer Person als Parameter erhält 
und das aktuelle Alter der Person zurückgibt. 
Verwende dabei das aktuelle Jahr, das du durch ein Datum-Objekt erhältst. 
Zusätzlich soll die Funktion überprüfen, ob das übergebene Geburtsjahr in der Zukunft liegt. 
In diesem Fall soll die Funktion den String "Geburtsjahr liegt in der Zukunft" zurückgeben. 
Nutze für die Implementierung Variablen, Kontrollstrukturen wie if-else, und Datum-Objekte.   */

function alterBerechnen(geburtsjahr) {
    const aktuellesJahr = new Date().getFullYear(); 
    if (geburtsjahr>aktuellesJahr){
        return"Geburtsjahr liegt in der Zukunft";
    } else {
        alter = aktuellesJahr - geburtsjahr 
        return `Person hat das Alter von ${alter} Jahren.`;
    }
}

console.log(alterBerechnen(1965));
console.log(alterBerechnen(2027));
