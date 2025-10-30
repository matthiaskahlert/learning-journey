/* Erstelle ein JavaScript-Skript, das folgende Aufgaben erfüllt: 

a) Definiere eine Variable text, die einen mehrzeiligen String enthält. 
Dieser String soll mindestens ein Mal den Namen einer Stadt (z.B. "Berlin"), gefolgt von einer Beschreibung (z.B. "ist die Hauptstadt von Deutschland.") enthalten. Die Beschreibung kann frei erfunden sein, muss aber nach dem Namen der Stadt in der gleichen Zeile stehen. 

b) Benutze reguläre Ausdrücke, um alle Vorkommen von Stadtnamen in text zu finden. 
Ein Stadtnamen soll hier als ein Wort definiert sein, das mit einem Großbuchstaben beginnt und ausschließlich aus Buchstaben besteht. 

c) Für jedes gefundene Vorkommen eines Stadtnamens, füge diesen Namen in ein Array gefundeneStaedte ein. 

d) Verwende die Methode join() auf gefundeneStaedte, um eine Zeichenkette zu erstellen, in der alle gefundenen Stadtnamen durch Kommas getrennt sind. Speichere das Ergebnis in einer Variablen stadtnamenString. 

e) Zeige stadtnamenString mit console.log() in der Konsole an. */

// a)
const text = `Berlin ist schön groß.
Köln ist bekannt.
München begeistert viele.
Hamburg ist toll!
Leipzig wächst schnell.
Dortmund ist auch halbwegs bekannt.`;
//b)

// Regex aus dem Lernscript:

// Wie finde ich alle Wörter, die mit Großbuchstaben beginnen? match() könnte helfen.
const gefundeneStaedte = text.match(/\b[A-Z][a-zß-ü]{1,}/g); // log: (6) ['B', 'K', 'M', 'H', 'L', 'D']
// der / umschließt das Regex, A-Z denn ich will großbuchstaben finden, g ist der parameter für ein golabes attribut um den ganzen string zu dutrchsuchen
// um die umlaute zu finden braucht man bei den kleinbuchstaben noch ß-ü

//c)
console.log(gefundeneStaedte); //log: (6) ['Berlin', 'Köln', 'München', 'Hamburg', 'Leipzig', 'Dortmund']

//d)
const stadtnamenString = gefundeneStaedte.join();

//e)
console.log(stadtnamenString); //log: Berlin,Köln,München,Hamburg,Leipzig,Dortmund
