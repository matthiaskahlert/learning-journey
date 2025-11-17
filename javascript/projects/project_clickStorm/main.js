let punkte = [];
let leben = 3;
let score = 0;
let highscore = localStorage.getItem("clickStormHighscore") || 0;
let highscoreName = localStorage.getItem("clickStormHighscoreName") || "Unbekannt";
let pointInterval;
let spawnInterval = 1000; // Startintervall 1 Sekunde

const gameArea = document.getElementById("game-area");
const scoreEl = document.getElementById("score");
const livesEl = document.getElementById("lives");

// Highscore Anzeige erstellen
const highscoreEl = document.createElement("div");
highscoreEl.style.position = "absolute";
highscoreEl.style.top = "10px";
highscoreEl.style.right = "10px";
highscoreEl.style.color = "yellow";
highscoreEl.style.fontSize = "1.2rem";
highscoreEl.innerText = `Highscore: ${highscore} (${highscoreName})`;
gameArea.appendChild(highscoreEl);

// Punkt erstellen
const createRandomPoint = () => {
    const size = Math.floor(Math.random() * 50) + 20;
    const x = Math.floor(Math.random() * (gameArea.clientWidth - size));
    const y = Math.floor(Math.random() * (gameArea.clientHeight - size));
    return { x, y, size };
};

// Punkt anzeigen
const showPoint = point => {
    const div = document.createElement("div");
    div.style.width = div.style.height = point.size + "px";
    div.style.background = "red";
    div.style.borderRadius = "50%";
    div.style.position = "absolute";
    div.style.left = point.x + "px";
    div.style.top = point.y + "px";
    div.classList.add("punkt");
    gameArea.appendChild(div);

    div.addEventListener("click", e => {
        e.stopPropagation();
        score++;
        scoreEl.innerText = score;
        div.remove();

        // Alle 3 Hits schneller machen
        if (score % 3 === 0) {
            spawnInterval = Math.max(200, spawnInterval - 100); // nie unter 200ms
            clearInterval(pointInterval);
            startGame();
        }
    });

    setTimeout(() => {
        if (gameArea.contains(div)) {
            div.remove();
            leben--;
            livesEl.innerText = leben;
            if (leben <= 0) gameOver();
        }
    }, 2000);
};

// Klicks außerhalb der Punkte zählen als Miss
gameArea.addEventListener("click", e => {
    if (!e.target.classList.contains("punkt") && leben > 0) {
        leben--;
        livesEl.innerText = leben;
        if (leben <= 0) gameOver();
    }
});

// Game Over Funktion
const gameOver = () => {
    clearInterval(pointInterval);

    // Alle Punkte entfernen
    document.querySelectorAll(".punkt").forEach(p => p.remove());

    // Spielername abfragen
    let playerName = prompt("GAME OVER! Gib deinen Namen für den Highscore ein:");
    playerName = playerName || "Unbekannt";

    if (score > highscore) {
        highscore = score;
        highscoreName = playerName;
        localStorage.setItem("clickStormHighscore", highscore);
        localStorage.setItem("clickStormHighscoreName", highscoreName);
    }

    highscoreEl.innerText = `Highscore: ${highscore} (${highscoreName})`;

    // Overlay erstellen
    const overlay = document.createElement("div");
    overlay.id = "game-over-overlay";
    overlay.style.position = "absolute";
    overlay.style.top = "50%";
    overlay.style.left = "50%";
    overlay.style.transform = "translate(-50%, -50%)";
    overlay.style.textAlign = "center";
    overlay.style.color = "white";
    overlay.style.fontSize = "2rem";
    overlay.style.fontWeight = "bold";
    overlay.style.background = "rgba(0,0,0,0.8)";
    overlay.style.padding = "2rem";
    overlay.style.borderRadius = "10px";

    overlay.innerHTML = `
        GAME OVER<br>
        Punkte: ${score}<br>
        Highscore: ${highscore} (${highscoreName})<br><br>
        <button id="restartBtn" style="font-size:1.2rem;padding:0.5rem 1rem;">Neustarten</button>
    `;

    gameArea.appendChild(overlay);

    // Neustart-Button Event
    document.getElementById("restartBtn").addEventListener("click", () => {
        overlay.remove();
        restartGame();
    });
};

// Spiel zurücksetzen
const restartGame = () => {
    punkte = [];
    score = 0;
    leben = 3;
    spawnInterval = 1000;
    scoreEl.innerText = score;
    livesEl.innerText = leben;
    startGame();
};

// Punkte generieren
const startGame = () => {
    pointInterval = setInterval(() => {
        if (leben <= 0) return;
        const punkt = createRandomPoint();
        showPoint(punkt);
    }, spawnInterval);
};

// Spiel starten
startGame();
