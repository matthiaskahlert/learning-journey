def f(n, memo={}):
    """
    Berechnet die n-te Fibonacci-Zahl effizient mit Memoization.

    Args:
        n (int): Position in der Fibonacci-Folge (n >= 0)
        memo (dict): Zwischenspeicher für bereits berechnete Werte

    Returns:
        int: n-te Fibonacci-Zahl
    """
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = f(n-1, memo) + f(n-2, memo)
    return memo[n]

# Test
for i in range(16):
    print(f"F({i}) = {f(i)}")

n = int(input("Welche Fibonacci-Zahl soll berechnet werden? ")) #die eingabe ist ein string und wird in int konvertiert
print(f"F({n}) = {f(n)}") #f string mit n und rückgabewert