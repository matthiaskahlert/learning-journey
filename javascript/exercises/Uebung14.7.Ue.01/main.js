/* Entwickle ein kleines JavaScript-Programm, das die folgenden Anforderungen erfüllt: 
Du erstellst eine Webseite, die beim Laden überprüft, ob im Local Storage unter dem Schlüssel "besucherZaehler" 
bereits ein Wert gespeichert ist. Falls ja, soll dieser Wert um 1 erhöht und zurück in den Local Storage geschrieben werden. 
Falls nein, soll der Wert auf 1 gesetzt und im Local Storage gespeichert werden. 
Anschließend soll der aktualisierte Besucherzähler auf der Webseite angezeigt werden. 
Zusätzlich soll die Webseite eine Nachricht anzeigen, die sich ändert, je nachdem, 
ob es der erste Besuch des Nutzers ist oder nicht. 
Verwende für die Umsetzung if-else-Anweisungen, Schleifen, und arbeite mit dem Window-Objekt, 
um auf den Local Storage zuzugreifen. 
Implementiere außerdem eine einfache Animation für die Anzeige des Besucherzählers unter Verwendung der Web Animations API.    */


// Funktion wird ausgeführt, sobald die Seite geladen ist
window.onload = function() {

    // a) Besucherzähler aus dem Local Storage abrufen
    let besucherZaehler = window.localStorage.getItem("besucherZaehler");

    // b) Prüfen: existiert der Wert?
    if (besucherZaehler) {
        // Umwandeln in Zahl
        besucherZaehler = Number(besucherZaehler) + 1;
    } else {
        // Erster Besuch
        besucherZaehler = 1;
    }

    // c) Zurück in den Local Storage schreiben
    window.localStorage.setItem("besucherZaehler", besucherZaehler);

    // d) Ausgabe in der HTML-Seite
    const counterBox = document.getElementById("counterBox");
    counterBox.textContent = `Besuche: ${besucherZaehler}`;

    const message = document.getElementById("message");

    // e) Nachricht abhängig vom Besuch anzeigen
    if (besucherZaehler === 1) {
        message.textContent = "Willkommen! Dies ist dein erster Besuch.";
    } else {
        message.textContent = "Schön, dass du wieder da bist!";
    }

    // f) Animation für den Besucherzähler (Wird größer rein-animiert)
    counterBox.animate(
        [
            { transform: "scale(0.5)", opacity: 0 },
            { transform: "scale(1)", opacity: 1 }
        ],
        {
            duration: 800,
            easing: "ease-out",
            fill: "forwards"
        }
    );

};