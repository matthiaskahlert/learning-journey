/* Aufgabe: Window-Objekt, Observer, Cookies, Animation, Local Storage
Du arbeitest als Webentwickler und hast die Aufgabe, eine interaktive Webseite zu erstellen, die verschiedene Webtechnologien nutzt. Die Webseite soll folgende Funktionen haben: 

a) Verwende das Window-Objekt, um die Breite und Höhe des Browserfensters zu ermitteln und zeige diese Informationen in einem Absatz () auf der Webseite an. 

b) Implementiere eine Funktion, die prüft, ob Cookies im Browser aktiviert sind. Zeige das Ergebnis ("Cookies aktiviert" oder "Cookies deaktiviert") in einem weiteren Absatz auf der Webseite an. 

c) Nutze Local Storage, um die Anzahl der Besuche auf der Webseite zu speichern und bei jedem Laden der Seite zu aktualisieren. Zeige die Anzahl der Besuche in einem Absatz an. 

d) Implementiere eine einfache Animation mithilfe der Web Animations API, die ein Element auf der Seite beim Laden der Seite einfliegen lässt. 

e) Verwende den Intersection Observer, um zu erkennen, wann ein bestimmtes Element (z.B. ein Bild) in das Sichtfeld des Nutzers scrollt und ändere daraufhin die Farbe des Elements. 

f) Erstelle eine Funktion, die mithilfe der Fetch-API Daten von einer Test-API (z.B. https://jsonplaceholder.typicode.com/posts) abruft und die Titel der ersten fünf Beiträge in einer Liste () auf der Webseite anzeigt. */

// a) Um die Breite und Höhe des Browserfensters ermitteln: 

window.onload = function() { 
    let breite = window.innerWidth; 
    let höhe = window.innerHeight; 
    document.getElementById('windowSize').innerHTML = `Die Größe des Fensters beträgt ${breite} x ${höhe} Pixel.`; 
}; 
 

// b)Cookies aktiv: 

function checkCookies() { 
    if(navigator.cookieEnabled) { 
        document.getElementById('cookieStatus').innerHTML = 'Cookies aktiviert'; 
    } else { 
        document.getElementById('cookieStatus').innerHTML = 'Cookies deaktiviert'; 
    } 
} 
checkCookies(); 
 

// c) Local Storage nutzen 

function updateBesuche() { 
    let besuche = localStorage.getItem('besuche'); 
    if(besuche) { 
        besuche = Number(besuche) + 1; 
    } else { 
        besuche = 1; 
    } 
    localStorage.setItem('besuche', besuche); 
    document.getElementById('besuche').innerHTML = `Diese Seite wurde ${besuche} Mal besucht.`; 
} 
updateBesuche(); 
 

// d) Animation mit Web Animations API 

document.getElementById("animation").animate(
  [
    { transform: "scale(0.5)", opacity: 0 },
    { transform: "scale(1)", opacity: 1 }
  ],
  {
    duration: 500,
    easing: "ease-out",
    fill: "forwards"
  }
);

// e) Intersection Observer

let observer = new IntersectionObserver((entries) => { 
    entries.forEach(entry => { 
        if(entry.isIntersecting) { 
            console.log("Observer ausgelöst! Element ist im Sichtbereich.");
            entry.target.style.backgroundColor = 'blue'; 
        } 
    }); 
}); 

observer.observe(document.getElementById('observerElement')); 
 


// f) Fetch-API und Titel

fetch('https://jsonplaceholder.typicode.com/posts') 
    .then(response => response.json()) 
    .then(data => { 
        let liste = document.getElementById('beiträge'); 
        for(let i = 0; i < 5; i++) { 
            let li = document.createElement('li'); 
            li.textContent = data[i].title; 
            liste.appendChild(li); 
        } 
    }); 
