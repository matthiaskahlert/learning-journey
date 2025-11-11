/* Erstelle eine JavaScript-Funktion verwalteFilmSammlung, die ein Array von Filmobjekten verwaltet. 
Jedes Filmobjekt soll folgende Eigenschaften haben: titel, jahr, genre, bewertung. 
Die Funktion soll folgende Funktionalitäten bieten: 

a) Hinzufügen eines neuen Films. 

b) Aktualisieren der Bewertung eines Films durch den Titel. 

c) Löschen eines Films durch den Titel. 

d) Anzeigen aller Filme in der Konsole, sortiert nach dem Jahr der Veröffentlichung. 

e) Suchen eines Films durch den Titel und Anzeigen der Details in der Konsole. 

Verwende dabei Kontrollstrukturen, Schleifen, Bedingungen, und Objektmanipulationen, die du kennst. 
Nutze die Konsole zur Ausgabe von Informationen.  */




const verwalteFilmSammlung = function() {
    const filmObjekte    =   [{ // Array das alle filme speichert
        titel       :   "Goodfellass",
        jahr        :   1990,
        genre       :   "Mafia / Krimi / Drama",
        bewertung   :   "8/10"
        },

       {
        titel       :   "Scarface",
        jahr        :   1983,
        genre       :   "Krimi / Drama",
        bewertung   :   "7/10"
        }
    ];

    // a) Hinzufügen eines neuen Films
    const hinzufuegen = function (titel, jahr, genre, bewertung){
        const neuerFilm = {titel, jahr, genre, bewertung}; //neues objekt wird gebaut
        filmObjekte.push(neuerFilm);                        // nimm das array filmObjekte und füge es das neue objekt hinten an
        console.log(`Film "${titel}" wurde hinzugefügt`);
    }
    // b) Aktualisieren der Bewertung eines Films durch den Titel.
    const bewerten = function (titel, bewertungNeu) {
        for (let i=0;i<filmObjekte.length; i++){
        if (filmObjekte[i].titel === titel) {
        filmObjekte[i].bewertung = bewertungNeu
        console.log(`Film "${titel}" hat eine neue Bewertung: "${bewertungNeu}"`);
           }
        }
    }
    // c) Löschen eines Films durch den Titel.
    const loeschen = function (titel) {
        for (let i=0;i<filmObjekte.length; i++){
        if (filmObjekte[i].titel === titel) {
        filmObjekte.splice(i,1);
        console.log(`Film "${titel}" wurde gelöscht.`);
        return;
           }
        }
    }
    // d) Anzeigen aller Filme in der Konsole, sortiert nach dem Jahr der Veröffentlichung.
    const sortieren = function() {
    const sortiert = [...filmObjekte].sort((a,b) => a.jahr - b.jahr);
    for (const key of sortiert) {
        console.log(`${key.titel} (${key.jahr}) - ${key.bewertung}`);
        }
    }
    // e) Suchen eines Films durch den Titel und Anzeigen der Details in der Konsole. 
    const suchen = function(titel) {
    for (const film of filmObjekte) {
        if (film.titel === titel) {
            console.log(film);
            return;
        }
    }
    console.log(`Film "${titel}" nicht gefunden.`);
}




     return {
        filmObjekte,
        hinzufuegen,
        bewerten,
        loeschen,
        sortieren,
        suchen,
     };

     }

const filmSammlung = verwalteFilmSammlung(); // wird gebraucht um das ergebnis vom funktionsaufruf zu speichern in der variablen!

for (const key of filmSammlung.filmObjekte){
    console.log(key.titel)
}
console.log(filmSammlung);
filmSammlung.hinzufuegen("Stargate", 1994, "ScienceFiction", "6/10");
console.log(filmSammlung);
for(const key of filmSammlung.filmObjekte){
    console.log(key.titel)
}

for(const key of filmSammlung.filmObjekte){
    console.log(key.titel, key.bewertung)
}
filmSammlung.bewerten("Scarface", "9/10");

for(const key of filmSammlung.filmObjekte){
    console.log(key.titel, key.bewertung)
}

filmSammlung.loeschen("Scarface");
console.log(filmSammlung);

filmSammlung.sortieren();
filmSammlung.suchen("Stargate");
filmSammlung.suchen("Scarface");


  