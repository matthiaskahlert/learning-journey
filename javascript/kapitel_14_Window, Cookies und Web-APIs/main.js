//Frage: Wie definiert man ein Array in JavaScript, das verschiedene Sensordaten enthält, wobei einige Sensoren möglicherweise null oder undefined liefern?
const sensorDaten = [23, null, 42, undefined, 15];

// Frage: Wie kann man mit einer Schleife durch ein Array iterieren und prüfen, ob ein Wert null oder undefined ist?

for (let i = 0; i < sensorDaten.length; i++) {
  if (sensorDaten[i] === null || sensorDaten[i] === undefined) {
    console.warn(`Sensor ${i} defekt`);
  } else {
    console.log(`Sensor ${i}: ${sensorDaten[i]}`);
  }
}

// Frage: Wie kann man mit einer Schleife durch ein Array iterieren und prüfen, ob ein Wert null oder undefined ist?

for (let i = 0; i < sensorDaten.length; i++) {
  if (sensorDaten[i] === null || sensorDaten[i] === undefined) {
    console.warn(`Sensor ${i} defekt`);
  } else {
    console.log(`Sensor ${i}: ${sensorDaten[i]}`);
  }
}

// Frage: Wie beobachtet man mit dem Intersection Observer API, wann ein Element vollständig sichtbar im Viewport ist?

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting) {
      console.log('Element jetzt sichtbar');
    }
  });
}, { threshold: 1 });

observer.observe(document.getElementById('sensorView'));
