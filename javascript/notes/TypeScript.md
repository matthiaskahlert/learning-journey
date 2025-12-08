## 1. Was ist TypeScript?

TypeScript ist wie JavaScript, nur besser: Es fügt ein statisches Typsystem hinzu. Das heißt, man sagt schon beim Schreiben des Codes, welche Art von Daten eine Variable haben soll. Das hilft, Fehler früh zu erkennen. Jeder JavaScript-Code funktioniert auch als TypeScript.

## 2. Vorteile gegenüber JavaScript

Fehler früh erkennen: TypeScript meckert schon beim Schreiben, wenn man z. B. versucht, eine Zahl mit einem Text zu addieren.

Modernes JS nutzen: Neue Funktionen können trotzdem auf älteren Browsern laufen, weil TypeScript sie in normales JavaScript umwandelt.

Bessere Übersicht: Durch Typen und Interfaces sieht man sofort, welche Daten wo erwartet werden.

## 3. Geschichte

Entwickelt 2012 von Microsoft, Open Source (Apache-2.0).
Besonders wichtig geworden durch Frameworks wie Angular, das komplett in TypeScript geschrieben ist.

## 4. Wie TypeScript funktioniert (Workflow)

Code schreiben → .ts Datei
Compiler (tsc) wandelt .ts in .js um (Transpilation)
JS-Datei kann im Browser oder Node laufen
Konfiguration über tsconfig.json

## 5. Erste Schritte
```bash
npm install -g typescript    # TypeScript installieren
tsc --init                   # Projekt initialisieren
```

Beispiel "Hello World" in TypeScript:
```typescript
type GreetFunction = (name: string) => string;
const greet: GreetFunction = (name) => `Hello, ${name}!`;

greet("Developer");  // OK
greet(123);          // Fehler!
```

TypeScript erkennt Typen automatisch, z. B. let message = "Hi"; → message ist automatisch string.

## 6. Typensystem

TypeScript ist statisch typisiert, JS dynamisch.
Vorteil: Fehler werden schon beim Schreiben entdeckt, nicht erst beim Ausführen.
IDEs können Typen für Code-Vervollständigung nutzen.

Primitive Typen

number: Zahlen (dezimal, hex, binär, oktal)

bigint: sehr große Zahlen

string: Texte

boolean: true/false

null / undefined: leere Werte

symbol: eindeutige Werte
Beispiel:

```typescript
// Numerische Typen
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
// String
let color: string = "blue";
let sentence: string = `The color is ${color}`;
// Boolean
let isDone: boolean = false;
// Null und Undefined
```

## 2.1.2 Komplexe Typen in TypeScript

Neben den einfachen Typen (number, string, etc.) gibt es in TypeScript komplexe Typen, die helfen, Datenstrukturen genau zu modellieren – besonders nützlich für größere Programme.

### 1. Arrays

Sammlung von Werten gleichen Typs.

Zwei Schreibweisen:
```typescript
let numbers: number[] = [1, 2, 3];       // kurz
let strings: Array<string> = ["hello"];  // generisch
```

Funktional gleich, generische Schreibweise oft bei verschachtelten Typen besser lesbar.

### 2. Tuples

Wie Arrays, aber feste Länge und feste Typen pro Position.

Praktisch für Paare/Tripel, z. B. Koordinaten oder Funktionsrückgaben.
```typescript
let tuple: [string, number] = ["hello", 42];
```

Reihenfolge und Typen sind hier wichtig.

### 3. Enums (Aufzählungen)

Gruppieren benannte Konstanten, die bestimmte Werte haben.

Gut für Status, Richtungen oder Optionen.

Zwei Arten: numerisch oder string-basiert (string oft besser für Debug und Serialisierung):
```typescript
enum Direction { Up, Down, Left, Right }
enum Status { Active = "ACTIVE", Inactive = "INACTIVE" }
```

### 4. Objekte

Zentrale Bausteine wie in JS, aber TypeScript erlaubt exakte Typdefinitionen:

```typescript
type User = {
  name: string;
  age: number;
};
const user: User = { name: "Anna", age: 25 };
```

Vorteile:

Fehler werden früh erkannt.
Struktur ist klar dokumentiert.
Typen können flexibel oder sehr genau sein.


## 2.2 Erweiterte Typen in TypeScript

TypeScript bietet fortgeschrittene Typen, um komplexe Datenstrukturen präzise zu modellieren. Sie machen den Code flexibel und typsicher – besonders für große Anwendungen.

### 1. Union Types

Ein Wert kann mehrere Typen haben (z. B. Zahl oder String).
Nützlich für optionale Parameter, verschiedene Rückgaben oder APIs.
TypeScript erkennt automatisch den aktuellen Typ in Kontrollstrukturen (Type Narrowing):

```typescript
function processInput(input: number | string) {
  if (typeof input === "string") {
    console.log(input.toUpperCase());
  } else {
    console.log(input.toFixed(2));
  }
}
processInput("hello"); // String input
processInput(42);      // Numeric input
```

### 2. Intersection Types

Kombinieren mehrere Typen zu einem Typ („und“-Beziehung).
Ein Wert muss alle Eigenschaften der kombinierten Typen besitzen.
Praktisch für Mixins oder modulare Typdefinitionen:

```typescript
interface HasName { name: string; }
interface HasAge { age: number; }
type Person = HasName & HasAge;
let person: Person = { name: "John", age: 30 }; // beide Eigenschaften nötig
```

### 3. Literal Types

Beschränken Werte auf feste Literale, statt alle Werte eines Typs zu erlauben.
Ideal für Zustände, Konfigurationen oder API-Endpunkte.

Sehr typsicher und gut für Autocomplete in IDEs:

```typescript
type ThemeColor = "light" | "dark" | "system";
function setTheme(theme: ThemeColor) { /* ... */ }
setTheme("light"); // OK
setTheme("blue");  // Fehler
```

Auch für Zahlen möglich:
```typescript
type DiceRoll = 1 | 2 | 3 | 4 | 5 | 6;
```

## 2.3 Typinferenz in TypeScript

Typinferenz ist ein Feature, das TypeScript automatisch Typen erkennt, ohne dass man sie immer explizit angeben muss. Dadurch wird der Code kürzer, lesbarer und trotzdem typsicher.

### 1. Grundlegende Typinferenz

TypeScript erkennt den Typ von Variablen anhand des Startwerts:
```typescript
let message = "Hello"; // string
let count = 42;        // number
```

Auch bei Funktionen wird der Rückgabetyp automatisch abgeleitet:
```typescript
function createUser(name: string, age: number) {
  return { name, age, createdAt: new Date() };
}
// Rückgabetyp: { name: string; age: number; createdAt: Date }
```

Vorteil: Weniger Tipparbeit und geringeres Fehlerpotenzial, weil der Typ konsistent bleibt.

### 2. Kontextuelle Typisierung

TypeScript nutzt den Kontext, in dem ein Wert verwendet wird, um den Typ abzuleiten.

Besonders nützlich bei Callbacks, Event-Handlern oder Array-Methoden:

```typescript
const numbers = [1, 2, 3];
numbers.forEach(num => {
  console.log(num.toFixed(2)); // num wird automatisch als number erkannt
});

function handleRequest(callback: (response: { status: number }) => void) {
  callback({ status: 200 });
}
handleRequest(response => {
  console.log(response.status); // response wird als { status: number } erkannt
});
```

Vorteil: Sicherere und sauberere Nutzung von Funktionen ohne explizite Typangaben.

## 2.4 Type Assertions

Type Assertions sind Hinweise an TypeScript, dass ein Wert einen bestimmten Typ hat.
Keine Typumwandlung: Sie ändern den Wert nicht zur Laufzeit, sie sagen dem Compiler nur, welchen Typ er annehmen soll.
Besonders nützlich, wenn TypeScript den Typ nicht automatisch erkennen kann, z. B. beim Arbeiten mit DOM-Elementen oder externen Bibliotheken.

Syntax

Angle-Bracket Syntax (älter, Konfliktgefahr mit JSX)
```typescript
let someValue: unknown = "this is a string";
let strLength: number = (<string>someValue).length;
```

As-Syntax (bevorzugt, besser lesbar, sicher mit JSX)
```typescript
let otherValue: unknown = "another string";
let otherLength: number = (otherValue as string).length;
```

Beispiel mit DOM
```typescript
const input = document.querySelector("#myInput") as HTMLInputElement;
console.log(input.value); // TypeScript weiß jetzt, dass input ein HTMLInputElement ist
```

Kurz gesagt:
Type Assertions sind wie ein Vertrauensvorschuss an TypeScript – du sagst dem Compiler: „Vertrau mir, dieser Wert hat diesen Typ.“

- Vorteil: Mehr Kontrolle und Präzision beim Typen-Handling

- Nachteil: Kann die Typsicherheit umgehen, also vorsichtig einsetzen.

## 2.5 Generics

Generics ermöglichen es, wiederverwendbare und typsichere Funktionen, Klassen und Interfaces zu schreiben, die mit verschiedenen Typen arbeiten können.

Vorteil: Typensicherheit bleibt erhalten, auch wenn unterschiedliche Datentypen verwendet werden.

Besonders nützlich für: Container, Utilities, abstrakte Datenstrukturen.

### Grundidee

Ein Typparameter (oft T) fungiert als Platzhalter für einen Typ, der erst bei der Verwendung bestimmt wird.

Dadurch kann eine Funktion oder Klasse flexibel arbeiten, ohne Typinformationen zu verlieren.

### Beispiele

Generische Funktion
```typescript
function identity<T>(arg: T): T {
  return arg;
}

let result1 = identity<string>("hello"); // string
let result2 = identity<number>(42);      // number
```

Generisches Interface & Klasse
```typescript
interface Container<T> {
  value: T;
  getValue(): T;
}

class NumberContainer implements Container<number> {
  constructor(public value: number) {}
  getValue(): number {
    return this.value;
  }
}
```

Fortgeschrittene Generics

Generische Constraints

Beschränken, welche Typen erlaubt sind, z. B. nur Typen mit length:
```typescript
interface Lengthwise { length: number; }

function logLength<T extends Lengthwise>(arg: T): void {
  console.log(arg.length);
}

logLength("hello");      // OK
logLength([1, 2, 3]);   // OK
logLength(42);           // Fehler: number hat keine length
```

Generische Klassen mit mehreren Typparametern
```typescript
class DataStore<K, V> {
  private items: Map<K, V> = new Map<K, V>();

  add(key: K, value: V): void {
    this.items.set(key, value);
  }

  get(key: K): V | undefined {
    return this.items.get(key);
  }
}

const store = new DataStore<string, number>();
store.add("age", 30);
console.log(store.get("age")); // 30
```

Kurz gesagt:
Generics = flexible, typsichere Platzhalter für Typen, die dafür sorgen, dass du wiederverwendbaren Code schreiben kannst, ohne Typsicherheit zu verlieren.

## 2.6 Utility Types

Utility Types sind vordefinierte generische Typen in TypeScript, die häufige Typ-Transformationen vereinfachen.

Ziel: Code kürzer, typsicherer und wartbarer machen.

Besonders nützlich bei komplexen Objekttypen oder API-Integration.

Wichtige Utility Types

Partial<T> → macht alle Eigenschaften optional
```typescript
interface Todo {
  title: string;
  description: string;
  completed: boolean;
}

function updateTodo(todo: Todo, fieldsToUpdate: Partial<Todo>) {
  return { ...todo, ...fieldsToUpdate };
}

const todo = { title: "Learn TS", description: "Study types", completed: false };
const updatedTodo = updateTodo(todo, { completed: true });
```

Pick<T, K> → wählt bestimmte Eigenschaften aus
```typescript
type TodoPreview = Pick<Todo, "title" | "completed">;
```

Readonly<T> → macht alle Eigenschaften schreibgeschützt
```typescript
const readonlyTodo: Readonly<Todo> = { title: "Read docs", description: "TS docs", completed: false };
// readonlyTodo.completed = true; // Fehler
```

Record<K, T> → erstellt ein Objekt mit vorgegebenen Schlüssel- und Werttypen
```typescript
type PageInfo = { title: string; url: string };
const pages: Record<string, PageInfo> = {
  home: { title: "Home", url: "/" },
  about: { title: "About", url: "/about" }
};
```


Kurz gesagt:
Utility Types = fertige Tools für häufige Typ-Anpassungen, die den Code robuster, flexibler und leichter wartbar machen.

## 3 - Objektorientierung in TypeScript

Objektorientierte Programmierung (OOP) ist ein Grundprinzip moderner Softwareentwicklung.
TypeScript erweitert die OOP-Fähigkeiten von JavaScript deutlich und macht sie typsicherer und strukturierter.

Mit TypeScript kannst du Klassen, Objekte, Vererbung und Interfaces klar definieren.

OOP-Konzepte wie Kapselung, Vererbung und Polymorphie werden unterstützt.

Vorteil: sauberer, besser wartbarer Code für große Anwendungen.
### 3.1 Klassen und Interfaces
#### 3.1.1 Klassen in TypeScript

Klassen sind zentrale Bausteine der objektorientierten Programmierung in TypeScript.
Sie definieren Objekte mit Eigenschaften (Properties) und Methoden.
TypeScript erweitert JavaScript-Klassen um Features wie:

- Zugriffsmodifizierer: public, private, protected
- readonly Properties: Werte, die nach der Initialisierung nicht mehr geändert werden können
- Parameter Properties: Kombinieren Deklaration und Initialisierung von Properties direkt im Konstruktor

Beispiel:
```typescript
class User {
  constructor(
    private readonly id: number, // readonly, nur innerhalb der Klasse
    public name: string,         // public, überall zugreifbar
    protected email: string      // protected, nur in Klasse & Unterklassen
  ) {}

  public getInfo(): string {
    return `${this.name} (${this.email})`;
  }

  private validateEmail(): boolean {
    return this.email.includes('@');
  }
}

const user = new User(1, "Max Mustermann", "max@example.com");
console.log(user.name);        // erlaubt
console.log(user.getInfo());   // erlaubt
// console.log(user.email);    // Fehler: protected
// user.id = 2;                // Fehler: readonly
```

Parameter Properties vereinfachen die Deklaration und Initialisierung von Eigenschaften direkt im Konstruktor.

#### 3.1.2 Interfaces

Interfaces definieren Strukturen oder Verträge für Objekte und Klassen.
Sie existieren in JavaScript nicht, sind also eine TypeScript-Erweiterung.

Nützlich, um Objektformen festzulegen und sicherzustellen, dass Klassen bestimmte Eigenschaften oder Methoden implementieren.

Beispiel Interface:

```typescript
interface IUserData {
  id: number;
  name: string;
  email: string;
  lastLogin?: Date;      // optional
  readonly createdAt: Date; // readonly, kann nicht verändert werden
  updateProfile(newData: Partial<IUserData>): void;
}
```

Klassenimplementierung:

```typescript
class UserProfile implements IUserData {
  readonly createdAt: Date = new Date();
  constructor(
    public id: number,
    public name: string,
    public email: string,
    public lastLogin?: Date
  ) {}
  updateProfile(newData: Partial<IUserData>): void {
    if (newData.name) this.name = newData.name;
    if (newData.email) this.email = newData.email;
    this.lastLogin = new Date();
  }
}
```

Interfaces erweitern andere Interfaces (interface IUser extends INameable, IIdentifiable)
Klassen können mehrere Interfaces implementieren, z. B. class Customer implements INameable, IIdentifiable

#### 3.1.3 Unterschiede zwischen Interfaces und Types
| Feature|Interface| Type Alias|
| -------------------------- |------------------------------------------ |---------------------------------------------- |
| **Definition**             | Definiert die Form eines Objekts| Definiert einen Typ (Objekt, Union, Tuple, Primitive, etc.)       |
| **Erweiterung**            | Kann mit `extends` erweitert werden und später nachträglich ergänzt werden (**Declaration Merging**) | Erweiterung nur über `&` möglich, keine nachträgliche Erweiterung |
| **Klassenimplementierung** | Ideal, wenn Klassen einen Vertrag erfüllen sollen | Kann nicht direkt implementiert werden (nur Typprüfung möglich)   |
| **Besondere Stärken**      | Objekttypen, öffentliche API-Verträge, Merging | Unions, Tuples, Mapped Types, Alias für Primitive                 |


Beispiele:

```typescript
// Interface
interface Animal {
  name: string;
}
interface Dog extends Animal {
  breed: string;
}
// Nachträgliche Erweiterung möglich
interface Animal {
  age: number;
}

// Type Alias
type AnimalType = { name: string };
type DogType = AnimalType & { breed: string };
// Nachträgliche Erweiterung nicht möglich
// type AnimalType = { age: number } // ❌ Fehler
```

Merksatz:

Interfaces: für Objekte und Klassen-Contracts

Types: für komplexe Typen, Unions oder Tuples