# Die Klausurersatzleistung von Arasp, Malte, Nick und Tobias

import math

# Aufgabe 1

# Diese Funktion überprüft, ob eine gegebene Zahl eine Primzahl ist.
def isPrime(n):
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
        # Wenn i größer als die Wurzel von n ist, ist n eine Primzahl.
        if i > r:
            # Gib True zurück, wenn n eine Primzahl ist.
            return True

        # Wenn n durch i restlos teilbar ist, ist n keine Primzahl.
        if n % i == 0:
            # Gib False zurück, wenn n keine Primzahl ist.
            return False

        # Erhöhe i um 2, da alle Primzahlen größer als 2 ungerade sind.
        # Nachdem i erhöht wurde, wird die Schleife erneut durchlaufen.
        # Dies wird so lange wiederholt, bis i größer als die Wurzel von n ist.
        i += 2
        # Es wurde schon geprüft, ob n durch 2 teilbar ist, deshalb kann i um 2 erhöht werden.

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
# Goldbachsche Vermutung: Jede gerade Zahl größer als 2 ist die Summe von zwei Primzahlen.
def Zerlegung(n):
    # Überprüfe, ob n eine gerade Zahl ist.
    if n % 2 == 1:
        raise ValueError("n muss eine gerade Zahl sein")

    # Anzahl der Zerlegungen
    anzahl = 0
    
    # Prüfe alle Zahlen zwischen 2 und n.
    # Wenn sowohl i als auch n-i Primzahlen sind, erhöhe die Anzahl der Zerlegungen um 1.
    for i in range(2, n):
        if isPrime(i):
            if isPrime(n - i):
                anzahl += 1
    # Gib die Anzahl der Zerlegungen zurück.
    return anzahl

# Nutzer-Eingabe
n = int(input("Geben Sie eine gerade Zahl ein: "))

# Ermittle die Anzahl der Zerlegungen von n als Summe von zwei Primzahlen.
anzahl = Zerlegung(n)

# Gib das Ergebnis aus.
print(f"Die Zahl {n} lässt sich {anzahl}-mal als Summe von zwei Primzahlen darstellen.")

# Gib alle Zerlegungen von n als Summe von zwei Primzahlen aus.
for i in range(2, n):
    # Wenn sowohl i als auch n-i Primzahlen sind, gib die Zerlegung aus.
    if isPrime(i):
        if isPrime(n - i):
            # Gib die Zerlegung aus.
            print(f"{i} + {n - i}")
