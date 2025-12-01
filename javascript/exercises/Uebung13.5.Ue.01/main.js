/* Aufgabe: Asynchrones JavaScript 

Entwickle eine kleine Webanwendung, die das aktuelle Datum und die Uhrzeit anzeigt 
und es dem Benutzer ermöglicht, 
eine Erinnerung für ein zukünftiges Datum und eine Uhrzeit zu setzen. 
Sobald die festgelegte Zeit erreicht ist, soll eine Benachrichtigung auf der Webseite erscheinen, 
die den Benutzer an sein Ereignis erinnert. 
Verwende dabei die Fetch-API, um eine API für die aktuelle Uhrzeit zu nutzen und async/await für die asynchrone Programmierung. 
Die Erinnerung und die Benachrichtigung sollen ohne Neuladen der Seite funktionieren. 

a) Richte eine HTML-Seite ein, die ein Formular enthält. 
Das Formular soll Felder für die Eingabe eines Ereignisnamens, eines Datums und einer Uhrzeit enthalten. 
Füge zudem einen Button hinzu, um die Erinnerung zu setzen.  

b) Verwende JavaScript, um das aktuelle Datum 
und die Uhrzeit von einer API wie http://worldtimeapi.org/api/timezone/Europe/Berlin zu ziehen. 
Zeige diese Informationen auf der Webseite an. 

c) Implementiere eine Funktion, die das Formular überwacht und bei der Einreichung eine Erinnerung erstellt. 
Speichere die Erinnerungen in einem Array. 

d) Setze einen Timer, der jede Minute überprüft, ob die Zeit für eine der gesetzten Erinnerungen erreicht wurde. 
Zeige eine Benachrichtigung auf der Webseite an, wenn die Zeit für eine Erinnerung gekommen ist. 

e) Verwende die Fetch-API und async/await, um die aktuelle Uhrzeit asynchron zu laden 
und die Seite bei der Anzeige der aktuellen Uhrzeit oder einer Erinnerung nicht neu zu laden. */

// Alle Erinnerungen werden hier gespeichert
let reminders = [];

// --- a) aktuelle Zeit aus API laden ---
async function loadTime() {
  const response = await fetch("https://worldtimeapi.org/api/timezone/Europe/Berlin");
  const data = await response.json();

  // Uhrzeit zeigen
  document.querySelector("#currentTime").textContent = data.datetime;

  return new Date(data.datetime); // als echtes Date-Objekt zurückgeben
}

// alle 10 Sekunden die Uhrzeit aktualisieren
setInterval(loadTime, 10000);
loadTime();

// --- b) Formular überwachen ---
const form = document.querySelector("#reminderForm");
form.addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.querySelector("#eventName").value;
  const date = document.querySelector("#eventDate").value;
  const time = document.querySelector("#eventTime").value;

  const datetimeString = `${date}T${time}:00`;
  const reminderDate = new Date(datetimeString);

  reminders.push({
    name: name,
    time: reminderDate
  });

  showReminders();
  form.reset();
});

// Erinnerungsliste anzeigen
function showReminders() {
  const list = document.querySelector("#reminderList");
  list.innerHTML = "";

  reminders.forEach(rem => {
    const li = document.createElement("li");
    li.textContent = `${rem.name} – ${rem.time.toLocaleString()}`;
    list.appendChild(li);
  });
}

// --- d) jede Minute prüfen, ob eine Erinnerung fällig ist ---
setInterval(checkReminders, 60000);

async function checkReminders() {
  const now = await loadTime(); // aktuelle Zeit fresh aus API

  reminders.forEach((rem, index) => {
    if (now >= rem.time) {
      notify(rem.name);
      reminders.splice(index, 1);
      showReminders();
    }
  });
}

// Benachrichtigung ausgeben
function notify(text) {
  const box = document.querySelector("#notifications");
  const msg = document.createElement("div");
  msg.textContent = `🔔 Erinnerung: ${text}`;
  msg.style.margin = "10px 0";
  msg.style.padding = "5px";
  msg.style.background = "#ffe4a6";
  box.appendChild(msg);
}
