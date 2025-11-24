/* Übertrage die x- und y-Position des Mauszeigers bei jeder Bewegung in die weißen Felder und bewege den blauen Kreis bei einem Klick auf die Position der
Maus.
 */

const wrapper = document.querySelector(".wrapper");
const mouseX = document.querySelector(".mouseX");
const mouseY = document.querySelector(".mouseY");
const pixel = document.querySelector(".pixel");
const clickList = document.querySelector("#clickList");

wrapper.addEventListener("mousemove", function(evt) {
    mouseX.textContent = evt.offsetX;
    mouseY.textContent = evt.offsetY;
});

wrapper.addEventListener("click", function(evt) {
  pixel.style.left = evt.offsetX + "px"; // Ohne "px" würde der Browser die Zahl nicht als gültige CSS-Angabe erkennen und das Element würde nicht richtig positioniert werden.
  pixel.style.top = evt.offsetY + "px";

const li = document.createElement("li");
li.textContent = `X: ${evt.offsetX}, Y: ${evt.offsetY}`;
clickList.appendChild(li);
});


