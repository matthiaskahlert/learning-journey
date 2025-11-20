/* Entwickle eine kleine Webanwendung, die eine dynamische Benutzeroberfläche zur Verwaltung einer ToDo-Liste ermöglicht. Die Anwendung soll folgende Funktionalitäten bieten: 

a) Ein Textfeld und einen Button, um neue ToDo-Elemente zur Liste hinzuzufügen. Jedes ToDo-Element soll als Objekt in einem Array gespeichert werden. Jedes Objekt enthält zwei Eigenschaften: id (eindeutige Identifikationsnummer) und text (der Text des ToDo-Elements). 

b) Eine Darstellung der ToDo-Liste im DOM, wobei jedes Element der Liste ein li-Element innerhalb eines ul-Elements ist. Verwende document.createElement und appendChild, um die li-Elemente dynamisch zu erstellen und ins DOM einzufügen. 

c) Die Möglichkeit, ein ToDo-Element aus der Liste zu entfernen, indem ein "Löschen"-Button neben jedem ToDo-Element angezeigt wird. Beim Klicken auf den "Löschen"-Button soll das entsprechende li-Element aus dem DOM entfernt und das Objekt aus dem Array gelöscht werden. 

d) Eine Funktion, die die Hintergrundfarbe der li-Elemente abwechselnd setzt, um eine gestreifte Liste zu erzeugen. Verwende CSS-Klassen und ändere die Klassen der li-Elemente, sobald ein neues Element hinzugefügt oder ein Element entfernt wird.   */



const container = document.querySelector("#todo-container");
const todos = []; // zur speicherung von ToDo Elementen als Objekt wie { id: 1, text: "Einkaufen"}
const input = document.querySelector("#todo-input");
const button = document.querySelector("#add-button");
const todoList = document.querySelector("#todo-list");
let aktuelleId = 0;


const addTodo = () => {
    const wert = input.value;
    console.log(wert);
    if (wert.trim() === ""){
        console.log("Todo war leer! Bitte etwas eingeben!");
        return;
    } else {
        const neueId = ++aktuelleId;
        todos.push({ id: neueId, text: wert });
        const li = document.createElement("li");
        li.innerText = `id ${neueId}, 
        text: "${wert}" `;
        li.dataset.id = neueId;
        todoList.appendChild(li);

        const loeschenButton = document.createElement("button");
        loeschenButton.innerText = "Löschen";
        li.appendChild(loeschenButton);
        loeschenButton.addEventListener("click", () => {
            // Li aus der Liste entfernen
            todoList.removeChild(li);

            // Objekt aus dem Array löschen
            const index = todos.findIndex(todo => todo.id == li.dataset.id);
            if (index !== -1) { // Wenn kein passendes Element gefunden wird → gibt es -1 zurück.
                todos.splice(index, 1);
            }
        
            // Farben neu setzen
            aktualisiereHintergrundfarben();

        });
        aktualisiereHintergrundfarben();
        input.value = "" // text entfernen von vorherigen eingaben
    }
}
button.addEventListener("click", addTodo);
input.addEventListener("keydown", (e)=>{
    if(e.key==="Enter"){
        addTodo();
    }
});
const aktualisiereHintergrundfarben = () => {
    const listenelemente = todoList.querySelectorAll("li");
    listenelemente.forEach((li, index) => {
        li.classList.remove("gerade", "ungerade");
        if (index % 2 === 0) {
            li.classList.add("gerade");
        } else {
            li.classList.add("ungerade");
        }
    });
};




