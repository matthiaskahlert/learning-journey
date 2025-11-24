function markiere(el) {
    el.style.background = "yellow";
}
/* this zeigt auf den Button.

markiere(this) ruft die Funktion auf und übergibt den Button.

el.style.background färbt genau diesen Button gelb. */
const img = document.querySelector(".zoomit"); // holt das img Element mit der Klasse zoomit

img.onmouseover = function() { // wenn der mauszeiger das element betritt - css macht transform: scale(2) - bild zoomt hinein
this.classList.add("zoomIn");
}
img.onmouseout = function() { // mauszeiger verlässt das element - bild zoomt wieder heraus
this.classList.remove("zoomIn")
}
img.ontouchend = function() {
console.log("Jetzt ist Schluss!");
this.classList.toggle("zoomIn");
}
// folgend die button farbänderung per click, also das callback function beispiel:
const color = document.querySelector(".color");
  const klick = document.querySelector("#klick");

  function changeColor(evt) {
    // Toggle am Element, das geklickt wurde
    evt.target.classList.toggle("dark");
    // Toggle am div mit der Klasse "color"
    color.classList.toggle("black");
  }

  // Callback-Funktion als Argument
  klick.addEventListener("click", changeColor);

  // EventHandler reagiert auf Grupe von Elementen
  const input = document.querySelectorAll(".feld");
/*   input.forEach((elem) =>  {
    elem.addEventListener("blur",()=>{ // blur bedeutet: Das Input-Feld verliert den Fokus (z. B. man klickt heraus oder tabbt weiter).
        elem.closest("label").append(elem.value); // elem.closest("label") sucht das nächstgelegene <label> um das Input herum..append(elem.value) hängt den eingegebenen Text als reinen Textknoten hinter das Label
    })
  })
 */


function blurField(evt) {
  evt.target.closest("label").append(evt.target.value);
}

input.forEach((elem) => {
  elem.addEventListener("blur", blurField);
});
input[2].removeEventListener("blur", blurField) // entfernt den eventlistener für den dritten input
input[2].remove(); // entfernt das element aus dem DOM

const elem = document.querySelector("#meinDiv");


const ausgabe = document.querySelector("#anzeige");

function coords(evt) {
  // evt.offsetX/Y = Position relativ zum Element
  ausgabe.textContent = `${evt.offsetX}, ${evt.offsetY}`;
}

elem.addEventListener("mousemove", coords);
textfld.addEventListener("keydown", evt => {
    console.log("keydown");
});

const textfld2 = document.querySelector("#textfld");
textfld2.addEventListener("keypress", evt => {
    console.log("keypress");
    console.log("key", evt.key);
    console.log("keyCode", evt.keyCode);
    console.log("code", evt.code);
});
textfld.addEventListener("keyup", evt => {
    console.log("keyup");
});
// folgendes snippet ist die Basis für jede Enter-Interaktion in einem Input-Feld, z.B.:
// Suche starten
// Formular absenden
// Filter oder Aktionen auslösen

const search = document.querySelector("#search");
search.addEventListener("keypress", (evt) => {
if (evt.keyCode === 13) { // keycode wurde dem console log entnommen von textfld2

console. log("keypressed enter"); // keypressed enter
}});

const input2 = document.querySelector("#inputField");
const ouput = document.querySelector("#output");

input2.addEventListener("keydown", function(evt){
    let info =` 
    key: ${evt.key} <br>
    keyCode: ${evt.keyCode} <br>
    code: ${evt.code} <br>
`;
    info += `Shift gedrückt: ${evt.shiftKey} <br>`;
    info += `Ctrl gedrückt: ${evt.ctrlKey} <br>`;
    info += `Alt gedrückt: ${evt.altKey} <br>`;
output.innerHTML = info;

});

// klassisches kontaktformular:
const form = document.querySelector("#myform");

// Validierungsfunktionen
function checkName() {
    const val = document.querySelector("#reqname").value.trim();
    const emsg = document.querySelector("#errName");
    if (!/^[\u00c0-\u01ffa-zA-Z.'-]{3,}$/.test(val)) {
        emsg.innerText = "Der Name muss mindestens drei Zeichen lang sein.";
        return false;
    }
    emsg.innerText = "";
    return true;
}

function checkEmail() {
    const val = document.querySelector("#reqemail").value.trim();
    const emsg = document.querySelector("#errEmail");
    if (!/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i.test(val)) {
        emsg.innerText = "Bitte prüfen Sie die E-Mail-Adresse!";
        return false;
    }
    emsg.innerText = "";
    return true;
}

function checkPhone() {
    const val = document.querySelector("#reqphone").value.trim();
    const emsg = document.querySelector("#errPhone");
    if (!/^(?:\+49|0)\d[\d\s()./-]{6,}$/.test(val)) {
        emsg.innerText = "Bitte prüfen Sie die Telefonnummer!";
        return false;
    }
    emsg.innerText = "";
    return true;
}

function checkText() {
    const val = document.querySelector("#reqtext").value.trim();
    const emsg = document.querySelector("#errText");
    if (!/^.{30,}$/.test(val)) {
        emsg.innerText = "Bitte erklären Sie Ihr Anliegen kurz, aber mindestens mit 30 Zeichen.";
        return false;
    }
    emsg.innerText = "";
    return true;
}

// Blur Events für alle Felder
document.querySelector("#reqname").addEventListener("blur", checkName);
document.querySelector("#reqemail").addEventListener("blur", checkEmail);
document.querySelector("#reqphone").addEventListener("blur", checkPhone);
document.querySelector("#reqtext").addEventListener("blur", checkText);

// Submit Event für finale Prüfung
form.addEventListener("submit", function(evt) {
    evt.preventDefault();
    let valid = checkName() && checkEmail() && checkPhone() && checkText();
    if (valid) form.submit();
});
