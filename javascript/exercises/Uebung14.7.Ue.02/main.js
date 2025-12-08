/* Entwickle ein einfaches JavaScript-Programm, das folgende Funktionalitäten umfasst:  

a) Überprüfe, ob im Local Storage ein Eintrag unter dem Schlüssel "userTheme" existiert. Falls nicht, lege diesen mit dem Wert "dark" an.  

b) Füge ein Array mit drei verschiedenen Farbnamen (z.B. "rot", "grün", "blau") hinzu.  

c) Erstelle eine Schleife, die für jede Farbe im Array prüft, ob die aktuelle Farbe "grün" ist. Falls ja, gib eine Meldung in der Konsole aus, dass "Grün ist eine tolle Farbe!" ist.  

d) Verwende das Window-Objekt, um die aktuelle Breite und Höhe des Browserfensters in der Konsole auszugeben.  

e) Führe eine Fetch-Anfrage an die Test-API https://jsonplaceholder.typicode.com/posts/1 aus und gib die Antwort in der Konsole aus.  

f) Implementiere einen einfachen Intersection Observer, der beobachtet, ob ein Element mit der ID "observerTarget" im Viewport sichtbar ist und gib eine Meldung in der Konsole aus, sobald dies der Fall ist.
 */
// a) Überprüfung und Anlegen des "userTheme" im Local Storage 

if (localStorage.getItem("userTheme") === null) { 
    localStorage.setItem("userTheme", "dark"); 
    console.log("userTheme auf 'dark' gesetzt."); 
} else { 
    console.log("userTheme existiert bereits."); 
} 
 

// b) Array mit Farbnamen 

const farben = ["rot", "grün", "blau"]; 
 

// c) Schleife, die prüft, ob die Farbe "grün" ist 

farben.forEach(farbe => { 
    if (farbe === "grün") { 
        console.log("Grün ist eine tolle Farbe!"); 
    } 
}); 
 

// d) Ausgabe der Breite und Höhe des Browserfensters 

console.log("Fensterbreite: ", window.innerWidth, "Fensterhöhe: ", window.innerHeight); 
 

// e) Fetch-Anfrage 

fetch('https://jsonplaceholder.typicode.com/posts/1') 
    .then(response => response.json()) 
    .then(json => console.log(json)) 
    .catch(error => console.log('Anfrage fehlgeschlagen', error)); 
 

// f) Intersection Observer 

const target = document.getElementById('observerTarget'); 
const observer = new IntersectionObserver((entries, observer) => { 
    entries.forEach(entry => { 
        if (entry.isIntersecting) { 
            console.log("Element ist im Viewport sichtbar."); 
            observer.unobserve(entry.target); 
        } 
    }); 
}); 
 
observer.observe(target); 