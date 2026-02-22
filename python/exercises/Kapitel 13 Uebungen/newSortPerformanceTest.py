import random
import timeit

def quicksort(s):
    if len(s) <= 1:
        return s
    else:
        pivot = s[0]
        s1 = [x for x in s[1:] if x < pivot]
        s2 = [x for x in s[1:] if x >= pivot]
        return quicksort(s1) + [pivot] + quicksort(s2)

zufallszahlen = [random.randint(0, 1000000) for _ in range(10000)]

def test_quicksort():
    quicksort(zufallszahlen.copy())

def test_sorted():
    sorted(zufallszahlen)

qs_time = timeit.timeit(test_quicksort, number=100)
builtin_time = timeit.timeit(test_sorted, number=100)

print(f"Quicksort: {qs_time:.4f} s")
print(f"sorted():  {builtin_time:.4f} s")