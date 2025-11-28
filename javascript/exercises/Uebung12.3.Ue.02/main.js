/* Entwickle ein JavaScript-Programm, das ein Formular zur Erfassung von Teilnehmerdaten für einen Online-Kochkurs verwaltet. 
Das Formular soll Felder für den Namen, die E-Mail-Adresse, 
das bevorzugte Küchenthema (z.B. italienisch, asiatisch, vegetarisch) und ob der Teilnehmer ein Anfänger ist oder nicht, enthalten. 
Verwende dabei folgende Anforderungen: 

a) Erstelle ein HTML-Formular mit den entsprechenden Eingabefeldern, 
inklusive eines Dropdown-Menüs für das Küchenthema 
und einer Checkbox für die Anfängeroption. Stelle sicher, dass das Formular einen "Absenden"-Button hat.  

b) Schreibe eine JavaScript-Funktion, die beim Absenden des Formulars aufgerufen wird. 
Diese Funktion soll überprüfen, ob alle Felder ausgefüllt wurden. 
Falls das Feld für den Namen oder die E-Mail-Adresse leer ist, soll eine entsprechende Fehlermeldung angezeigt werden, 
ohne das Formular abzusenden. 

c) Falls das Formular korrekt ausgefüllt wurde, soll eine Bestätigungsnachricht angezeigt werden, 
die den Namen des Teilnehmers und das gewählte Küchenthema enthält. 
Verwende dazu das Event "submit" und verhindere das standardmäßige Absenden des Formulars mit event.preventDefault(). 

d) Implementiere eine Funktion, die prüft, ob der Teilnehmer ein Anfänger ist. 
Wenn ja, füge der Bestätigungsnachricht hinzu, dass der Teilnehmer zusätzliche Ressourcen per E-Mail erhalten wird. */

// a) Formular und Elemente auslesen
const form = document.querySelector("#kochForm");
const msg = document.querySelector("#msg");
const name = document.querySelector("#name");
const email = document.querySelector("#email");
const themaSelect = document.querySelector("#thema");
const anfängerCheckbox = document.querySelector("#anfänger");

// c) Event "submit" für Formular
form.addEventListener("submit", function(event) {
    event.preventDefault(); // verhindert das Standard-Absenden
    msg.style.color = "red";
    msg.textContent = "";

    // b) Validierung: Name und E-Mail müssen ausgefüllt sein
    const errors = [];
    if (!name.value.trim()) errors.push("Bitte geben Sie Ihren Namen ein.");
    if (!email.value.trim()) errors.push("Bitte geben Sie Ihre E-Mail-Adresse ein.");

    if (errors.length > 0) {
        msg.innerHTML = errors.join("<br>");
        return; // Formular nicht absenden
    }

    // c) Bestätigungsnachricht erstellen
    let confirmation = `Vielen Dank, ${name.value}! Sie haben das Küchenthema "${themaSelect.value}" gewählt.`;

    // d) Prüfen, ob Teilnehmer Anfänger ist
    if (anfängerCheckbox.checked) {
        confirmation += " Als Anfänger erhalten Sie zusätzliche Ressourcen per E-Mail.";
    }

    msg.style.color = "green";
    msg.textContent = confirmation;

    // Optional: Formular zurücksetzen
    form.reset();
});