/* Entwickle eine Webanwendung, die Nutzereingaben über ein Formular entgegennimmt, 
um eine personalisierte Begrüßung basierend auf der aktuellen Uhrzeit und dem Namen des Nutzers zu generieren. 
Die Anwendung soll außerdem die Fähigkeit haben, Daten von einer externen API zu beziehen 
und diese Daten abhängig von der Nutzereingabe zu filtern. 
Verwende die Fetch-API und async/await für asynchrone Anfragen an eine Test-API, 
um eine Liste von Aufgaben zu erhalten. 
Die Anwendung soll folgende Funktionalitäten aufweisen:  

a) Erstelle ein HTML-Formular mit einem Textfeld für den Namen des Nutzers und einem Submit-Button. 
Binde ein Event an den Submit-Button, das die Eingaben verarbeitet, ohne die Seite neu zu laden. 

b) Implementiere eine Funktion, die eine personalisierte Begrüßung in einem <div>-Element auf der Seite anzeigt. 
Die Begrüßung soll "Guten Morgen, [Name]!" von 5:00 bis 11:59, "Guten Tag, [Name]!" von 12:00 bis 17:59 
und "Guten Abend, [Name]!" von 18:00 bis 4:59 ausgeben. 

c) Verwende die Fetch-API und async/await, um eine Liste von Aufgaben von der Test-API 
https://jsonplaceholder.typicode.com/todos zu beziehen. Zeige die ersten fünf Aufgaben in einer Liste auf der Seite an. 

d) Erweitere die Anwendung, sodass der Nutzer eine Zahl zwischen 1 und 200 eingeben kann, 
um eine spezifische Aufgabe aus der Liste der abgerufenen Aufgaben anzuzeigen. 
Verarbeite diese Eingabe im selben Formular wie den Namen. */

//a) Formular und Event Listener
const nameInput = document.getElementById("nameInput");
const taskInput = document.getElementById("taskInput");
const greetButton = document.getElementById("greetButton");
const greetingResult = document.getElementById("greetingResult");
const taskList = document.getElementById("taskList");
const specificTaskResult = document.getElementById("specificTaskResult");

// Event Listener für Klick auf Button
greetButton.addEventListener("click", async (event) => {
  event.preventDefault(); // warten mit Verarbeitung bis Klick
  const name = nameInput.value.trim(); // Name aus Input holen

  if (!name) {
    greetingResult.textContent = "Bitte einen Namen eingeben.";
    return;
  }

  displayGreeting(name);  // Begrüßung anzeigen

  // c) Aufgaben von API holen und anzeigen
  const tasks = await fetchTasks(); // Daten von der API abrufen
  displayTasks(tasks); // erste 5 Aufgaben anzeigen

  // d) Spezifische Aufgabe anzeigen
  const taskNumber = parseInt(taskInput.value.trim());
  if (!isNaN(taskNumber) && taskNumber >= 1 && taskNumber <= tasks.length) {
    const task = tasks[taskNumber - 1]; // Array ist 0-basiert
    specificTaskResult.textContent = `Aufgabe #${taskNumber}: ${task.title}`;
  } else if (taskInput.value.trim() !== "") {
    specificTaskResult.textContent = "Bitte eine Zahl zwischen 1 und 200 eingeben.";
  } else {
    specificTaskResult.textContent = ""; // leer lassen, wenn keine Zahl eingegeben
  }
});

//b) Begrüßungsfunktion
function displayGreeting(name) {
  const now = new Date();
  const hours = now.getHours();
  let greeting;
  if (hours >= 5 && hours < 12) {
    greeting = `Guten Morgen, ${name}!`;
  } else if (hours >= 12 && hours < 18) {
    greeting = `Guten Tag, ${name}!`;
  } else {
    greeting = `Guten Abend, ${name}!`;
  }
  greetingResult.textContent = greeting; // zeigt die Begrüßung im <div> an
}

// c) Fetch-API und async/await für Aufgaben
async function fetchTasks() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos");

    if (!response.ok) { // hier kann ich explizit auf HTTP Fehler reagieren
      throw new Error("Fehler beim Abrufen der Aufgaben"); // wenn !response.ok true ist, wird eine Exception geworfen (throw)
    }

    const data = await response.json(); // Daten aus Response extrahieren
    return data;

  } catch (error) {
    console.error("Fehler beim Abrufen der Aufgaben:", error);
    return []; // leeres Array zurückgeben bei Fehler
  }
}

// c) Aufgaben anzeigen
function displayTasks(tasks) {
  taskList.innerHTML = ""; // Alte Aufgaben löschen

  tasks.slice(0, 5).forEach(task => {
    const li = document.createElement("li");
    li.textContent = task.title; // Titel der Aufgabe
    taskList.appendChild(li);
  });
}

// Enter-Taste im Name-Input und Task-Input abfangen
nameInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") greetButton.click();
});
taskInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") greetButton.click();
});
