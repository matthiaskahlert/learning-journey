/* const filme = [  { titel: "Inception", jahr: 2010, genre: "Sci-Fi", bewertung: "9/10" },
  { titel: "Matrix", jahr: 1999, genre: "Action", bewertung: "8.5/10" }];

  console.log(filme[0]);
  console.log(filme[0].titel);
  for (const film of filme) {
    console.log(`${film.titel} (${film.jahr}) - ${film.bewertung}`);
  }

Was du hier lernst:

Arrays können Objekte enthalten.

Auf einzelne Objekte greifst du mit [index] zu.

Auf Eigenschaften im Objekt mit objekt.eigenschaft.

Mit einer for...of-Schleife kannst du alle Objekte durchlaufen */

function zeigeFilme(filmListe){
    for (const film of filmListe) {
        console.log(`${film.titel} (${film.jahr}) - ${film.genre}`);
    }
}
const meineFilme = [
  { titel: "Interstellar", jahr: 2014, genre: "Sci-Fi", bewertung: "9/10" },
  { titel: "Tenet", jahr: 2020, genre: "Action", bewertung: "8/10" }
];

zeigeFilme(meineFilme);