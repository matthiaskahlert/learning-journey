/* Entwickle ein JavaScript-Programm, das auf Tastatureingaben reagiert, 
um die Anzahl der Buchstaben, die Anzahl der Wörter und die Häufigkeit jedes Buchstabens in einem Text zu analysieren. 
Der Text soll durch Eingabe des Benutzers über die Tastatur in ein Textfeld auf einer Webseite eingegeben werden. 
Sobald der Benutzer die Eingabetaste (Enter) drückt, soll die Analyse durchgeführt und das Ergebnis auf der Webseite angezeigt werden.  

Folge diesen Schritten: 

a) Erstelle eine HTML-Seite mit einem Textfeld für die Eingabe und einem Bereich, in dem die Ergebnisse angezeigt werden. 

b) Schreibe eine JavaScript-Funktion, die bei Betätigung der Eingabetaste (Enter) die Analyse startet. 
Diese Funktion soll die Anzahl der Buchstaben, die Anzahl der Wörter und die Häufigkeit jedes Buchstabens (ignoriere Groß- und Kleinschreibung) in dem eingegebenen Text berechnen. 

c) Zeige die Ergebnisse unterhalb des Eingabefeldes an. Stelle sicher, dass die Ergebnisse übersichtlich präsentiert werden.  */


const textArea = document.querySelector("#textAnalyse");
const resultDiv = document.querySelector("#analyseErgebnis");

// folgendes snippet ist die Basis für eine Enter-Interaktion in dem Input-Feld, um das Formular abzusenden


textArea.addEventListener("keydown", (evt) => {
    if (evt.key === "Enter") {
        evt.preventDefault(); // verhindert neue Zeile
        const text = textArea.value;
        analyzeText(text);
    }
});

function analyzeText(text) {
    const letterCount = text.replace(/[^a-zA-Z0-9äöüÄÖÜß]/g, "").length; // Anzahl der Buchstaben, über trim() und length
    const wordCount = text.trim().split(/\s+/).length;  //die Anzahl der Wörter über split(" ") und length

    const letterFrequency = {}; //die Häufigkeit jedes Buchstabens über ein Objekt, in dem die Buchstaben als Schlüssel und die Häufigkeit als Wert gespeichert werden.
    for (const char of text.toLowerCase()) {
        if (char.match(/[a-z0-9äöüß]/)) {
            letterFrequency[char] = (letterFrequency[char] || 0) + 1;
        }
    }
    // Ergebnis übersichtlich anzeigen
    resultDiv.innerHTML = `
        <p><strong>Buchstaben insgesamt:</strong> ${letterCount}</p>
        <p><strong>Wörter insgesamt:</strong> ${wordCount}</p>
        <p><strong>Buchstabenhäufigkeit:</strong></p>
        <ul>
            ${Object.entries(letterFrequency).map(([letter, count]) => `<li>${letter}: ${count}</li>`).join('')}
        </ul>
    `;
}




