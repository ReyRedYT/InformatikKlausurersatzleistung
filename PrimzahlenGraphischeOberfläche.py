# Importiere die benötigten Module
import math
import tkinter as tk

# Aufgabe 1

# Definiere eine Funktion, um zu überprüfen, ob eine Zahl eine Primzahl ist
def isPrime(n, verbose=False):
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    i = 3
    r = math.sqrt(n)

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

# Definiere eine Funktion, um die Primzahlüberprüfung auszuführen
def checkPrime():
    Eingabe = int(entry.get())
    if isPrime(Eingabe):
        result_label.config(text=f"{Eingabe} ist eine Primzahl.")
    else:
        result_label.config(text=f"{Eingabe} ist keine Primzahl.")

# Erstelle das Fenster
window = tk.Tk()
window.title("Primzahl-Checker")

# Erstelle die Eingabe- und Ausgabe-Widgets
input_label = tk.Label(window, text="Gib eine Zahl ein:")
input_label.pack()

entry = tk.Entry(window)
entry.pack()

check_button = tk.Button(window, text="Überprüfen", command=checkPrime)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Aufgabe 2

# Definiere eine Funktion, um alle Primzahlen bis zu einer gegebenen Zahl zu erhalten
def getPrimes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes

# Definiere eine Funktion, um die Primzahlen anzuzeigen
def showPrimes():
    n = int(entry2.get())
    primeList = getPrimes(n)
    result_label2.config(text=f"Die Primzahlen kleiner oder gleich {n} sind: {primeList}")

# Erstelle die Eingabe- und Ausgabe-Widgets für Aufgabe 2
input_label2 = tk.Label(window, text="Geben Sie eine Zahl ein:")
input_label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

show_button = tk.Button(window, text="Anzeigen", command=showPrimes)
show_button.pack()

result_label2 = tk.Label(window, text="")
result_label2.pack()

# Aufgabe 3

# Definiere eine globale Variable für die Zerlegungen
Zerlegungen :str = ""

# Definiere eine Funktion, um zu überprüfen, ob eine Zahl als Summe von zwei Primzahlen dargestellt werden kann
def MalteIstCool(n):
    global Zerlegungen
    if n % 2 == 1:
        raise ValueError("n muss eine gerade Zahl sein")

    anzahl = 0
    output = ""
    for i in range(2, n):
        if isPrime(i):
            if isPrime(n - i):
                anzahl += 1
                output += f"{i} + {n - i}\n"
                result_label3.config(text=output)
                print(f"{i} + {n - i}")
                Zerlegungen += f"{i} + {n - i}\n"
    return anzahl

# Definiere eine Funktion, um die Summen zu berechnen
def calculateSums():
    n = int(entry3.get())
    try:
        anzahl = MalteIstCool(n)
        result_label3.config(text=f"Die Zahl {n} lässt sich {anzahl}-mal als Summe von zwei Primzahlen darstellen. \n {Zerlegungen}")

    except ValueError as e:
        result_label3.config(text=str(e))

# Erstelle die Eingabe- und Ausgabe-Widgets für Aufgabe 3
input_label3 = tk.Label(window, text="Geben Sie eine gerade Zahl ein:")
input_label3.pack()

entry3 = tk.Entry(window)
entry3.pack()

calculate_button = tk.Button(window, text="Berechnen", command=calculateSums)
calculate_button.pack()

result_label3 = tk.Label(window, text="")
result_label3.pack()

# Starte die Haupt-Schleife des Fensters
window.mainloop()

# Zusätzlicher Code außerhalb des Fensters

# Definiere eine Funktion, um zu überprüfen, ob eine Zahl als Summe von zwei Primzahlen dargestellt werden kann
def MalteIstCool(n):
    if n % 2 == 1:
        raise ValueError("n muss eine gerade Zahl sein")

    anzahl = 0
    output = ""
    for i in range(2, n):
        if isPrime(i):
            if isPrime(n - i):
                anzahl += 1
                output += f"{i} + {n - i}\n"
                result_label3.config(text=output)
    return anzahl, output

try:
    n = int(input("Geben Sie eine gerade Zahl ein: "))
    anzahl, output = MalteIstCool(n)
    print(f"Die Zahl {n} lässt sich {anzahl}-mal als Summe von zwei Primzahlen darstellen.")
    print(output)
except ValueError as e:
    print(str(e))
