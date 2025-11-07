/* Entwickle ein JavaScript-Programm, das die folgenden Anforderungen erfüllt:  

a) Definiere ein Objekt auto, das Eigenschaften für marke, modell, farbe, jahr und istVerkauft hat. 
Setze dabei istVerkauft zunächst auf false. 

b) Füge dem Objekt eine Methode verkaufen hinzu, die den Wert von istVerkauft auf true setzt und eine Nachricht in der Konsole ausgibt, 
die besagt, dass das Auto nun verkauft ist. 

c) Verwende eine if-else-Struktur, um zu prüfen, ob das Auto älter als 10 Jahre ist.
Wenn ja, gib eine Nachricht aus, dass das Auto als Oldtimer betrachtet werden kann. 

d) Erstelle eine Funktion autoInfo, die Informationen über das Auto in einem formatierten String zurückgibt (Marke, Modell, Farbe, Jahr). 

e) Verwende eine for-in-Schleife, um alle Eigenschaften des auto-Objekts in der Konsole auszugeben. 

f) Erstelle eine Arrow-Funktion updateFarbe, die als Parameter eine neue Farbe entgegennimmt und die Farbe des Autos aktualisiert.  

g) Demonstriere die Verwendung von try-catch für einfaches Debugging, indem du versuchst, 
eine nicht existierende Methode des auto-Objekts aufzurufen und im Falle eines Fehlers eine entsprechende Nachricht in der Konsole auszugeben.   */

// a)
const auto = {
    marke :         "Škoda",
    modell:         "Enyaq",
    farbe:          "Weiß",
    jahr:           "2025",
    istVerkauft:    false,
    //b)
    verkaufen:      function(){
        this.istVerkauft = true;
        console.log(`Das Fahrzeug ${this.marke + " " + this.modell} ist verkauft.`);
    },
    //d)
    autoInfo: function(){
    for (const key in auto){
        if (typeof auto[key] !== "function"&& key !== "istVerkauft"){       // die Zeile verhindert dass auch Methoden ausgegeben werden
        console.log(`${key}: ${auto[key]}`);
        }
    }
},
//f)
    updateFarbe:    (neueFarbe) =>auto.farbe=neueFarbe
    }

auto.verkaufen();
auto.autoInfo();
auto.updateFarbe("schwarz");


//c)
// aus beispiellösung: const aktuellesJahr = new Date().getFullYear(); 
if (auto.jahr - 2025 >10){  // hier könnte man die variable aktuellesJahr nutzen
      console.log("Das Auto ist als Oldtimer zu betrachten.");
} else {
  console.log("Das Auto ist kein Oldtimer.");
}

//e)
for (const key in auto){
    console.log("Object key", key); // gibt die Schlüssel des Objekts aus
}

//g)
try {
  auto.nichtExistent();
} catch (error) {
  console.error(error);
}

// Folgend ein Unit Test ob die Funktion tut was sie soll indem mir der Wert der Eigenschaft istVerkauft in der Konsole ausgegeben wird, ich entscheide dann ob es funktioniert hat.
for (const key in auto) {
        if (key==="istVerkauft"){ // prüft auf den String "istVerkauft", weil die for...in-Schleife die Eigenschaftsnamen als Text liefert.
        console.log(`Die Eigenschaft ${key} wurde auf ${auto[key]} gesetzt.`);}
    }

// besserer Ansatz als oben, da die Bedingung direkt geprüft wird
if (auto.istVerkauft === true) {
  console.log("Test bestanden: Das Auto wurde als verkauft markiert.");
} else {
  console.error("Test fehlgeschlagen: Das Auto ist nicht als verkauft markiert.");
}


