✅ 🔷 TEIL 1 — TypeScript (komplette kompakte Zusammenfassung)
1. Was TypeScript ist

Superset von JavaScript
→ erweitert JS um statische Typen.

Wird zu normalem JavaScript kompiliert.

Ziel: Fehler früh finden, bessere Wartbarkeit, bessere Entwickler-Tools.

2. Typen – das Fundament
Primitive Typen

string

number

boolean

null

undefined

bigint

symbol

Any, Unknown & Never

any → Typprüfung ausgeschaltet

unknown → sicherer, muss vor Nutzung geprüft werden

never → Funktionen, die nie zurückkehren (z. B. Errors)

3. Objekt-Typen
type User = {
  id: number;
  name: string;
};

Optional
name?: string

Readonly
readonly id: number

4. Union & Intersection Types
Union
let value: string | number;

Intersection
type Admin = User & { role: "admin" };

5. Arrays & Tuples
Arrays
let numbers: number[] = [1, 2, 3];

Tuples
let entry: [string, number];

6. Enums
enum Status { Ok, Error }

7. Funktionen
function greet(name: string): string {
  return "Hello " + name;
}


Optional: name?: string

Default: function f(x: number = 10){}

Parameter- und Rückgabewerte sind typisiert

8. Interfaces
interface Person {
  name: string;
  age: number;
}


Werden hauptsächlich für Objektstrukturen verwendet

können erweitert werden:

interface Employee extends Person {
  id: number;
}

9. Klassen
class User {
  constructor(public name: string) {}
}


public, private, protected

readonly möglich

TypeScript ändert nichts am JS-Verhalten, sondern nur die Typen zur Übersetzungszeit

10. Generics – extrem wichtig
function wrap<T>(value: T): T {
  return value;
}


erlauben flexible, typsichere Funktionen und Klassen

unverzichtbar bei Frameworks (React, NestJS, Express-Middleware, Prisma)

11. Tooling
tsconfig.json

konfigurierte Datei für den Compiler

wichtige Einstellungen:

"strict": true

"target": "ES2022"

"module": "ESNext"

"outDir": "./dist"

12. Kompilieren
tsc


oder im Watch-Mode:

tsc --watch

13. Ecosystem

Wird überall verwendet, wo moderne JS-Backends existieren:
Node.js, Deno, Bun, Next.js, React, Angular, Svelte, NestJS.

🔷 Fertig — TypeScript vollständig zusammengefasst.
✅ 🔶 TEIL 2 — JS-Laufzeitumgebungen (Node.js, Deno, Bun)
A) Node.js
1. Was Node ist

eine JavaScript-Laufzeit für Server & Tools

basiert auf V8 (Chrome Engine)

ermöglicht JS außerhalb des Browsers

2. Node-Module
CommonJS (älter)
const fs = require("fs");
module.exports = ...

ES Modules (modern)
import fs from "fs";
export default ...

3. NPM – der wichtigste Teil

Standard-Paketmanager von Node

npm init → erstellt eine package.json

npm install express

package.json enthält:

Abhängigkeiten

Scripts

Name, Version, Beschreibung

Beispiel:

{
  "scripts": {
    "dev": "node index.js"
  }
}

4. Asynchrones Modell / Event Loop

Node ist non-blocking

arbeitet überwiegend mit Promises und async/await

5. HTTP-Server in Node
import http from "http";

const server = http.createServer((req, res) => {
  res.end("Hello");
});

server.listen(3000);

6. Frameworks auf Node-Basis

Express (klassisch)

NestJS (enterprise)

Fastify (modern & schnell)

Next.js (Fullstack)

B) Deno
1. Was Deno ist

vom selben Erfinder wie Node (Ryan Dahl)

Verbesserungen:

sicherer: Sandboxed, Permission-System

integriertes TypeScript ohne Konsole

Web APIs statt Node-spezifische APIs

2. Import per URL
import { serve } from "https://deno.land/std/http/server.ts";

3. Standardbefehle
deno run app.ts
deno task start

4. Zielpublikum

moderne Web-APIs

TypeScript-first

cleane Syntax ohne Node-Historie

C) Bun
1. Bun = Node, nur viel schneller

sehr schnelle Startup-Zeit

sehr schneller Paketmanager

schneller Bundler

integrierter Test-Runner

2. Hauptfeatures

bun install → extrem schnell

bun run file.ts → direkte Ausführung

Bundler & Transpiler eingebaut

kompatibel mit Node-APIs

3. Zielpublikum

Entwickler, die Geschwindigkeit wollen

moderne Projekte

Tools, Scripts, Fullstack-Webserver