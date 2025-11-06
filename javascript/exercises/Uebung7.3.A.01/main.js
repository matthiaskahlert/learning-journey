/* Aufgabe: Objekte


Entwickle ein einfaches Kontaktverwaltungssystem in JavaScript, das die folgenden Anforderungen erfüllt:  

a) Erstelle ein Objekt kontaktListe, das als Schlüssel-Wert-Paare die Namen und E-Mail-Adressen von drei Kontakten enthält. 
Die Namen der Kontakte sollen als Schlüssel und ihre E-Mail-Adressen als Werte gespeichert werden.  

b) Füge eine Methode neuerKontakt zum Objekt kontaktListe hinzu, die es ermöglicht, einen neuen Kontakt hinzuzufügen. 
Diese Methode soll zwei Parameter entgegennehmen: den Namen und die E-Mail-Adresse des neuen Kontakts. 

c) Erstelle eine Funktion emailSuche, die nach der E-Mail-Adresse eines Kontakts sucht, 
indem der Name des Kontakts als Argument übergeben wird. 
Die Funktion soll die E-Mail-Adresse des gesuchten Kontakts zurückgeben. 
Wenn der Kontakt nicht gefunden wird, soll die Funktion eine entsprechende Nachricht zurückgeben. 

d) Implementiere eine Kontrollstruktur, die überprüft, ob ein Kontakt in der kontaktListe existiert, 
bevor ein neuer Kontakt hinzugefügt wird, um Duplikate zu vermeiden. 

e) Nutze eine for-in-Schleife, um alle Kontakte in der kontaktListe und ihre E-Mail-Adressen in der Konsole auszugeben. 

f) Erweitere das Kontaktverwaltungssystem um eine Methode kontaktLöschen, die es ermöglicht, einen Kontakt anhand seines Namens zu löschen.   */

const kontaktListe = {
    Max :   "max@mustermann.de",
    Erika :   "erika@mustermann.de",
    Moritz :   "moritz@mustermann.de"
}
kontaktListe.neuerKontakt = function(name, email){
    this[name]? console.log(`der name "${name}" existiert schon`) : kontaktListe[name] = email     // man muss die eckigen Klammern nutzen, um den Wert der Variable name als Schlüssel zu verwenden
    
}
console.log(kontaktListe);
kontaktListe.neuerKontakt("Matze","matze@mustermann.de");
kontaktListe.emailSuche = function(name){
    this[name] ? console.log(`Zum Namen: "${name} ist die Emailadresse "${this[name]}" gespeichert`): console.log(`Zum Namen: "${name} wurde nichts gefunden.`);
    // for (const key in this){  // this verweist auf kontaktListe
    //     if (key===name){
    //         console.log(`Zum Namen: "${name} ist die Emailadresse "${kontaktListe[key]}" gespeichert`);
    //     }
    // }
}
kontaktListe.emailSuche("Max");
kontaktListe.emailSuche("Matze");
kontaktListe.emailSuche("ungültig");

console.log(kontaktListe["Max"]); // max@mustermann.de
kontaktListe.neuerKontakt("Matze","matze@mustermann.de");
kontaktListe.neuerKontakt("Matze2","matze2@mustermann.de");

for (const key in kontaktListe){
    if (typeof kontaktListe[key] !== "function")        // die Zeile verhindert dass auch Methoden ausgegeben werden
    console.log(`Object key: ${key} - Object Value: ${kontaktListe[key]}`); 

}

kontaktListe.kontaktLoeschen = function(name){
    this[name]? delete this[name] :   console.log(`der name "${name}" existiert nicht`);
   }   // man muss die eckigen Klammern nutzen, um den Wert der Variable name als Schlüssel zu verwenden

kontaktListe.emailSuche("Matze2");
console.log("nun löschen");
kontaktListe.kontaktLoeschen("Matze2");
kontaktListe.emailSuche("Matze2");

/* for (const key in imgObj){
    console.log("Object key", key); // gibt die Schlüssel des Objekts aus Object key src, key width, key height, key alt
}

for (const key in imgObj){
    console.log("Object value", imgObj[key]);
} */