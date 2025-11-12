/* Du arbeitest als Entwickler*in in einem Unternehmen, das eine interne Webanwendung zur Verwaltung von Mitarbeiterdaten entwickelt. 
Die Anwendung soll es ermöglichen, Mitarbeiterdaten wie Name, Alter, Abteilung und Jahresgehalt in einem Array von Objekten zu speichern. 
Außerdem soll die Anwendung die Möglichkeit bieten, 
neue Mitarbeiter hinzuzufügen, 
Mitarbeiterdaten zu aktualisieren, 
Mitarbeiter nach verschiedenen Kriterien zu filtern 
und die durchschnittlichen Jahresgehälter innerhalb der Abteilungen zu berechnen. 

a) Erstelle eine Klasse Mitarbeiter, die Konstruktorparameter für Name, Alter, Abteilung und Jahresgehalt hat. 
Die Klasse soll auch eine Methode vorstellen enthalten, die eine kurze Beschreibung des Mitarbeiters ausgibt. 

b) Implementiere eine Funktion mitarbeiterHinzufuegen, die ein Mitarbeiterobjekt zu einem Array von Mitarbeiterobjekten hinzufügt. 

c) Implementiere eine Funktion mitarbeiterAktualisieren, die es ermöglicht, das Jahresgehalt eines Mitarbeiters anhand seines Namens zu aktualisieren. 

d) Implementiere eine Funktion durchschnittsGehaltBerechnen, die das durchschnittliche Jahresgehalt innerhalb einer bestimmten Abteilung berechnet. 

e) Implementiere eine Funktion mitarbeiterFiltern, die Mitarbeiter nach einem spezifischen Kriterium filtert (z.B. alle Mitarbeiter über 30 Jahre). 

f) Verwende die Array.prototype.sort-Methode, um die Mitarbeiter nach ihrem Jahresgehalt in aufsteigender Reihenfolge zu sortieren.   */

class Mitarbeiter {
    constructor(name, alter, abteilung, jahresgehalt){
    this.name                   =   name;
    this.alter                  =   alter;
    this.abteilung              =   abteilung;
    this.jahresgehalt           =   jahresgehalt;

}
    beschreibung(){         // fügt jedem Objekt eine eigene Methode zu - alles, was in einer Klasse als Name + Klammern {} steht, ist eine Methode, auch ohne function davor.
        return `${this.name} ist ${this.alter} Jahre alt, arbeitet in der Abteilung ${this.abteilung} und verdient ${this.jahresgehalt} pro Jahr.`
    };

}
// (name, alter, abteilung, jahresgehalt)
const mitarbeiterDaten = [
    // Marketing
    new Mitarbeiter("Max Mustermann", 38, "Marketing", 72000),
    new Mitarbeiter("Laura Hoffmann", 31, "Marketing", 68000),
    new Mitarbeiter("Tobias Klein", 44, "Marketing", 75000),
    new Mitarbeiter("Julia König", 27, "Marketing", 64000),

    // IT
    new Mitarbeiter("Lukas Weber", 45, "IT", 85000),
    new Mitarbeiter("Nina Schröder", 34, "IT", 79000),
    new Mitarbeiter("Felix Brandt", 29, "IT", 56000),
    new Mitarbeiter("Stefan Berger", 50, "IT", 42000),

    // Vertrieb
    new Mitarbeiter("Anna Schneider", 29, "Vertrieb", 68000),
    new Mitarbeiter("Kevin Meier", 36, "Vertrieb", 62000),
    new Mitarbeiter("Sabrina Lehmann", 32, "Vertrieb", 60000),
    new Mitarbeiter("Thomas Fischer", 40, "Vertrieb", 56000),

    // Finanzen
    new Mitarbeiter("Jonas Richter", 41, "Finanzen", 78000),
    new Mitarbeiter("Miriam Krüger", 37, "Finanzen", 82000),
    new Mitarbeiter("Patrick Schmitt", 46, "Finanzen", 88000),
    new Mitarbeiter("Claudia Neumann", 30, "Finanzen", 74000)
];
console.log(mitarbeiterDaten[0].beschreibung()); // Testausgabe der Methode
// console.log(mitarbeiterDaten.beschreibung());

//b)

const mitarbeiterHinzufuegen = function(name, alter, abteilung, jahresgehalt){
    const neuerMitarbeiter = new Mitarbeiter(name, alter, abteilung, jahresgehalt); 
    mitarbeiterDaten.push(neuerMitarbeiter);
    console.log(`"${neuerMitarbeiter.name}" wurde hinzugefügt`);
    };
mitarbeiterHinzufuegen("Dennis Walter", 35, "Marketing", 69000);

for (const elem of mitarbeiterDaten){

    // console.log(elem); // gibt alle daten aus
    if (elem.name === "Dennis Walter"){
        console.log(`Datensatz wurde korrekt hinzugefügt.`);
        break;
    }
}


//c)) Jahresgehalt anhand von Namen aktualisieren

    const mitarbeiterAktualisieren = function(name, neuesGehalt){
       for (const elem of mitarbeiterDaten){
            if (elem.name === name){
                elem.jahresgehalt = neuesGehalt;
            console.log(`Datensatz wurde korrekt aktualisiert. 
                Das neue Gehalt von ${elem.name} beträgt ${elem.jahresgehalt}.`);
            console.log(elem);
            }
    }

    };
mitarbeiterAktualisieren("Dennis Walter", 79000);
// d) durchschnittliches jahresgehalt innerhalb einer abteilung
const durchschnittsGehaltBerechnen = function(abteilung){
    let summe = 0;  //gesamtsumme
    let anzahl = 0;  //anzahl Mitarbeiter
    for (const mitarbeiter of mitarbeiterDaten){
        if (mitarbeiter.abteilung === abteilung){
            summe += mitarbeiter.jahresgehalt;  // gehalt addieren
            anzahl++;
        }
    }
    
    const durchschnitt = summe / anzahl;
    return durchschnitt;
};
console.log(durchschnittsGehaltBerechnen("Marketing"));


/*// d) durchschnittliches jahresgehalt innerhalb einer abteilung
    const durchschnittsGehaltBerechnen = function(abteilung){
        const mitarbeiterFilter = mitarbeiterDaten.filter(function(m) {
            return m.abteilung === abteilung;
    });
    const gehälter = mitarbeiterFilter.reduce(function(acc, m){
        return acc + m.jahresgehalt;
    },0);
    const durchschnitt = mitarbeiterFilter.length ? gehälter / mitarbeiterFilter.length : 0;
    return durchschnitt;
    };
 */


// e) Implementiere eine Funktion mitarbeiterFiltern, die Mitarbeiter nach einem spezifischen Kriterium filtert (z.B. alle Mitarbeiter über 30 Jahre). 
    const mitarbeiterFiltern = function(){
       return mitarbeiterDaten.filter(function(m) {
            return m.alter > 30;
        });

    };
    console.log(mitarbeiterFiltern());
//  f) Verwende die Array.prototype.sort-Methode

const sortierteDaten = [...mitarbeiterDaten].sort(function(a, b){
    return a.jahresgehalt - b.jahresgehalt;
});
console.log(sortierteDaten.map(m => m.name + ": " + m.jahresgehalt));
