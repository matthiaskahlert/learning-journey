 Dart-Syntax
Erkläre die Unterschiede zwischen den Variablendeklarationen var, final und const in Dart. 
Verwende für jede der drei Deklarationsarten ein eigenes Beispiel, das nicht im Kontext genannt wurde, und verdeutliche, in welchen Situationen jede dieser Deklarationsarten bevorzugt verwendet wird. Beschreibe außerdem, wie Dart Typinferenz bei der Verwendung von var handhabt und warum es wichtig sein könnte, final oder const anstelle von var zu verwenden.

- **`var`**: Deklariert eine Variable, deren Wert später geändert werden kann.
  ```dart
  var name = 'Alice';
  name = 'Bob'; // Gültig
  ```

- **`final`**: Deklariert eine Variable, die nach der Initialisierung nicht mehr geändert werden kann. Der Wert einer `final`-Variable kann jedoch zur Laufzeit berechnet werden.
  ```dart
  final currentTime = DateTime.now();
  // currentTime = DateTime.now(); // Fehler: Wert kann nicht geändert werden
  ```

- **`const`**: Deklariert eine Kompilierzeit-Konstante. Der Wert muss bereits zur Kompilierzeit vollständig bekannt sein.
  ```dart
  const pi = 3.14159;
  // const area = pi * radius; // Fehler, wenn radius nicht const ist
  ```

**Zusammenfassung:**
| Schlüsselwort | Änderbarkeit | Zeitpunkt der Wertzuweisung |
|---------------|--------------|-----------------------------|
| `var`         | Änderbar     | Zur Laufzeit                |
| `final`       | Nicht änderbar | Zur Laufzeit                |
| `const`       | Nicht änderbar | Zur Kompilierzeit           |