# Caesar-Chiffre Projekt - Vollständiger Plan

## 🎯 Ziel
Entwicklung einer Caesar-Chiffre-Anwendung mit Multithreading in Java zur praktischen Anwendung kryptographischer Konzepte.

---

## 1️⃣ Performance-Analyse

| Kriterium | JavaScript | Java |
|-----------|-----------|------|
| **Brute-Force 25 Verschiebungen** | ~1ms | ~0.1ms |
| **Overhead** | Keine | JVM-Start |
| **Für 1 Text** | ✅ Ausreichend | Overkill |
| **Multithreading** | ❌ Single-threaded | ✅ Ja, möglich |
| **25 Verschlüsselungen parallel** | Seriell | 25 Threads gleichzeitig |

**Entscheidung:** Java mit Multithreading (Lerneffekt + Skalierbarkeit)

---

## 2️⃣ Anforderungen & Features

### Funktionalität
- ✅ **Verschlüsseln:** Text + Verschiebung (1-25) → verschlüsselter Text
- ✅ **Entschlüsseln:** Text + Verschiebung (1-25) → original Text
- ✅ **Brute-Force:** Text → alle 25 Varianten mit Nummern
- ✅ **Groß-/Kleinschreibung bewahren:** A/a, B/b, etc.
- ✅ **Nur A-Z verarbeiten:** Leerzeichen, Zahlen, Sonderzeichen bleiben unverändert
- ✅ **Umlaute ignorieren:** ä→a, ö→o, ü→u (oder entfernen)

### Performance-Anforderungen
- Brute-Force nutzt 25 Threads parallel (einer pro Verschiebung)
- ExecutorService mit fixem Thread-Pool
- Ergebnisse gesammelt und sortiert nach Verschiebung (1-25)

---

## 3️⃣ Architektur & Klassen

### 📁 Datei-Struktur
```
java/src/main/java/exercises/Caesar/
├── CaesarCipher.java        # Kernlogik für einzelne Verschiebung
├── CaesarBruteForce.java    # Multithreading-Brute-Force
├── CaesarApp.java           # Hauptprogramm & Benutzermenü
└── CaesarTest.java          # Unit-Tests (optional)
```

### CaesarCipher.java
```java
public class CaesarCipher {
    // Methoden:
    // - encrypt(String text, int shift) → String
    // - decrypt(String text, int shift) → String
    // - isValidShift(int shift) → boolean
}
```

### CaesarBruteForce.java
```java
public class CaesarBruteForce {
    // Methoden:
    // - bruteForce(String text) → Map<Integer, String>
    //   (nutzt ExecutorService mit 25 Threads)
    // - formatResults(Map<Integer, String>) → String
}
```

### CaesarApp.java
```java
public class CaesarApp {
    // Methoden:
    // - main() → Menü-Loop
    // - showMenu() → 1=Verschlüsseln, 2=Entschlüsseln, 3=Brute-Force, 4=Exit
    // - handleEncrypt()
    // - handleDecrypt()
    // - handleBruteForce()
    // - getUserInput() → String
}
```

---

## 4️⃣ Benutzerinteraktion (CLI)

### Menü
```
===== CAESAR-CHIFFRE =====
1. Verschlüsseln
2. Entschlüsseln
3. Brute-Force
4. Beenden
Wahl: _
```

### Verschlüsseln
```
Text eingeben: hallo
Verschiebung (1-25): 5
Ergebnis: mfqqt
```

### Entschlüsseln
```
Text eingeben: mfqqt
Verschiebung (1-25): 5
Ergebnis: hallo
```

### Brute-Force
```
Text eingeben: uhlDAReHHw
Berechne alle 25 Varianten...

Verschiebung 1: vikEBSfiIIx
Verschiebung 2: wjlFCTgjJJy
...
Verschiebung 25: tgkCDQehHHv
```

---

## 5️⃣ Multithreading-Details

### ExecutorService Setup
- `Executors.newFixedThreadPool(25)` für alle 25 Shifts gleichzeitig
- Callable<String> für jede Verschiebung
- Future-Liste sammelt Ergebnisse
- `awaitTermination()` wartet auf Completion

### Thread-Sicherheit
- Immutable Strings (kein Race Condition)
- ConcurrentHashMap für Ergebnisse (optional, falls gemeinsamer Zustand)
- Keine synchronized Blöcke nötig für diese Logik

---

## 6️⃣ Implementierungs-Reihenfolge

1. **CaesarCipher.java** schreiben + testen
   - encrypt/decrypt Logik (Modulo-Arithmetik)
   - Edge-Cases: Groß-/Kleinschreibung, Non-Alpha-Zeichen

2. **CaesarBruteForce.java** schreiben + testen
   - ExecutorService aufsetzen
   - 25 Threads starten
   - Ergebnisse sammeln & formatieren

3. **CaesarApp.java** schreiben
   - Menü & User-Input
   - Integiere CaesarCipher & CaesarBruteForce

4. **Testen**
   - Test-Cases für encrypt/decrypt
   - Brute-Force performance messen
   - Beispiel: `uhlDAReHHw` durchprobieren

---

## 7️⃣ Testfälle

| Input | Verschiebung | Ergebnis | Status |
|-------|-------------|----------|--------|
| `hello` | 5 | `mjqqt` | ✅ |
| `Hello World!` | 3 | `Khoor Zruog!` | ✅ |
| `xyz` | 3 | `abc` | ✅ (Wrap-around) |
| `ABC abc 123!` | 1 | `BCD bcd 123!` | ✅ (Nicht-Alpha bleiben) |
| `uhlDAReHHw` | Brute-Force | Alle 25 | 🔄 |

---

## 8️⃣ Bonus-Features (Optional)

- [ ] Häufigkeitsanalyse (welche Buchstaben kommen vor?)
- [ ] Deutsch-Wörterbuch laden und beste Alternative finden
- [ ] GUI mit JavaFX statt CLI
- [ ] File-Input/Output (Dateien ver-/entschlüsseln)

---

## ✅ Projektstatus

- [ ] CaesarCipher.java erstellt
- [ ] CaesarBruteForce.java erstellt
- [ ] CaesarApp.java erstellt
- [ ] Tests geschrieben & bestanden
- [ ] Performance gemessen
- [ ] Dokumentation fertig