document.getElementById("loginForm").addEventListener("submit", function(e) {
  const user = document.getElementById("usernameLogin").value;

  if (user.length < 3) {
    e.preventDefault(); // Absenden verhindern
    alert("Username muss mindestens 3 Zeichen lang sein.");
  }
});

const plzInput = document.getElementById("plz");
const output   = document.getElementById("output");
const form     = document.getElementById("plzForm");

// Eingaben live anzeigen
plzInput.addEventListener("input", () => {
  output.textContent = "Eingabe: " + plzInput.value;
});

// Form-Validierung
form.addEventListener("submit", (e) => {
  const val = plzInput.value;

  if (!/^\d{5}$/.test(val)) {
    e.preventDefault();
    alert("PLZ muss genau 5 Ziffern enthalten.");
    return;
  }

  // Beispiel: Wert aus Serverantwort wieder ins Feld schreiben
  // plzInput.value = serverAntwort.plz;
});

// Beispiel 3


const inputUsername = document.querySelector("#username");
const ortSelection = document.querySelector("#ort");
const text = document.querySelector("#bemerkung");
const checkbox = document.querySelector("#age");
const radio = document.getElementsByName("choice");

// Eingaben auslesen
function checkInput(evt) {
  console.log(evt.target.value);
}

// Events anhängen
inputUsername.addEventListener("input", checkInput);
ortSelection.addEventListener("input", checkInput);
text.addEventListener("input", checkInput);

