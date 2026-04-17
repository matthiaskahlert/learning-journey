void main() {
  // Rekursive Funktion zur Berechnung der Fakultät
  int fakultaet(int n) {
    if (n <= 1) {
      return 1;
    }
    return n * fakultaet(n - 1);
  }

  print('Fakultät von 5: ${fakultaet(5)}'); // 120 (5 * 4 * 3 * 2 * 1)

  // Rekursive Fibonacci-Funktion
  int fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
  }

  print('Fibonacci von fibonacci(6): ${fibonacci(6)}'); // 8
}
