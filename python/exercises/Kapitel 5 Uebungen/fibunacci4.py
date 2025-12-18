def fib(n):
    """
    Berechnet die n-te Fibonacci-Zahl iterativ.
    Funktioniert auch für sehr große n ohne Rekursionslimit.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Memoization-Liste: speichert alle Fibonacci-Zahlen bis n
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

# Test: F(1500)
n = int(input("Welche Fibonacci-Zahl soll berechnet werden? "))
print(f"F({n}) = {fib(n)}")
