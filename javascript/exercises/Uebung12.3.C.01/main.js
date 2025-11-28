/* Aufgabe: Formulare

Entwickle ein JavaScript-Programm für eine Konferenz-Website, um die Anmeldung von Teilnehmern zu verwalten. Das Formular soll folgende Felder enthalten: Vorname, Nachname, E-Mail-Adresse, Teilnahmetyp (Vortragender, Zuhörer), Auswahl der Workshops (maximal 3 aus 5 möglichen), sowie ein Feld für spezielle Ernährungsbedürfnisse. Zusätzlich soll ein Feld für die Zustimmung zur Verarbeitung persönlicher Daten vorhanden sein. Das Programm soll folgende Funktionalitäten umsetzen: 

a) Prüfe, ob alle erforderlichen Felder ausgefüllt sind. Falls nicht, zeige eine entsprechende Fehlermeldung an und verhindere das Absenden des Formulars. 

b) Stelle sicher, dass mindestens ein Workshop ausgewählt wurde, aber nicht mehr als drei. Zeige eine Fehlermeldung an, wenn die Auswahl nicht den Anforderungen entspricht. 

c) Überprüfe, ob die E-Mail-Adresse im richtigen Format eingegeben wurde. Falls nicht, zeige eine Fehlermeldung an. 

d) Implementiere eine Funktion, die das aktuelle Datum und die Uhrzeit anzeigt und überprüft, ob die Anmeldung noch innerhalb der Anmeldefrist (z.B. eine Woche vor der Konferenz) erfolgt. Ist die Anmeldung zu spät, soll eine entsprechende Nachricht angezeigt werden. 

e) Sorge dafür, dass die Zustimmung zur Verarbeitung persönlicher Daten gegeben sein muss, um das Formular absenden zu können. Falls diese Zustimmung fehlt, zeige eine Fehlermeldung an. */
const form = document.querySelector("#anmeldeFormular");
const msg  = document.querySelector("#msg");

const konferenzDatum = new Date("2025-12-10"); // Datum der Konferenz
const anmeldeschluss = new Date(konferenzDatum); 
anmeldeschluss.setDate(anmeldeschluss.getDate() - 7); // eine Woche vorher

function checkAnmeldefrist() {
    const jetzt = new Date();
    
    // Aktuelles Datum auf der Seite anzeigen
    const datumDiv = document.querySelector("#datum");
    if (datumDiv) {
        datumDiv.textContent = `Aktuelles Datum: ${jetzt.toLocaleString()}`;
    }

    if (jetzt > anmeldeschluss) {
        return false; // Anmeldung zu spät
    }
    return true; // Anmeldung noch möglich
}

form.addEventListener("submit", function (event) {
    event.preventDefault(); // verhindert Seiten-Neuladung

    msg.style.color = "red";
    msg.textContent = "";

    const errors = []; // Array für Fehlermeldungen

    const vorname = document.querySelector("#vorname").value.trim(); // trim verhindert Leerzeichen
    const nachname = document.querySelector("#nachname").value.trim();
    const email = document.querySelector("#email").value.trim();
    const teilnahmetyp = document.querySelector("input[name='teilnahmetyp']:checked"); // :checked → aktuell ausgewähltes Element
    const workshop = document.querySelectorAll("input[name='workshop']:checked"); // NodeList, min 1, max 3
    const ernährung = document.querySelector("input[name='ernährung']:checked");
    const datenschutz = document.querySelector("#datenschutz").checked; // boolean

    // a) Pflichtfelder prüfen
    if (vorname === "" || nachname === "" || email === "") {
        errors.push("Bitte füllen Sie Vorname, Nachname und E-Mail aus.");
    }

    if (!teilnahmetyp) {
        errors.push("Bitte wählen Sie einen Teilnahmetyp aus.");
    }

    // b) Workshop-Auswahl überprüfen
    if (workshop.length < 1 || workshop.length > 3) {
        errors.push("Bitte wählen Sie mindestens 1 und höchstens 3 Workshops aus.");
    }

    // Ernährungsoption prüfen
    if (!ernährung) {
        errors.push("Bitte wählen Sie eine Ernährungsoption aus.");
    }

    // e) Zustimmung zur Datenverarbeitung prüfen
    if (!datenschutz) {
        errors.push("Sie müssen der Verarbeitung Ihrer Daten zustimmen, wenn Sie teilnehmen möchten.");
    }

    // c) E-Mail-Überprüfung
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // RegEx prüft @ und Punkt nach @
    if (!emailPattern.test(email)) {
        errors.push("Bitte geben Sie eine gültige E-Mail-Adresse ein.");
    }
    // d) Anmeldefrist prüfen
    if (!checkAnmeldefrist()) {
        errors.push("Die Anmeldung ist leider geschlossen. Die Frist endet eine Woche vor der Konferenz.");

    }

    // Fehler anzeigen
    if (errors.length > 0) {
        msg.innerHTML = errors.join("<br>"); // alle fehler erscheinen dadurch in <div id="msg"> und werden durch einen Zeilenumbruch getrennt
        return; // Formular nicht absenden
    }

    // Formular zurücksetzen oder Absenden
  
    form.reset();
    msg.style.color = "green";
    msg.textContent = "Anmeldung erfolgreich!";
    // form.submit(); // wirklich absenden, dann kein reset davor - wenn daten an den server sollen, dafür ein action="dein-endpunkt" im <form> setzen
    // beispiel für index.html <form id="anmeldeFormular" action="https://example.com/submit" method="POST">
});


