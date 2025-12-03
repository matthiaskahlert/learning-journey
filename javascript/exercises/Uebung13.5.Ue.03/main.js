/* Entwickle eine kleine Webanwendung, die Nutzereingaben aus einem Formular verwendet, 
um eine Liste von Aufgaben zu verwalten. Die Anwendung soll folgende Funktionen umfassen: 

a) Ein Formular, in dem der Nutzer eine neue Aufgabe beschreiben 
und eine Priorität (hoch, mittel, niedrig) auswählen kann. 
Nach dem Abschicken des Formulars soll die Aufgabe in einem Array gespeichert werden. 
Jede Aufgabe ist ein Objekt mit den Eigenschaften beschreibung und priorität. 

b) Eine Funktion, die das Array von Aufgaben durchläuft 
und diese sortiert nach Priorität (hoch > mittel > niedrig) in der Konsole ausgibt. 
Verwende dabei eine if-else-Struktur, um die Priorität zu überprüfen. 

c) Eine Schaltfläche "Aufgaben anzeigen", die bei Klick die oben genannte Funktion ausführt. 

d) Implementiere eine einfache Validierung für das Formular, die überprüft, 
ob die Eingabe der Aufgabenbeschreibung nicht leer ist. 
Falls das Eingabefeld leer ist, soll eine entsprechende Nachricht angezeigt 
werden und das Abschicken verhindert werden. 

e) Verwende die Fetch-API, um eine GET-Anfrage an https://jsonplaceholder.typicode.com/posts/1 zu senden, 
sobald das Formular erfolgreich abgeschickt wurde. Logge die Antwort in der Konsole. */

// --- HTML-Elemente holen ---
const form = document.getElementById("taskForm");
const taskInput = document.getElementById("taskName");
const prioInput = document.getElementById("prio");

// --- Aufgaben werden in diesem Array gespeichert ---
let aufgaben = [];
form.addEventListener("submit", async (event) => {
    event.preventDefault(); // verhindert Neuladen der Seite

    const beschreibung = taskInput.value.trim();
    const priorität = prioInput.value;


    const neueAufgabe = {
        beschreibung: beschreibung,
        priorität: priorität
    };

    if (beschreibung === "") {
        alert("Bitte eine Aufgabenbeschreibung eingeben!");
        return; // Code danach wird nicht ausgeführt
    }

    if (priorität === "") {
        alert("Bitte eine Priorität auswählen!");
        prioInput.focus();
        return;
    }

    aufgaben.push(neueAufgabe);
    console.log("Aufgabe gespeichert:", neueAufgabe);
    console.log("Aktuelles Aufgaben-Array:", aufgaben);
    form.reset();

    // --- (e) Fetch-API Anfrage ---
try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts/1", {
        method: "GET"});

    // Prüfen, ob die Antwort OK war (status 200–299)
    if (!response.ok) {
        throw new Error("Server-Fehler: " + response.status);
    }

    const data = await response.json(); // Antwort als JSON auslesen
    console.log("Fetch-Daten:", data);

} catch (error) {
    console.error("Fetch-Fehler:", error);
}

});





document.getElementById("showTasksBtn").addEventListener("click", () => {
    aufgabenAusgeben();
});
function aufgabenAusgeben() {
    const listEl = document.getElementById("taskList");
    listEl.innerHTML = ""; // alte Einträge löschen

    // sortieren
    const sortiert = [...aufgaben].sort((a, b) => {
        const order = { hoch: 1, mittel: 2, niedrig: 3 };
        return order[a.priorität] - order[b.priorität];
    });

    // Aufgaben durchlaufen und ausgeben
    for (const k of sortiert) {
        let li = document.createElement("li");

        if (k.priorität === "hoch") {
            console.log("Hohe Priorität:", k.beschreibung);
            li.textContent = "Hohe Priorität: " + k.beschreibung;

        } else if (k.priorität === "mittel") {
            console.log("Mittlere Priorität:", k.beschreibung);
            li.textContent = "Mittlere Priorität: " + k.beschreibung;

        } else {
            console.log("Niedrige Priorität:", k.beschreibung);
            li.textContent = "Niedrige Priorität: " + k.beschreibung;
        }

        listEl.appendChild(li);
    }
}


