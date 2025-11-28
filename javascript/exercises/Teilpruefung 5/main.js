/* Entwickle eine Webanwendung zur Verwaltung von Veranstaltungseinladungen. 
Die Anwendung soll es einem Benutzer ermöglichen, Veranstaltungsdetails einzugeben, 
Teilnehmer hinzuzufügen oder zu entfernen und die Einladungen per E-Mail zu versenden. 
Die Anwendung soll auch überprüfen, ob alle erforderlichen Informationen vorhanden sind, 
bevor die Einladungen versendet werden.  

a) Erstelle ein HTML-Formular mit Feldern für die Veranstaltungsdetails: 
Titel, Datum, Uhrzeit, Ort und eine Beschreibung. 
Füge auch eine dynamische Liste von Teilnehmern hinzu, 
die Vorname, Nachname und E-Mail-Adresse enthält.  

b) Implementiere JavaScript-Logik, um Teilnehmer zur Liste hinzuzufügen. 
Jeder Teilnehmer soll in einem Array gespeichert werden. 
Überprüfe, ob die E-Mail-Adresse im richtigen Format vorliegt und nicht null oder undefined ist.  

c) Implementiere eine Funktion, die prüft, ob alle Formularfelder (Titel, Datum, Uhrzeit, Ort, Beschreibung) 
ausgefüllt sind und mindestens ein Teilnehmer hinzugefügt wurde. 
Wenn ein Feld leer ist oder keine Teilnehmer vorhanden sind, soll eine entsprechende Fehlermeldung angezeigt werden.  

d) Füge Event-Listener hinzu, die auf das "Submit"-Event des Formulars reagieren. 
Verhindere das Standardverhalten des Formularabsendens und führe stattdessen die Überprüfung der Eingaben durch. 
Wenn alle Überprüfungen erfolgreich sind, zeige eine Bestätigungsmeldung an, 
dass die Einladungen versendet wurden (das tatsächliche Versenden der E-Mails wird simuliert). 

e) Implementiere eine Funktion, die das aktuelle Datum und die Dauer bis zum Veranstaltungsdatum berechnet 
und diese Informationen auf der Webseite anzeigt. */

// a) HTML-Formularfelder auslesen
const form = document.querySelector("#eventForm");
const msg  = document.querySelector("#msg");

    // Veranstaltungselemente
const titel = document.querySelector("#titel");
const datum = document.querySelector("#datum");
const zeit = document.querySelector("#zeit");
const ort = document.querySelector("#ort");
const beschreibung = document.querySelector("#beschreibung");
    // Teilnehmerelemente
const vorname = document.querySelector("#vorname");
const nachname = document.querySelector("#nachname");
const email = document.querySelector("#email");

const teilnehmerButton = document.querySelector("#addTeilnehmer");
const teilnehmerAnzeige = document.querySelector("#teilnehmerAnzeige");

let teilnehmerListe = [];

// e) Funktion zur Berechnung der Dauer bis zum Event
const dauerAnzeige = document.querySelector("#dauerAnzeige");


function berechneDauer() {

    const datumWert = datum.value;
    const zeitWert = zeit.value;

    // Wenn noch nicht beide ausgefüllt sind, nix anzeigen
    if (!datumWert || !zeitWert) {
        dauerAnzeige.textContent = "";
        return;
    }

    const jetzt = new Date();
    const eventDatum = new Date(`${datumWert}T${zeitWert}`);

    const diffMs = eventDatum - jetzt;

    if (diffMs < 0) {
        dauerAnzeige.style.color = "red";
        dauerAnzeige.textContent = "Das Veranstaltungsdatum liegt in der Vergangenheit!";
        return;
    }

    const tage = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    const stunden = Math.floor((diffMs / (1000 * 60 * 60)) % 24);
    const minuten = Math.floor((diffMs / (1000 * 60)) % 60);

    dauerAnzeige.style.color = "black";
    dauerAnzeige.textContent = 
        `Die Veranstaltung beginnt in ${tage} Tagen, ${stunden} Stunden und ${minuten} Minuten.`;
}

// e) Eventlistener für Live-Aktualisierung
datum.addEventListener("input", berechneDauer);
zeit.addEventListener("input", berechneDauer);



// b) Teilnehmer hinzufügen
teilnehmerButton.addEventListener("click", function () {
    msg.textContent = "";

    // Teilnehmerwerte auslesen
    const vornameWert = vorname.value.trim();
    const nachnameWert = nachname.value.trim();
    const emailWert = email.value.trim();

    // Array für Fehlermeldungen bei den Teilnehmern
    const errorsTeilnehmer = []; 

    if (!vornameWert || !nachnameWert || !emailWert) {
        errorsTeilnehmer.push("Bitte füllen Sie alle Teilnehmerfelder aus.");
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailWert)) {
        errorsTeilnehmer.push("Bitte geben Sie eine gültige Teilnehmer-E-Mail ein.");
    }

    if (errorsTeilnehmer.length > 0) {
        msg.style.color = "red";
        msg.innerHTML = errorsTeilnehmer.join("<br>");
        return;
    }

    // Teilnehmer ins Array einfügen
    teilnehmerListe.push({ 
        vorname: vornameWert, 
        nachname: nachnameWert, 
        email: emailWert 
    });

    console.log("Teilnehmerliste:", teilnehmerListe);

    // In HTML-Liste anzeigen
    const li = document.createElement("li");
    li.textContent = `${vornameWert} ${nachnameWert} (${emailWert})`;
    teilnehmerAnzeige.appendChild(li);

    // Felder leeren
    vorname.value = "";
    nachname.value = "";
    email.value = "";
});

// c) + d) Event absenden, Validierung und Bestätigung
form.addEventListener("submit", function (event) {
    event.preventDefault();

    msg.textContent = "";
    msg.style.color = "red";

    // Veranstaltungsdaten auslesen
    const titelWert = titel.value.trim();
    const datumWert = datum.value;
    const zeitWert = zeit.value;
    const ortWert = ort.value.trim();
    const beschreibungWert = beschreibung.value.trim();

    // Array für Fehlermeldungen bei den Veranstaltungsemelenten
    const errorsEvent = []; 

// c) Validierung aller Felder und mindestens ein Teilnehmer
    if (!titelWert || !datumWert || !zeitWert || !ortWert || !beschreibungWert) {
        errorsEvent.push("Bitte füllen Sie alle Veranstaltungsfelder aus.");
    }

    if (teilnehmerListe.length === 0) {
        errorsEvent.push("Bitte fügen Sie mindestens einen Teilnehmer hinzu.");
    }

    if (errorsEvent.length > 0) {
        msg.innerHTML = errorsEvent.join("<br>");
        return;
    }
// e) Zusätzlich zur Validierung auch noch eine Zusammenfassung mit einem confirm
    let teilnehmerText = "";
    for (const t of teilnehmerListe) {
        teilnehmerText += `
        ${t.vorname} ${t.nachname} (${t.email})\n`;
    }

    const zusammenfassung = `
    Veranstaltung: ${titelWert}
    Datum: ${datumWert}
    Uhrzeit: ${zeitWert}
    Ort: ${ortWert}
    Beschreibung: ${beschreibungWert}

    Teilnehmer:
    ${teilnehmerText}
    `;

    // Abbrechen, wenn Nutzer "Nein" klickt
    if (!confirm(zusammenfassung + "\n\nMöchten Sie die Einladungen versenden?")) {
        return; 
    }

    msg.style.color = "green";
    msg.textContent = "Einladungen wurden erfolgreich versendet!";

    form.reset(); // Anstelle des Reset könnte auch ein versenden des Formulars stattfinden
    teilnehmerListe = [];
    teilnehmerAnzeige.innerHTML = "";
    dauerAnzeige.textContent = "";
});