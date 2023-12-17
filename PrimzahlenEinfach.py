import math
import time

# Aufgabe 1

# Diese Funktion überprüft, ob eine gegebene Zahl eine Primzahl ist.
# Sie nimmt eine Zahl n und einen optionalen Parameter verbose entgegen.
# Wenn verbose=True ist, werden zusätzliche Informationen ausgegeben.
def isPrime(n, verbose=False):
    # Wenn n = 2 ist, wird True zurückgegeben, da 2 eine Primzahl ist.
    if n == 2:
        return True

    # Wenn n kleiner als 2 ist oder durch 2 teilbar ist, wird False zurückgegeben.
    if n < 2 or n % 2 == 0:
        return False

    # Prüfe alle Zahlen zwischen 3 und der Wurzel von n.
    i = 3
    r = math.sqrt(n)

    # Wenn die Wurzel eine ganze Zahl ist, ist n keine Primzahl.
    if r % 1 == 0:
        return False

    while True:
        if i > r:
            return True

        if n % i == 0:
            if verbose:
                print(f"{n} ist teilbar durch {i}")
            return False

        i += 2

# Nutzer-Eingabe
Eingabe = int(input("Gib eine Zahl ein: "))

# Überprüfe, ob die eingegebene Zahl eine Primzahl ist.
if isPrime(Eingabe):
    print(f"{Eingabe} ist eine Primzahl.")
else:
    print(f"{Eingabe} ist keine Primzahl.")

# Aufgabe 2

# Diese Funktion gibt eine Liste aller Primzahlen zurück, die kleiner oder gleich n sind.
def getPrimes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes

# Nutzer-Eingabe
n = int(input("Geben Sie eine Zahl ein: "))

# Erstelle eine Liste der Primzahlen kleiner oder gleich n.
primeList = getPrimes(n)

# Gib das Ergebnis aus.
print(f"Die Primzahlen kleiner oder gleich {n} sind: {primeList}")

# Aufgabe 3

# Diese Funktion ermittelt die Anzahl der Zerlegungen einer geraden Zahl n als Summe von zwei Primzahlen.
def Zerlegung(n):
    # Überprüfe, ob n eine gerade Zahl ist.
    if n % 2 == 1:
        raise ValueError("n muss eine gerade Zahl sein")

    anzahl = 0
    for i in range(2, n):
        if isPrime(i):
            if isPrime(n - i):
                anzahl += 1
    return anzahl

# Nutzer-Eingabe
n = int(input("Geben Sie eine gerade Zahl ein: "))

# Ermittle die Anzahl der Zerlegungen von n als Summe von zwei Primzahlen.
anzahl = Zerlegung(n)

# Gib das Ergebnis aus.
print(f"Die Zahl {n} lässt sich {anzahl}-mal als Summe von zwei Primzahlen darstellen.")

# Gib alle Zerlegungen von n als Summe von zwei Primzahlen aus.
for i in range(2, n):
    if isPrime(i):
        if isPrime(n - i):
            print(f"{i} + {n - i}")
