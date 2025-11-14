/* Erstelle ein JavaScript-Programm, das folgende Aufgaben erfüllt: 

a) Definiere ein Array von Objekten, wobei jedes Objekt einen Studenten repräsentiert. 
Jedes Objekt soll die Eigenschaften name, fachrichtung und semester enthalten. 

b) Füge dem Array zwei neue Studenten hinzu. 

c) Erstelle eine Funktion, die das Array entgegennimmt und die Namen der Studenten der Informatik-Fachrichtung, 
die im ersten Semester sind, in die Konsole ausgibt. 

d) Verwende die map-Methode, um ein neues Array zu erstellen, das nur die Namen der Studenten enthält. 

e) Konvertiere das Array von Studentenobjekten in einen JSON-String und speichere diesen in einer Variablen. 

f) Parse den JSON-String zurück in ein Array von Objekten. 

g) Gib das resultierende Array in der Konsole aus, um zu überprüfen, ob die Konvertierung korrekt funktioniert hat.   */
 //a)

const studierende = 
[];
//b)
const hinzufuegen = function (name, fachrichtung, semester){
            const neuerStudent = {name, fachrichtung, semester};  
            studierende.push(neuerStudent);
            console.log(`Studierenden "${name}" hinzugefügt.`);
            return;
}
hinzufuegen("Max Mustermann", "Informatik", 5);
hinzufuegen("Laura Bartels", "Informatik", 1);
hinzufuegen("Tobias Hoffmann", "Geodäsie", 2);
// es geht auch ohne extra funktion:
studierende.push({name: "Martin Klein", fachrichtung: "Informatik", semester: 1}); 
studierende.push({name: "Maria Groß", fachrichtung: "Elektrotechnik", semester: 2}); 


console.log(studierende)
//c)
const ersties = function(arr){
  for (const student of arr){
     if (student.fachrichtung === "Informatik" && student.semester <2){
      console.log(`${student.name} ist ein Erstie.`);
      }
    }
  }

ersties(studierende);


// Verwende die map-Methode, um ein neues Array zu erstellen, das nur die Namen der Studenten enthält. 


const namenObjekt = studierende.map(s => ({ name: s.name }));
const namenString = studierende.map(s => s.name);
console.log(namenObjekt);
console.log(namenString);

// Objekt → JSON-String
const jsonString = JSON.stringify(studierende);
console.log(jsonString);

// JSON-String → zurück in Objekt
const jsonParsed = JSON.parse(jsonString);

console.log(jsonParsed);