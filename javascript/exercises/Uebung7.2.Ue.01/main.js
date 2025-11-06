/* Aufgabe: Objekte


Erstelle ein JavaScript-Programm, das folgende Anforderungen erfüllt: 

a) Definiere ein Objekt filmSammlung, das zwei Filme enthält. 
Jeder Film soll durch ein eigenes Objekt repräsentiert werden, das die Eigenschaften titel, jahr, genre und eine Methode info hat. 
Die Methode info gibt einen String zurück, der Titel, Jahr und Genre des Films in einem Satz zusammenfasst.  

b) Verwende eine for-in Schleife, um über das Objekt filmSammlung zu iterieren und die info Methode jedes Filmobjekts aufzurufen. 
Gib das Ergebnis in der Konsole aus. 

c) Füge dem Objekt filmSammlung eine Methode alter hinzu, 
die das Alter jedes Films seit seinem Erscheinungsjahr bis zum aktuellen Jahr (nimm hierfür das Jahr 2023 an) berechnet und in der Konsole ausgibt. 
Nutze dabei eine for-in Schleife und die Eigenschaft jahr jedes Films.  

*/


//a)
const filmSammlung = {
    film1      :   {
        titel   :   "Goodfellass",
        jahr    :   1990,
        genre   :   "Mafia / Krimi / Drama",
        info    :   function(){
            return `Der Film "${this.titel}" ist aus dem Jahr "${this.jahr}" und hat das Genre: "${this.genre}".`;
        }
    },
    film2      :   {
        titel   :   "Scarface",
        jahr    :   1983,
        genre   :   "Krimi / Drama",
        info    :   function(){
            return `Der Film "${this.titel}" ist aus dem Jahr "${this.jahr}" und hat das Genre: "${this.genre}".`;
        }
    },   
    alter       :   function(){
            for (const key in this){ // this verweist auf filmSammlung
                if (this[key].jahr) { //prüfung ob eigenschaft jahr hat, key läuft durch ale Eigenschaften von filmSammlung also film1, film2, alter
                    const filmAlter = 2023 - this[key].jahr;
                    console.log(`Der Film "${this[key].titel}" ist aus dem Jahr "${this[key].jahr}" und ist ${filmAlter} Jahre alt.`);
                }
            }
        }                   
    }




//b)
for (const key in filmSammlung){ // gehe über alle Eigenschaftren des Objekts
    if (filmSammlung[key].info){
        console.log(filmSammlung[key].info());
    }


}  

// c)


filmSammlung.alter();
console.log(filmSammlung);

/* 
for (const key in filmSammlung){
    console.log(`${key}, ${filmSammlung[key]}`); // film1, [object Object]
                                                // film2, [object Object]
}


for (const key in filmSammlung){
    console.log("Object key", key); // gibt die Schlüssel des Objekts aus
}

for (const key in filmSammlung){
    console.log("Object value", filmSammlung[key]); //Object value {titel: 'Goodfellass', jahr: 1990, genre: 'Mafia / Krimi / Drama', info: ƒ}
                                                    // Object value {titel: 'Scarface', jahr: 1983, genre: 'Krimi / Drama', info: ƒ}
} 

for (const key in filmSammlung){
    console.log("Object key", key,"Object value", filmSammlung[key]); // Object key film1 Object value {titel: 'Goodfellass', jahr: 1990, genre: 'Mafia / Krimi / Drama', info: ƒ}
                                                                    // Object key film2 Object value {titel: 'Scarface', jahr: 1983, genre: 'Krimi / Drama', info: ƒ}
} 

/* for (const key in filmSammlung.film1){
    if (key === "info"){
        console.log("Object key", [key],"Object value", filmSammlung.film1[key]);
    }
}   */


