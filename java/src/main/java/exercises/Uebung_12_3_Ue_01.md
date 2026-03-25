Beschreibe die Schritte, die notwendig sind, um in Java einen Thread zu erstellen, 
der eine gemeinsame Ressource sicher verwaltet, um ein Data Race zu verhindern. 
Gehe dabei auch auf die Verwendung von synchronized und ReentrantLock ein. 
Erkläre, wie diese Mechanismen funktionieren und in welchen Situationen du sie einsetzen würdest.


1. Es wird eine gemeiname Variable geben, auf die beide threads zugreifen wollen.
z.b. 
```java
static int zaehlerMitLock = 0;
```

2. Dann brauchen wir ein Lock-Objekt, das den Zugriff auf die Variable schützt z.B. ReentrantLock:
```java
static ReentrantLock lock = new ReentrantLock()
```

3. Dann sollte man die threads erstellen
```java
Thread thread1 = new Thread(() -> {
             // auszuführender code für thread 1
            }
        );

Thread thread2 = new Thread(() -> {
             // auszuführender code für thread 2
            }
        );        
```
4. Man muss die threads starten
```java
thread1.start(); // Thread starten, nicht .run()!
thread2.start();
```

5. man nutzt .join(). .join wartet  bis der erste Thread fertig ist, damit es zu keine datarace kommt
```java
thread1.join();
thread2.join();
```

6. Im thread selbst muss man den zugriff auf die gemeinsame variable mit dem lock schützen.
lock.lock() sperrt den zugriff, lock.unlock() gibt ihn wieder frei.
unlock sollte immer in einem finally-block stehen, damit das lock auch bei fehlern freigegeben wird.
```java
lock.lock();
try {
    zaehlerMitLock++;
} finally {
    lock.unlock();
}
```

7. alternativ kann man statt ReentrantLock auch synchronized verwenden.
synchronized ist einfacher, weil man sich nicht um lock/unlock kümmern muss, das passiert automatisch.
```java
synchronized void erhoeheZaehler() {
    zaehlerMitLock++;
}
```
oder als block:
```java
synchronized (lockObjekt) {
    zaehlerMitLock++;
}
```

### Wann synchronized, wann ReentrantLock?

- **synchronized** nutzt man, wenn es einfach bleiben soll. man schreibt weniger code und kann nichts vergessen (kein unlock nötig). reicht für die meisten fälle.
- **ReentrantLock** nutzt man, wenn man mehr kontrolle braucht, z.b.:
  - tryLock() – man will nicht ewig warten, sondern prüfen ob das lock frei ist
  - lockInterruptibly() – man will das warten abbrechen können
  - fairness – threads sollen in der reihenfolge drankommen, in der sie angefragt haben
