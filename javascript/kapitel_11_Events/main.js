function markiere(el) {
    el.style.background = "yellow";
}
/* this zeigt auf den Button.

markiere(this) ruft die Funktion auf und übergibt den Button.

el.style.background färbt genau diesen Button gelb. */
const img = document.querySelector(".zoomit"); // holt das img Element mit der Klasse zoomit

img.onmouseover = function() { // wenn der mauszeiger das element betritt . css macht transform: scale(2) - bild zoomt hinein
this.classList.add("zoomIn");
}
img.onmouseout = function() { // mauszeiger verlässt das element . bild zoomt wieder heraus
this.classList.remove("zoomIn")
}
img.ontouchend = function() {
console.log("Jetzt ist Schluss!");
this.classList.toggle("zoomIn");
}