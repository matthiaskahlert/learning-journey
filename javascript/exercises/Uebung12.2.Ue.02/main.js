/* Erstelle ein JavaScript-Programm, das ein einfaches Formular zur Erfassung von Benutzerfeedback nutzt. 
Das Formular soll Felder für 
den Namen des Benutzers, 
eine E-Mail-Adresse, 
eine Auswahl für die Zufriedenheit (zufrieden, neutral, unzufrieden) über Radiobuttons 
und ein Textfeld für Kommentare enthalten. Dein Programm soll folgende Funktionalitäten umfassen: 

a) Überprüfe beim Absenden des Formulars, ob alle Felder ausgefüllt wurden. 
Falls ein Feld leer ist, zeige eine entsprechende Fehlermeldung an und verhindere das Absenden des Formulars. 

b) Überprüfe die Gültigkeit der E-Mail-Adresse (einfache Überprüfung, ob ein "@" enthalten ist). 

c) Gib eine Bestätigungsnachricht aus, wenn das Formular erfolgreich abgeschickt wurde, ohne die Seite neu zu laden. 

d) Speichere die Eingaben in einem Objekt und gib dieses Objekt in der Konsole aus. */

const form = document.querySelector("#feedbackForm");
const msg  = document.querySelector("#msg");

form.addEventListener("submit", function (e) {
  e.preventDefault(); // verhindert Seiten-Neuladung

  msg.style.color = "red";
  msg.textContent = "";

  const name = document.querySelector("#name").value.trim();
  const email = document.querySelector("#email").value.trim();
  const kommentar = document.querySelector("#kommentar").value.trim();
  const zufriedenheit = document.querySelector("input[name='zufriedenheit']:checked");

  // a) Alle Felder ausgefüllt?
  if (name === "" || email === "" || kommentar === "" || !zufriedenheit) {
    msg.textContent = "Bitte füllen Sie alle Felder vollständig aus.";
    return;
  }

  // b) Einfache E-Mail-Überprüfung
  if (!email.includes("@")) {
    msg.textContent = "Bitte geben Sie eine gültige E-Mail-Adresse ein.";
    return;
  }

  // d) Objekt mit allen Eingaben erstellen
  const feedbackObjekt = {
    name: name,
    email: email,
    zufriedenheit: zufriedenheit.value,
    kommentar: kommentar
  };

  console.log("Feedback gesendet:", feedbackObjekt);

  // c) Erfolgsnachricht ausgeben
  msg.style.color = "green";
  msg.textContent = "Vielen Dank für Dein Feedback!";

  // Formular zurücksetzen
  form.reset();
});
