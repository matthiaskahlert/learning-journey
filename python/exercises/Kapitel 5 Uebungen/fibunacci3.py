from multiprocessing import Pool

def f(n):
    if n == 0: return 0
    if n == 1: return 1
    return f(n-1) + f(n-2)

def fib_wrapper(n):
    return (n, f(n))

def berechne_pool():
    zahlen = list(range(20))
    with Pool(processes=12) as pool:
        ergebnisse = pool.map(fib_wrapper, zahlen)
    for n, wert in ergebnisse:
        print(f"F({n}) = {wert}")

if __name__ == "__main__":
    # Pool-Aufruf
    berechne_pool()

    # Benutzerinput danach
    n = int(input("Welche Fibonacci-Zahl soll berechnet werden? "))
    print(f"F({n}) = {f(n)}")
