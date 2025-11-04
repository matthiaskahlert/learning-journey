/* Erstelle ein JavaScript-Programm, das folgende Anforderungen erfüllt: 

a) Definiere eine Variable alter und weise ihr ein beliebiges Alter zu. 

b) Verwende eine if-else-Struktur, um zu überprüfen, ob die Person volljährig ist. 
Gib eine entsprechende Nachricht in der Konsole aus. 

c) Erstelle eine Schleife, die die Zahlen von 1 bis zum Wert der Variable alter ausgibt. 
Verwende dafür eine for-Schleife. 

d) Nutze eine while-Schleife, um eine Variable countdown von 10 herunterzuzählen 
und bei jedem Schritt eine Nachricht in der Konsole auszugeben, bis der Countdown bei 0 ankommt. 

e) Verwende den ternären Operator, um zu überprüfen, ob alter größer als 50 ist. 
Gib je nach Ergebnis eine unterschiedliche Nachricht in der Konsole aus. 

f) Deklariere eine globale Variable name und weise ihr deinen Namen zu. 
Erstelle eine Funktion, die eine Begrüßungsnachricht mit diesem Namen in der Konsole ausgibt. 

g) Definiere innerhalb einer Funktion eine lokale Variable lokaleVariable und gib ihren Wert in der Konsole aus. 
Rufe diese Funktion auf und beobachte, was passiert.   */

//a)
const alter = 45
// b)

if (alter >=18){
    console.log(`Nutzer ist volljährig, das alter ${alter} Jahre liegt über dem alter von 18 Jahren!`)
} else {
    console.log(`Nutzer ist nicht volljährig, das alter ${alter} Jahre liegt unter dem alter von 18 Jahren!`)
}
//c)
for (let i = 1; i<= alter; i++) {
    console.log(i);
}
//d)
let countdown = 10
while (countdown >=0){
    console.log(`Countdown: ${countdown}`);
    countdown--;
}
//e)

// const foo = (Bedingung) ? wenn true : wenn false;
const ausgabe = (alter>50) ? `${alter} ist größer als 50!` : `${alter} ist kleiner oder gleich 50!`
console.log(ausgabe);

//f)
vorname = "Matthias"
function begruessung(){
    console.log(`Guten morgen ${vorname}!`);
}
begruessung();
//g)
function lokal(){
    const lokaleVariable = "Ich bin eine lokale Variable!";
    console.log("Lokale Variable:", lokaleVariable);
    }
lokal(); //log: Lokale Variable: Ich bin eine lokale Variable!

