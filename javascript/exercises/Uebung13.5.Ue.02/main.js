/* Erstelle eine Webseite, die ein Formular mit einem Texteingabefeld und einem Button enthält. 
Das Texteingabefeld soll vom Benutzer genutzt werden, um eine Stadt einzugeben. 
Beim Klicken auf den Button soll eine asynchrone Anfrage an die OpenWeatherMap API gesendet werden, 
um die aktuelle Temperatur in der eingegebenen Stadt zu erhalten. 
Die Temperatur soll anschließend auf der Webseite angezeigt werden. 
Verwende async/await für die asynchrone Anfrage. 
Sorge auch dafür, dass die Anwendung auf mögliche Fehler, wie eine falsche Stadteingabe 
oder Probleme mit der Netzwerkverbindung, angemessen reagiert und dem Benutzer eine entsprechende Meldung anzeigt. */
async function getTemperature(city) {
  try {
    const geoResponse = await fetch(
      `https://geocoding-api.open-meteo.com/v1/search?name=${city}`
    );
    const geoData = await geoResponse.json();
    if (!geoData.results || geoData.results.length === 0) {
      throw new Error("Stadt nicht gefunden");
    }
    const { latitude, longitude } = geoData.results[0];

    const weatherResponse = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m`
    );
    const weatherData = await weatherResponse.json();
    return weatherData.current.temperature_2m;
  } catch (error) {
    throw error;
  }
}



const input = document.getElementById("cityInput");
const button = document.getElementById("getTempButton");
const result = document.getElementById("result");

async function handleRequest() {
  const city = input.value.trim();
  if (!city) {
    result.textContent = "Bitte eine Stadt eingeben.";
    return;
  }

  result.textContent = "Lade...";

  try {
    const temp = await getTemperature(city);
    result.textContent = `Die aktuelle Temperatur in ${city} beträgt ${temp}°C.`;
  } catch (err) {
    result.textContent = "Fehler: " + err.message;
  }
}

// Button-Klick
button.addEventListener("click", handleRequest);

// Enter-Taste im Input-Feld
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    handleRequest();
  }
});
