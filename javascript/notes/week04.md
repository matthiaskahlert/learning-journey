# Meine Markdown notes Woche 4

## Tag 16

## Learningfacts - Kapitel 10 - DOM - Document Object Model

Das HTML wird mit Java Script zum DOM. Java Script kann die Elemente einzeln ansprechen und so mit dem DOM Informationen an andere Anwendungen weiterreichen.
Das DOM erzeugt eine Baumstruktur, in der jedes HTML element einzeln erreicht wird.
Die Elemente werden Nodes genannt. Nicht nur Elemente, sondern auch Attribute wie src- oder img-tags bilden nodes.
Mit console.dir(document) in der Browserkonsole kann man die properties des DOM in der Baumstruktur inspizieren.
Über dot-notation kann man sich unterelemente explizit rauspicken, z.B. console.dir(document.links) u die linksammlung (HTML Collection) zu inspizieren.
Eckige Klammern deuten an, dass es sich um eine Arrayähnliche struktur handelt und die elemente einen 
index haben.

### Methode  document.getElementById().
Um nicht über den index nach Elementen der Webseite suchen zu müssen, nutzt man die Methode:
document.getElementById().

document.getElementById() ist eine DOM-Methode, mit der ich ein bestimmtes HTML-Element über seinen eindeutigen id-Wert auswähle.

```js

const element = document.getElementById("meinElement");
```



Man benutzt es um:

- HTML-Elemente gezielt auszulesen

- Inhalte zu ändern (textContent, innerHTML, …)

- Styles zu setzen (style.color = "red")

- Events zu registrieren (addEventListener)

- Formularelemente zu steuern (Input-Werte auslesen oder setzen)

Kurzform:
getElementById() verbindet JavaScript direkt mit einem bestimmten HTML-Element, damit ich es im DOM manipulieren kann.

### 10.2 - Zugriff auf DOM Elemente

console.dir(document); // zeigt ein Verzeichnis der Eigenschaften eines Objekts 

console.dir(document); // zeigt die Elemente des DOM
Folgend eine Liste von HTML collections:
• document.all
listet alle HTML-Elemente der Webseite in einer HTMLAllCollection auf –
heute »deprecated« (veraltet), aber interessant.
• document.anchors
eine HTMLCollection aller Links der Seite.
• document.body
ein Objekt mit allen Elementen des body-Elements.
• document.cookie
ein String mit den Informationen zu den Cookies der Seite.
• document.forms
eine HTMLCollection aller form-Elemente der Seite.
• document.images
gibt alle img-Elemente des Dokuments als HTMLCollection zurück.
• document.isConnected
gibt true zurück, wenn eine Verbindung zum Internet besteht, sonst false.
• document.lastModified
Datum der letzten Änderung des Dokuments.
• document.links
gibt alle a-Elemente des Dokuments als HTMLCollection zurück.
• document.location
gibt ein Location-Objekt mit Informationen über die URL zurück und öffnet
die Möglichkeit, die URL zu ändern.
• document.styleSheets
Liste der CSS-Dateien der Seite

### 10.3 - DOM Methoden und Eigenschaften
• getElementById() hatte ich schon kennengelernt. In komplexen Fällen in denen getElementsById zu aufwändig wird, bieten sich folgende Methoden an:

• document.getElementsByTagName()
gibt alle Elemente mit einem HTML-Tag-Namen als HTML Collection zurück
• document.getElementByClassName()
gibt alle Elemente mit einem HTML-class-Namen als HTML Collection zurück
```js
const items = document.getElementsByClassName("item");
console.log(items[0]);      // erstes Element
console.log(items.length);  // Anzahl
```

• – HTML-Tag-Name
Jedes Element hat einen Tag-Namen, z. B. DIV, P, UL, LI, A usw.
Mit getElementsByTagName("tag") kann ich alle Elemente dieses Typs im DOM auswählen.
Zugriff über dot-notation für Tag-Namen gibt es nicht direkt - man muss getElementsByTagName() nutzen.
```js
const paragraphs = document.getElementsByTagName("p");
console.log(paragraphs.length); // Anzahl aller <p>-Elemente

```

• class-Attribut
das class-Attribut bildet eine Ausnahme bei der dot.notation, denn der Zugriff erfolgt über className.
```js
    const className = regal.className;
    console.log("className", className);
    const attr = regal.getAttribute("class");
    console.log("attr", attr);

    regal.classList.add("neu");    // fügt Klasse hinzu
    regal.classList.remove("alt"); // entfernt Klasse
    regal.classList.toggle("aktiv"); // fügt hinzu oder entfernt je nach Zustand


```
className gibt alle Klassen des elements als String zurück.
getAttribute verwendet den realen Namen des Attributs.

setAttribute(attributname, Werte) Überschreibt das Attribut oder setzt es.

#### CSS-Stile ändern

• elem.style überschreibt css stile.
```js
regal.style.color = "red";      // Textfarbe ändern
regal.style.backgroundColor = "yellow"; // Hintergrundfarbe ändern
```
elem.style überschreibt das style-Attribut. Anweisungen wie elem.style.color oder elem.style.width fügen Eigenschaften dynamisch ein, ohne vorhandene Stile zu überschreiben.

einige Beispiele:
```js
    regal.style.color = "#4A884D";
    regal.style.backgroundColor = "lavender";
    regal.style.backgroundImage = "url('images/flowers-01.webp')";
    regal.style.border = "3px solid green";
    regal.style.boxShadow = "10px 20px 15px silver";
    regal.style.fontSize = "3rem"
    regal.style.height = "200px";
    regal.style.maxWidth = "96%";
    regal.style.opacity = "0.8";
    regal.style.padding = "1rem";
    regal.style.textAlign = "center";
```

• style.cssText() – CSS kompakt einbringen
Wenn mehr als eine Eigenschaft geändert wird, braucht elem.style.xy viele Zeilen. 
Eleganter und gut lesbar ist elem.style.cssText.
cssText() kann CSS-Eigenschaften auslesen und schreiben.
.
Bevor man Eigenschaften überschreibt, sollte man auf die existenz des Elements prüfen:
const item = document.getElementById("#item");
console.log("item", item);
Wenn item nicht existiert, gibt die zuweisung null zurück
if (item !== null){
    item.style.cssText = "font-size: 2rem";

}

### 10.4 Zugriff mit CSS-Selektoren – querySelector() und querySelectorAll()

Mit querySelector() und querySelectorAll() erreicht JavaScript jedes element mit CSS-Selektoren.


#### querySelector() Zugriff auf jedes einzelne Element

querySelector(elem) gibt das erste Element zurück auf das der Selector passt. Das Argument ist ein String in Hochkommas. beispiel:
```js
const nav = document.querySelector("header");
console.log(header);
```

Wenn das Dokument mehr als nur ein angefragtes Element enthält, wird es nur das erste gefundene zurückgeben. Für den zugriff aus alle Elemente einer CSS Klasse braucht man querySelectorAll().

das Argument von querySelector() ist ein string der Typ-Selektoren (z.B. h1, input, p), class- oder id-Selektoren (z.B. .foo, #bar) und attribut-Selektoren (z.B. input[type="password"]) darstellt.

```js
const h3 = document.querySelector(`h3`); // erstes element von h3
const block = document.querySelector(".block"); // erstes Element mit der CSS-Klasse .block
const main = document.querySelector("#main"); // erstes element mit id="main"
const search = document.querySelector("input[type=`search`]"); // erstes input element mit type=`search`
```

Um auf elemente an einer bestimmten Position zuzugreifen, nutzt querySelector() sogenannte Pseoduklassen. man erkennt sie am einfachen Doppelpunkt (:hover oder :first-child).

Elementtypen.

💡 Merke:
nth-child() zählt alle Kinder eines Eltern-Elements, egal welchen Typ,
nth-of-type() zählt nur Kinder eines bestimmten Typs (z. B. nur <li>).

CSS Stile mit querySelector() Ändern

```js
const teaser = document.querySelector(".teaser");
teaser.style.backgroundColor = "var(--magna-color-rot)";
```
dont trust HTML, denn wenn kein element mit dem selektor existiert, gibt querySelector() null zurück.

```js
const elem = document.querySelector(".selector");
console.log("elem", elem);

```

Erst der Versuch, dem nicht vorhandenen Element eine Eigenschaft zuzuweisen
oder den Inhalt zu ändern, bringt einen Syntaxfehler zum Vorschein.

besser ist es zu prüfen ob das element existiert:
if (elem !== null) {
    elem.style.color = "green ";
    } else {
        console.log("Element existiert nicht");
    }

#### document.querySelectorAll() – alle Elemente, die zu einem CSS-Selektor passen

document.querySelectorAll() gibt alle Elemente mit einem CSS-Selector als NodeList zurück. Argument ist ein String mit den gesuchten CSS-Elementen.


•  document.querySelectorAll('main img'); // alle img-Elemente unterhalb von main
•  document.querySelectorAll('.ci.post'); // alle elemente mit class="post ci"
•  document.querySelectorAll('input[type="number"]'); // alle inputs mit type ="number"
•  document.querySelectorAll('li:nth-child(odd)'); // alle elemente mit ungeradem index
•  document.querySelectorAll('img[src*="/img/"]'); // alle Bilder mit der Zeichenkette /img( im src Attribut)


*= ist ein css selector trick:
/* Allgemein */
element[attribut]         /* alle Elemente, die dieses Attribut haben */
element[attribut="wert"]  /* alle Elemente, bei denen das Attribut exakt diesen Wert hat */
element[attribut*="teil"] /* alle Elemente, bei denen der Attributwert die Teilzeichenkette enthält */
element[attribut^="anfang"] /* alle, die mit diesem Wert beginnen */
element[attribut$="ende"]   /* alle, die mit diesem Wert enden */

NodeLists - Listen von Elementen
Der rückgabewert von querySelectorAll() ist eine NodeList. sie sehen so aus wie arrays, sind aber statische Listen. Man kann array Methoden auf NodeLists nutzen
NodeLists haben einen Index – item(index) – und unterstützen die Iteration mit
forEach().
```js
listElems.forEach(item => console.log(item.innerText));
```
Der Index steuert ein individuelles Element der NodeList an, z.B. um den Text zwischen öffnendem und schließendem li-Tag zu lesen oder zu überschreiben.
```js
console.log("listElems[2]", listElems[2].innerText); // listElems[2] Der Herr der Ringe Zum Warenkorb
```

Wie wählt man Elemente im DOM aus?
* Nach ID
document.getElementById("name");

HTML:
<div id="name"></div>

* Nach Klasse

In querySelector brauchst du einen Punkt:

document.querySelector(".box"); 

HTML:
<div class="box"></div>

* Nach Tag

Ohne Punkt:

document.querySelector("p");

HTML:
<p>Hallo</p>

* Klasse + Tag zusammen
document.querySelector(".list li");

HTML:
<ul class="list">
    <li>Eintrag</li>
</ul>

Bedeutung: Alle <li> inside eines Elements mit der Klasse .list.



Merksatz (ganz kurz)

ID → ohne Zeichen → "idName"

Klasse im Selektor → mit Punkt → ".klasse"

Tag → einfach nur "tag"

HTML selbst → nie mit Punkt → class="name"


💡 Merksatz:

createElement = Neues Element im Speicher erstellen
appendChild = Element in den DOM „einfügen“ und sichtbar machen


### Exkurs CSS-Selektoren – Kurz-Merkliste

CSS-Selektoren sind Muster, mit denen ich Elemente im DOM auswähle, um sie mit CSS zu gestalten oder z.B. mit querySelector() zu finden.

#### 🔹 Grundselektoren
element → alle Elemente (div, p, span)
.class → Elemente mit bestimmter Klasse
#id → Element mit dieser ID


#### 🔹 Attributselektoren
[attr] → hat Attribut
[attr="x"] → Attribut = x
[attr^="x"] → beginnt mit x
[attr$="x"] → endet mit x
[attr*="x"] → enthält x

#### 🔹 Struktur
'A B'             → B irgendwo in A  
'A > B'           → B direktes Kind von A  
'A + B'           → nächstes Geschwister  
'A ~ B'           → spätere Geschwister  

#### 🔹 Pseudo-Klassen
:hover → Maus über Element
:active → aktiv beim Klicken
:focus → Fokus (z. B. Input)
:first-child → erstes Kind
:last-child → letztes Kind
:nth-child(n) → n-tes Kind


#### 🔹 Pseudo-Elemente
::before → Inhalt vor Element
::after → Inhalt nach Element
::first-letter → erster Buchstabe


#### 🔹 querySelector()
document.querySelector('CSS-Selektor');
document.querySelectorAll('CSS-Selektor');

querySelector(sel)     → erstes Element  
querySelectorAll(sel)  → NodeList (alle Elemente)  

#### 🔹 Beispiele
document.querySelector('#login');  
document.querySelector('.item.active');  
document.querySelector('ul > li:last-child');  
document.querySelector('[data-id="42"]');  
document.querySelector('input[type="email"]');  
document.querySelectorAll('.todo-item');  

#### 🔹 Quick Alias
const $  = (s) => document.querySelector(s);  
const $$ = (s) => document.querySelectorAll(s);




### 10.5 DOM-Navigation
Die sicherste und einfachte Methode für Elementzugriffe ist der querySelector() in verbindung mit einem CSS selektor.
Falls keine Klassen oder Attribute zur Verfügung stehen kann man über die Verwandschaftsverhältnisse auf die elemente zugreifen.

#### DOM - Verwandschaftsbeziehungen
Folgend eine Liste von DOM eigenschaften
| DOM-Eigenschaft          | Beschreibung |
|--------------------------|-------------|
| `nextElementSibling`     | Gibt das nächste Geschwisterelement **rechts** im DOM zurück (nur Elemente, keine Textknoten). |
| `previousElementSibling` | Gibt das vorherige Geschwisterelement **links** im DOM zurück (nur Elemente). |
| `parentElement`          | Gibt das **übergeordnete Elternelement** zurück. |
| `firstElementChild`      | Gibt das **erste Kind-Element** zurück (ignoriere Textknoten). |
| `lastElementChild`       | Gibt das **letzte Kind-Element** zurück. |
| `children`               | Gibt eine **HTMLCollection aller Kind-Elemente** zurück (keine Textknoten). |


### 10.6 innerHTML, innerText und TextContent

item.innerText gibt den sichtbaren Textinhalt eines elements zurück.
innerText überschreibt auch den Inhalt eines Elements.
innerHTML überschreibt den Inhalt eines elements, kann dabei aber auch HTML-Tags mitsamt Attributen setzen.
textContent gibt den gesamten Textinhalt eines Elements zurück. HTML tags werden nicht ausgewertet sondern angezeigt.

### 10.7 Elemente ins DOM einfügen

Die Methoden um neue Elemente ins DOM einzufügen uterscheiden sich in den Referenz-Elementen.

| Methode         | NodeObjekt          | Position / Wirkung                                                    |
|-----------------|---------------------|-----------------------------------------------------------------------|
| appendChild()   | ein Node            | Fügt als **letztes Kind** ein                                         |
| insertBefore()  | ein Node            | Fügt als Kind-Element **vor einem bestimmten Kind** ein               |
| append()        | Eltern-Element      | Fügt ein oder mehrere Element-Knoten oder Strings **am Ende** ein     |
| prepend()       | Eltern-Element      | Fügt ein oder mehrere Element-Knoten oder Strings **am Anfang** ein   |
| replaceChild()  | Eltern-Element      | **Ersetzt** ein vorhandenes Kind-Element                              |
| replaceWith()   | Element-Knoten      | **Ersetzt** den Knoten selbst                                         |
| before()        | Element-Knoten      | Fügt Elemente **vor** diesem Knoten ein                               |
| after()         | Element-Knoten      | Fügt Elemente **nach** diesem Knoten ein                              |
| innerHTML       |                     | Ersetzt das vollständige Element                                      |

appendChild() und replaceChild() setzen das Fragment an der gewünschten Stelle im dokument ein.
insertBefore() Element vor einem anderen element einfügen. 
Für den Einsatz von insertBefore() muss das Referenz-Element identifiziert werden, vor dem ein neues Element erscheinen soll und das Eltern element der Rezferenz.

Beispiel: man möchte "Orange" vor "Banane" einfügen:
```html
<ul id="fruits">
  <li>Apfel</li>
  <li>Banane</li>
</ul>
```
```js
// 1. Eltern-Element auswählen
const ul = document.getElementById("fruits");

// 2. Referenz-Element auswählen (vor welchem Element soll das neue stehen?)
const banana = ul.children[1]; // das zweite <li> = Banane

// 3. Neues Element erstellen
const orange = document.createElement("li");
orange.innerText = "Orange";

// 4. Neues Element einfügen
ul.insertBefore(orange, banana);
```
```html
<ul id="fruits">
  <li>Apfel</li>
  <li>Orange</li> <!-- neu -->
  <li>Banane</li>
</ul>

```

parent.insertBefore(newNode, referenceNode) → „Füge newNode in parent ein, vor referenceNode.“
parent → das Eltern-Element, das die Kinder enthält - "Wo soll das neue Element eingefügt werden?"
newNode → das Element, das du einfügen willst - "Was soll eingefügt werden?"
referenceNode → das Kind, vor dem eingefügt werden soll  - "Vor welchem Kind soll es eingefügt werden?"

append(), prepend() – am Ende bzw. am Anfang einfügen

before() und after() - vor oder nach einem Element einfügen

### 10.9 Komplexe Strukturen einfügen

Die übernahme von Daten z.B. für produktbeschreibungenn, die eine anwendung auf dem Server als JSON-Array liefert.
Das array enthält die elemente jedes Produkts als Objekt.

