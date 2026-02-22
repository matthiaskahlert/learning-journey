import random
import time

# Daten vorbereiten AUSSERHALB der Messung. Es werden 10000 Zufallszahlen zwischen 0 und 1.000.000 generiert.
zufallszahlen = [random.randint(0, 1000000) for _ in range(10000)]

# Nur das Sortieren messen
from quicksort import quicksort
start_time = time.perf_counter()
sortierte_zahlen = quicksort(zufallszahlen.copy())  # copy() für Fairness
end_time = time.perf_counter()

print(f"Quicksort dauerte: {(end_time - start_time)*1000:.3f} ms")

# Zum Vergleich: Pythons sorted()
start_time = time.perf_counter()
sortierte_builtin = sorted(zufallszahlen)
end_time = time.perf_counter()

print(f"Python sorted() dauerte: {(end_time - start_time)*1000:.3f} ms")

# Quicksort dauerte: 0.499 ms
# Python sorted() dauerte: 0.944 ms
