/* Programmiere eine Funktion, die ein Element über seinen Index entfernt, also 
z.B. das zweite und dritte Element. 




*/
// document.querySelectorAll('main img'); // alle img-Elemente unterhalb von main
const blumen = document.querySelectorAll(".blumen li"); // alle li Elemente unterhalb von .blumen
console.log(blumen);
console.log(blumen[0].innerText); // Rosen
console.log(blumen[1].innerText); // Kakteen
console.log(blumen[2].innerText); // Orchideen
const Kakteen = blumen[1].innerText;
const Orchideen = blumen[2].innerText;
blumen[2].remove(); // man muss vo hinten nach vorne löschen, wegen der index verschiebung.
blumen[1].remove();

const aktuelleBlumen = document.querySelectorAll(".blumen li");
console.log(aktuelleBlumen);
aktuelleBlumen.forEach(li => console.log(li.innerText));

/* lösung....
Aufgabe von ../../dom-replace-remove.html

Lösung
 Rosen  Kakteen  Orchideen  Hortensien  Tulpen
<input type="radio" value="Rosen" name="blumen"> Rosen
<input type="radio" value="Kakteen" name="blumen"> Kakteen
<input type="radio" value="Orchideen" name="blumen"> Orchideen
<input type="radio" value="Hortensien" name="blumen"> Hortensien
<input type="radio" value="Tulpen" name="blumen"> Tulpen
Hinweis: Die Lösung ist trickreich, denn die Eingabefelder bestehen aus Element-Knoten und Text-Knoten. Um ein Feld zu löschen, müssen sowohl das input-Element als auch der nachfolgende Text gelöscht werden.

Die Lösung nutzt das div-Element mit der CSS-Klasse »auswahl« und sammelt mit der Eigenschaft children die input-Elemente in einer HTMLCollection.

del.nextSibling.remove() löscht den Text, erst dann löscht del.remove() das input-Element selbst.

function removeElement(index) {
   const buttons = document.querySelector('.realauswahl').children;
   const del = buttons [index];
   del.nextSibling.remove();
   del.remove();
}

removeElement(2);
removeElement(3);
 Rosen  Kakteen  Hortensien */