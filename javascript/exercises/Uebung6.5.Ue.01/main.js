/* Aufgabe: Funktionen


- [x] Entwickle eine Funktion berechneUrlaubstage, die das Alter und die Betriebszugehörigkeit (in Jahren) einer Person als Parameter annimmt. 
- [x] Basierend auf diesen Informationen soll die Funktion die Anzahl der Urlaubstage berechnen und zurückgeben. 

- [x] Jede Person hat zunächst einen Anspruch auf 24 Urlaubstage. 
- [x] Personen über 50 Jahre erhalten 5 zusätzliche Tage. 
- [x] Für jedes Jahr der Betriebszugehörigkeit gibt es einen zusätzlichen Tag, jedoch maximal 10 zusätzliche Tage. 
- [x] Verwende if-else-Kontrollstrukturen, um die Bedingungen zu prüfen. 
- [x] Nutze außerdem eine Arrow-Funktion, um die Logik für die zusätzlichen Tage aufgrund der Betriebszugehörigkeit zu implementieren. 
- [x] Demonstriere die Verwendung von console.log, um das Ergebnis für zwei unterschiedliche Szenarien auszugeben: 

 

Eine 45-jährige Person mit 12 Jahren Betriebszugehörigkeit. 

Eine 55-jährige Person mit 8 Jahren Betriebszugehörigkeit. */

function berechneUrlaubstage (alter, anzahlJahre){
    let basisUrlaub = 24;
    let zusatzUrlaubAlter = 0;
    let zusatzUrlaubBetrieb = 0;
    if (alter >=50){
        zusatzUrlaubAlter = 5; // 5 zusätzliche Tage ab alter von 50 Jahren
    }   
    const summe = (anzahlJahre, zusatzUrlaubBetrieb) => (anzahlJahre >=10) ? (zusatzUrlaubBetrieb = 10) : (zusatzUrlaubBetrieb = anzahlJahre);  // Arrow Funktion für zusatzUrlaubBetrieb 
    zusatzUrlaubBetrieb = summe (anzahlJahre,zusatzUrlaubBetrieb);
    console.log(`Die Person im Alter von ${alter} hat Anspruch auf ${basisUrlaub + zusatzUrlaubAlter + zusatzUrlaubBetrieb} Urlaubstage in diesem Jahr.`);
    const urlaubsanspruch = basisUrlaub + zusatzUrlaubAlter + zusatzUrlaubBetrieb;
    return urlaubsanspruch;
// folgend der initiale ansatz nur mit if/else für zusatzUrlaubBetrieb
//    if (anzahlJahre >=10){
//        zusatzUrlaubBetrieb = 10;   //wenn Betriebszugehörigkeit großer gleich zehn, max wert erreicht
//    } else {
//        zusatzUrlaubBetrieb = anzahlJahre; //1 zusätzlicher Tag pro Jahr solange Betriebszugehörigkeit kleiner zehn
//    }    
// 
// folgend der zweite Ansatz von mir mithilfe von Ternary operatoren in der klassischen Funktion
//  function summe (anzahlJahre, zusatzUrlaubBetrieb){
//        return (anzahlJahre >=10) ? (zusatzUrlaubBetrieb = 10) : (zusatzUrlaubBetrieb = anzahlJahre); //Umsetzung der if/else logik in ternary Operatoren
// }

    
}

        

berechneUrlaubstage (45, 12);   //Die Person im Alter von 45 hat Anspruch auf 34 Urlaubstage in diesem Jahr.
berechneUrlaubstage (55, 8);    // Die Person im Alter von 55 hat Anspruch auf 37 Urlaubstage in diesem Jahr.
