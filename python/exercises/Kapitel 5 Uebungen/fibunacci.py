def f(n):
    """
    diese rekursive Funktion übernimmt eine natürliche Zahl n als Argument 
    und gibt die n-te Fibonacci-Zahl zurück. 0, 1, 1, 2, 3, 5, 8, 13, ...

    Beispiel für n = 5
    f(5) = f(4) + f(3)
    f(4) = f(3) + f(2)
    f(3) = f(2) + f(1)
    f(2) = f(1) + f(0)


    Es gibt zwei Basisfälle:
    f(1) = 1
    f(0) = 0
    ................
    Dann wird folgendermaßen gerechnet:

    f(2) = 1 + 0 = 1
    f(3) = 1 + 1 = 2
    f(4) = 2 + 1 = 3
    f(5) = 3 + 2 = 5
    

    """
    if n == 0: return 0
    if n == 1: return 1
    return f(n-1) + f(n-2) # z.B. bei n = 2: f(2) = f(2-1) + f(2-2) = 1

n = int(input("Welche Fibonacci-Zahl soll berechnet werden? ")) #die eingabe ist ein string und wird in int konvertiert
print(f"F({n}) = {f(n)}") #f string mit n und rückgabewert
