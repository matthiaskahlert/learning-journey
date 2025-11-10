/* Entwickle ein kleines Programm in JavaScript, das folgende Funktionalitäten umfasst: 

a) Definiere eine Funktion bewerteWetter, die als Parameter eine Zeichenkette wetter erhält. 
Die Funktion gibt basierend auf dem übergebenen Wetterzustand (Sonnig, Bewölkt, Regnerisch, Schneefall) 
eine Empfehlung für eine Aktivität zurück. Verwende eine switch-Anweisung für die Entscheidungsfindung. 

b) Erweitere die Funktion um eine Prüfung der übergebenen Zeichenkette. 
Stelle sicher, dass nur valide Wetterzustände verarbeitet werden (Sonnig, Bewölkt, Regnerisch, Schneefall). 
Gib eine entsprechende Fehlermeldung aus, falls ein ungültiger Zustand übergeben wird. 
Nutze eine Kombination aus if-else und switch. 

c) Implementiere eine Schleife (wahlweise for oder while), die die Funktion bewerteWetter für eine Liste 
von verschiedenen Wetterzuständen aufruft. Die Liste soll mindestens vier verschiedene Zustände enthalten, 
darunter mindestens einen ungültigen Zustand. 

d) Verwende Funktionsausdrücke und/oder Arrow-Funktionen, um eine anonyme Funktion zu definieren, 
die die aktuelle Uhrzeit in Stunden ausgibt und eine Empfehlung abgibt, 
ob es Zeit für das Mittagessen ist (zwischen 12 und 14 Uhr). 

e) Füge Debugging-Code hinzu, der überprüft, ob die Uhrzeit korrekt ausgegeben wird. 
Verwende console.log für die Ausgabe der Ergebnisse und der Empfehlungen */

//a)

function bewerteWetter(wetter){
    const erlaubtesWetter = ["sonnig", "bewölkt", "regnerisch", "schneefall"];
    if (typeof wetter !== "string") {
        return `Eingabe ist kein string, Funktion akzeptiert nur ${erlaubtesWetter.join(", ")}`;
    }
    if (!erlaubtesWetter.includes(wetter)) {
        return `Eingabe ungültig (falscher String?), Funktion akzeptiert nur ${erlaubtesWetter.join(", ")}`;
    }
switch (wetter) {

    case "sonnig":
        return `Das Wetter: ${wetter}, geh zum Strand!`;
        
    case "bewölkt":
        return `Das Wetter: ${wetter}, du brauchst keine Sonnencreme!`;
        
    case "regnerisch":
        return `Das Wetter: ${wetter}, nimm einen Schirm mit!`;
        
    case "schneefall":
        return `Das Wetter: ${wetter}, bau einen Schneemann!`;
    }
}

/* // Testausgaben
console.log(bewerteWetter(1337));       
console.log(bewerteWetter("sonnig"));

console.log(bewerteWetter("bewölkt"));

console.log(bewerteWetter("regnerisch"));

console.log(bewerteWetter("schneefall"));

console.log(bewerteWetter("heiss")); */

// c)

const testAusgaben = [1337, "sonnig", "bewölkt", "regnerisch", "schneefall", "heiss",];
for (let i=0;i<testAusgaben.length; i++){
console.log(bewerteWetter(testAusgaben[i]));
}
 

// d)
const zeit = new Date().getHours();
const checkMittagessen = function(){


    if (zeit >=12 && zeit <=14){
        console.log("Zeit für das Mittagessen, denn es ist zwischen 12 und 14 uhr!");
    } else{
        console.log("Kein Mittagessen, denn es ist nicht zwischen 12 und 14 uhr!");
    }
}
checkMittagessen();
const aktuelleStunde = new Date().getHours();
console.log(`Debug: aktuelle Stunde =${aktuelleStunde}`); //e): das console.log ist die debugging aufgabe, eine separate prüfung ob die zeit korrekt ermittelt wurde.