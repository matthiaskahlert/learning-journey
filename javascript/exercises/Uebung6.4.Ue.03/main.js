/* Entwickle eine Funktion berechneUrlaubstage, die basierend auf der Anzahl der Jahre, die ein Mitarbeiter im Unternehmen gearbeitet hat, die Anzahl der Urlaubstage berechnet. Die Funktion soll zwei Parameter haben: den Namen des Mitarbeiters (ein String) und die Anzahl der Jahre, die der Mitarbeiter im Unternehmen gearbeitet hat (eine Zahl). Die Basisanzahl der Urlaubstage beträgt 26 Tage. Für jedes gearbeitete Jahr erhält der Mitarbeiter einen zusätzlichen Urlaubstag, jedoch darf die maximale Anzahl der Urlaubstage 30 nicht überschreiten. Verwende eine if-else-Struktur, um zu prüfen, ob die Anzahl der Jahre die maximale Anzahl der zusätzlichen Urlaubstage überschreitet. Gib am Ende der Funktion einen String zurück, der folgendermaßen formatiert sein sollte: "Mitarbeiter [Name] hat Anspruch auf [Anzahl] Urlaubstage in diesem Jahr." */

function berechneUrlaubstage (nameMitarbeiter, anzahlJahre){
    let basisUrlaub = 26;
    let zusatzUrlaub = 0;
    if (anzahlJahre >=4){
        zusatzUrlaub = 4; //maximal 4 zusätzliche Tage
    } else {
        zusatzUrlaub = anzahlJahre; //1 zusätzlicher Tag pro Jahr
    }       
        
    console.log(`Mitarbeiter ${nameMitarbeiter} hat Anspruch auf ${basisUrlaub + zusatzUrlaub} Urlaubstage in diesem Jahr.`);
}

        

berechneUrlaubstage("Matthias", 12);
berechneUrlaubstage("Julia", 3);
berechneUrlaubstage("Edda", 0);
berechneUrlaubstage("Kjell", 4);