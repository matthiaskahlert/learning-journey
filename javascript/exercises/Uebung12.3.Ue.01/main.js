/* Erstelle ein JavaScript-Programm, das ein Formular zur Eingabe eines Veranstaltungstermins inklusive der Dauer in Stunden nutzt. Das Formular soll Felder für den Titel der Veranstaltung, das Datum, die Startzeit und die Dauer in Stunden enthalten. Nach dem Absenden des Formulars soll das Programm überprüfen, ob das eingegebene Datum in der Zukunft liegt und ob die Dauer realistisch ist (zwischen 1 und 8 Stunden). Falls das Datum nicht in der Zukunft liegt oder die Dauer nicht im angegebenen Bereich liegt, soll eine entsprechende Fehlermeldung angezeigt werden. Andernfalls soll eine Bestätigung mit den eingegebenen Daten und dem berechneten Endzeitpunkt der Veranstaltung ausgegeben werden.   */

const jetzt = new Date();
const form = document.querySelector("#veranstaltungsFormular");
const msg  = document.querySelector("#msg");

form.addEventListener("submit", function (event) {
    event.preventDefault(); // verhindert Seiten-Neuladung
    msg.style.color = "red";
    msg.textContent = "";
    const errors = []; // Array für Fehlermeldungen

    const titel = document.querySelector("#titel").value.trim();
    const datum = document.querySelector("#datumInput").value;
    const startzeit = document.querySelector("#startzeit").value;
    const dauer = parseInt(document.querySelector("#dauer").value); // input ist string, daher parseInt

    // Pflichtfeld prüfen
    if (titel === "") {
        errors.push("Bitte geben Sie einen Veranstaltungstitel ein.");
    }

    // Datum in der Zukunft prüfen
    const veranstaltungsDatum = new Date(`${datum}T${startzeit}`);
    if (veranstaltungsDatum <= jetzt) {
        errors.push("Das Datum muss in der Zukunft liegen.");
    }
    // Dauer prüfen
    if (isNaN(dauer) || dauer < 1 || dauer > 8) {
        errors.push("Die Dauer muss zwischen 1 und 8 Stunden liegen.");
    }
    // Fehler anzeigen
    if (errors.length > 0) {
        msg.innerHTML = errors.join("<br>"); // alle fehler erscheinen dadurch in <div id="msg"> und werden durch einen Zeilenumbruch getrennt
        return; // Formular nicht absenden
    }

    // Endzeit berechnen
    const endDatum = new Date(veranstaltungsDatum);
    endDatum.setHours(endDatum.getHours() + dauer);
    // Formular zurücksetzen oder Absenden
  
    form.reset();
    msg.style.color = "green";
    msg.innerHTML = `
        <strong>Veranstaltung erfolgreich eingetragen!</strong><br>
        Titel: ${titel}<br>
        Datum: ${veranstaltungsDatum.toLocaleDateString()}<br>
        Start: ${veranstaltungsDatum.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})} Uhr<br>
        Dauer: ${dauer} Stunden<br>
        Ende: ${endDatum.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})} Uhr
    `;

});
console.log(datum, startzeit, `${datum}T${startzeit}`);