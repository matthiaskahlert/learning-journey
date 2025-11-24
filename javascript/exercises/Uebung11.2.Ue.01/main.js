/* Aufgabe: Events

Erstelle eine JavaScript-Funktion, die ein Array von Objekten, die jeweils einen Namen und eine E-Mail-Adresse enthalten, verarbeitet. Die Funktion soll folgende Aufgaben erfüllen: 

a) Überprüfe für jedes Objekt im Array, ob die E-Mail-Adresse das Format einer gültigen E-Mail hat (einfache Überprüfung auf das Vorhandensein eines "@"-Zeichens). Wenn nicht, füge dem Objekt eine neue Eigenschaft isValid mit dem Wert false hinzu. Wenn doch, setze isValid auf true. 

b) Für jedes Objekt, dessen E-Mail-Adresse gültig ist (isValid ist true), füge einen Event Listener hinzu, der bei einem Klick ein Alert-Fenster mit dem Namen und der E-Mail-Adresse anzeigt. Verwende dazu ein dynamisch erstelltes DOM-Element für jeden gültigen Eintrag (z.B. ein <div>-Element), das den Namen und die E-Mail-Adresse enthält. 

c) Gib das modifizierte Array zurück und stelle sicher, dass alle DOM-Elemente auf der Webseite angezeigt werden.  */
const personArr = [
    { name: "Max Mustermann", email: "max@trashmail.com" },
    { name: "Erika Musterfrau", email: "erika@musterfrau.com" },
    { name: "John Doe", email: "john@doe.de" },
    { name: "Invalid User", email: "invalidemail.com" }
]; 
function checkEmail() {

    const container = document.querySelector("#email-container");
    
    
// iterieren durch array
for (const person of personArr) {
    const regexCheck = /@/;
    const valid = regexCheck.test(person.email);
    if (valid) {
    person.isValid = true;

    const div = document.createElement("div");
    div.textContent = `${person.name} – ${person.email}`;
    container.append(div);
    div.addEventListener("click", () => {
        alert(`${person.name}: ${person.email}`);
    });
} else {
    person.isValid = false;
}
}
return personArr;
}
console.log(checkEmail());