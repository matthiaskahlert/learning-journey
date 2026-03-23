# Derby ij – Quick Start mit relativen Pfaden

## 🚀 Schnelle Anleitung zur Derby ij-Konsole

### Option 1: PowerShell-Skript (empfohlen für alle Rechner)

Das Skript `start_ij.ps1` befindet sich im `java/`-Verzeichnis und startet die ij-Konsole automatisch mit den richtigen Pfaden:

```powershell
cd C:\Users\velpTEC edutainment\repositories\learning-journey\java
.\start_ij.ps1
```

**Vorteil**: Funktioniert auf allen Rechnern, da relative Pfade verwendet werden!

---

### Option 2: Manuelle Eingabe mit relativen Pfaden

1. **Ins java-Verzeichnis wechseln**:
```powershell
cd C:\Users\[User Directory]\repositories\learning-journey\java
```

2. **ij-Konsole starten**:
```powershell
java -cp "lib/derbytools.jar;lib/derby.jar" org.apache.derby.tools.ij
```

3. **Erfolgreiches Starten erkennbar an**:
```
ij>
```

---

## 📋 SQL-Befehle in der ij-Konsole

### Datenbank verbinden oder erstellen:
```sql
CONNECT 'jdbc:derby:meineDatenbank;create=true';
```

### Tabelle anlegen:
```sql
CREATE TABLE games (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(100),
    genre VARCHAR(50),
    release_year INT
);
```

### Daten einfügen:
```sql
INSERT INTO games (title, genre, release_year)
VALUES ('The Witcher 3', 'RPG', 2015);
```

### Daten abfragen:
```sql
SELECT * FROM games;
```

### Daten aktualisieren:
```sql
UPDATE games
SET genre = 'Action RPG'
WHERE id = 1;
```

### Daten löschen:
```sql
DELETE FROM games
WHERE id = 1;
```

### Tabelle löschen:
```sql
DROP TABLE games;
```

### Verbindung schließen:
```sql
DISCONNECT;
```

### ij beenden:
```
exit;
```

---

## 💡 Wichtige Hinweise

- Jeder SQL-Befehl muss mit einem **Semikolon** (`;`) enden
- Das Datenbankverzeichnis wird automatisch erstellt, wenn `create=true` gesetzt ist
- Derby speichert die Datenbank als **Ordnerstruktur**, nicht als einzelne `.db`-Datei
- Die Datenbank wird im Verzeichnis `java/meineDatenbank/` gespeichert
