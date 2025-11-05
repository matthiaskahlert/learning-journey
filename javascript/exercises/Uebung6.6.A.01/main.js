/* Aufgabe: Funktionen


Entwickle ein kleines JavaScript-Programm, das folgende Anforderungen erfüllt: 

-[x] a) Definiere eine Funktion temperaturKonverter, die eine Temperatur von Celsius in Fahrenheit umrechnet und zurückgibt. 
Die Formel dafür lautet: Fahrenheit = Celsius * 9/5 + 32. 

b) Erweitere die Funktion um die Möglichkeit, auch von Fahrenheit in Celsius umzurechnen. 
Die Funktion soll zwei Parameter entgegennehmen: den Temperaturwert und die Einheit der Eingabetemperatur ('C' für Celsius, 'F' für Fahrenheit). 
Nutze eine if-else-Struktur, um zu entscheiden, welche Umrechnung durchgeführt werden soll. 
Die Formel zur Umrechnung von Fahrenheit in Celsius lautet: Celsius = (Fahrenheit - 32) * 5/9. 

c) Implementiere eine Schleife (wahlweise for oder while), 
die die Funktion temperaturKonverter für Temperaturen von 0 bis 100 Grad Celsius in 10-Grad-Schritten aufruft 
und das Ergebnis in Fahrenheit ausgibt. 

d) Verwende String-Methoden, um die Ausgabe der umgerechneten Temperaturen zu formatieren, 
sodass sie lesbar und ansprechend ist (z.B. "30°C entspricht 86°F"). 

e) Füge eine Funktion hinzu, die eine einfache Debugging-Nachricht ausgibt, bevor eine Temperaturumrechnung durchgeführt wird. 
Die Nachricht soll den Typ der Umrechnung (Celsius zu Fahrenheit oder umgekehrt) und den zu konvertierenden Wert enthalten. 
Nutze Funktionsausdrücke und Arrow-Funktionen für diese Debugging-Funktion.   */

function temparaturKonverter(temparaturwert, einheit){
    let fahrenheit = 0;
    let celsius = 0;
    if (einheit === "C") {
        console.log(`Typ der Umrechnung Celsius zu Fahrenheit mit Temparaturwert:`, temparaturwert)
        fahrenheit = temparaturwert * (9/5)+32;
    return fahrenheit;
    } else if (einheit === "F"){
        console.log(`Typ der Umrechnung Fahrenheit zu Celsius mit Temparaturwert:`, temparaturwert)
        celsius = (temparaturwert -32) * (9/5);
    return celsius;
    } else {
        console.log(`Berechnung nicht möglich, bitte Einheit angeben mit "C" oder "F"!`);     
    }
}

for (i = 0; i <=100; i+=10) {
    let temp = i
    let ergebnis1 = temparaturKonverter(temp, "C");
    console.log(`${i}°C sind umgerechnet ${ergebnis1}°F`);
}

const ergebnis2 = temparaturKonverter(25, "F");
console.log(`25°F sind umgerechnet ${ergebnis2}°C`);

const ergebnis3 = temparaturKonverter("0","C");
console.log(`0°C sind umgerechnet ${ergebnis3}°F`);





/* Temperatur
Umrechnung Celsius in Fahrenheit: °F = °C x 1,8 + 32.
Umrechnung Fahrenheit in Celsius: °C = (°F - 32) / 1,8.
 */

