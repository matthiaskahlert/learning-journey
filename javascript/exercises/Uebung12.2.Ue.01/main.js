/* Aufgabe: Formulare
Entwickle ein JavaScript-Programm, das ein einfaches Anmeldeformular für ein Event handhabt. 
Das Formular soll folgende Felder enthalten: Vorname, Nachname, E-Mail-Adresse und eine Auswahl für die Teilnahme an Workshops. 
Jeder Workshop soll durch eine Checkbox repräsentiert werden. 
Es gibt drei Workshops zur Auswahl: "Webentwicklung Grundlagen", "Fortgeschrittene JavaScript-Techniken" und "Einführung in CSS". 
Zusätzlich soll es einen "Anmelden"-Button geben. 
Deine Aufgabe besteht darin, folgende Funktionalitäten zu implementieren: 

a) Überprüfe beim Klick auf den "Anmelden"-Button, ob alle Felder (Vorname, Nachname, E-Mail-Adresse) ausgefüllt wurden. 
Wenn eines der Felder leer ist, zeige eine entsprechende Fehlermeldung an. 

b) Stelle sicher, dass die E-Mail-Adresse ein gültiges Format hat (z.B. enthält "@" und einen Punkt nach dem "@"). 
Wenn das Format ungültig ist, zeige eine Fehlermeldung an. 

c) Überprüfe, ob mindestens ein Workshop ausgewählt wurde. 
Wenn kein Workshop ausgewählt wurde, zeige eine Fehlermeldung an. 

d) Wenn alle Überprüfungen erfolgreich sind, zeige eine Bestätigungsnachricht an, dass die Anmeldung erfolgreich war. 

Verwende für die Implementierung DOM-Manipulation, um auf die Formularelemente zuzugreifen und Event-Listener hinzuzufügen. */

const form = document.querySelector("#eventForm");
const msg = document.querySelector("#msg");

form.addEventListener("submit", function (e) {
  e.preventDefault(); // Verhindert das automatische Absenden

  msg.textContent = ""; // Fehlermeldungen zurücksetzen

  const vorname = document.querySelector("#vorname").value.trim(); // wenn der value leer ist, gibt es eine fehlermeldung
  const nachname = document.querySelector("#nachname").value.trim();
  const email = document.querySelector("#email").value.trim();
  const workshops = document.querySelectorAll("input[name='workshop']:checked");

  // a) Felder dürfen nicht leer sein
  if (vorname === "" || nachname === "" || email === "") {
    msg.textContent = "Bitte füllen Sie alle Felder aus.";
    return;
  }

  // b) E-Mail-Format prüfen
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; //RegEx prüft, ob ein @ vorhanden ist und ein Punkt nach dem @ steht
  if (!emailPattern.test(email)) {
    msg.textContent = "Bitte geben Sie eine gültige E-Mail-Adresse ein.";
    return;
  }

  // c) Mindestens einen Workshop auswählen
  if (workshops.length === 0) { // Wenn length === 0 dann gab keine Auswahl.
    msg.textContent = "Bitte wählen Sie mindestens einen Workshop aus.";
    return;
  }

  // d) Alles ok → Erfolgsmeldung
  msg.style.color = "green";
  msg.textContent = "Anmeldung erfolgreich! Vielen Dank.";

  // Optional: Formular zurücksetzen
  form.reset();
});
