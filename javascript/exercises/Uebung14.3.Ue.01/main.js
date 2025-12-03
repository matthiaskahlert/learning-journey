/* a) Definiere ein Array mit verschiedenen Werten, 
einschließlich mindestens eines null und eines undefined Wertes. 
Dieses Array soll Daten von verschiedenen Sensoren repräsentieren, wobei einige Sensoren möglicherweise ausgefallen sind 
und daher null oder undefined als Wert liefern. 

b) Verwende eine Schleife, um durch das Array zu iterieren. 
Für jeden Wert im Array überprüfe mit einer if-else-Struktur, ob der Wert null oder undefined ist. 
Wenn ja, zeige eine Warnmeldung in der Konsole an, die besagt, dass der Sensor defekt ist. 
Andernfalls gib den Wert des Sensors aus. 

c) Implementiere eine Funktion, die das Window-Objekt verwendet, um die aktuelle Bildschirmbreite und -höhe in der Konsole auszugeben. 

d) Verwende den Intersection Observer API, um zu beobachten, 
wann ein bestimmtes Element (z.B. ein <div> mit der ID sensorView) vollständig sichtbar im Viewport ist. 
Sobald das Element sichtbar ist, soll eine Nachricht in der Konsole ausgegeben werden, 
die besagt, dass das Element jetzt sichtbar ist. */


// a) Array mit Sensorwerten, inkl. null und undefined
const sensorDaten = [23, null, 42, undefined, 15];

// b) Schleife zum Überprüfen der Sensorwerte
for (let i = 0; i < sensorDaten.length; i++) {
    if (sensorDaten[i] === null || sensorDaten[i] === undefined) {
        console.warn(`Sensor ${i} defekt`);
    } else {
        console.log(`Sensor ${i}: ${sensorDaten[i]}`);
    }
}

// c) Funktion zur Ausgabe der Bildschirmgröße
function zeigeBildschirmgroesse() {
    console.log(`Breite: ${window.innerWidth}px, Höhe: ${window.innerHeight}px`);
}

// Bildschirmgröße direkt beim Laden anzeigen
zeigeBildschirmgroesse();

// Auch bei Größenänderung ausgeben
window.addEventListener('resize', zeigeBildschirmgroesse);

// d) Intersection Observer für das Element #sensorView
const sensorView = document.getElementById('sensorView');
if (sensorView) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                console.log('Element jetzt sichtbar');
            }
        });
    }, { threshold: 1 }); // threshold 1 = vollständig sichtbar

    observer.observe(sensorView);
} else {
    console.warn('Element #sensorView existiert nicht!');
}
