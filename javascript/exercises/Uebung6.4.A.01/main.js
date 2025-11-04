
let besucherZaehler = 0

function besucherHinzufuegen(anzahl){
    besucherZaehler = besucherZaehler + anzahl; // aktualisiere den Zähler
    console.log(`Aktuelle Besucheranzahl: ${besucherZaehler}`);
    
    if (besucherZaehler >=20){  // wenn 20 oder mehr Besucher, setze Zähler zurück
        resetBesucherZaehler(); // Funktion kann aufgerufen werden bevor sie deklariert wird
    } else if (besucherZaehler >= 10){ // wenn 10 oder mehr Besucher, setze status auf voll
        let status = "voll";
        console.log("Status:", status);
        return      // verhindert die weitere Ausführung der Funktion
    } else status = "offen"; // sonst status offen
    console.log("Status:", status);
}

besucherHinzufuegen(11); // prüft den status voll
besucherHinzufuegen(-4); //prüfe den Zustandsübergang zu status offen
besucherHinzufuegen(15); //prüfe den reset bei über 20 Besuchern

function resetBesucherZaehler(){
    besucherZaehler = 0;
    console.log(`Aktuelle Besucheranzahl: ${besucherZaehler}. der Zähler wurde resetted.`);
}

