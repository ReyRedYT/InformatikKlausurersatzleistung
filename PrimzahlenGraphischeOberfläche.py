# Die Klausurersatzleistung von Arasp, Malte, Nick und Tobias

import math
import tkinter as tk
from tkinter import messagebox
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

# Aufgabe 2

# Diese Funktion gibt eine Liste aller Primzahlen zurück, die kleiner oder gleich n sind.
def getPrimes(n):
    primes = []
    for i in range(2, n+1):
        if isPrime(i):
            primes.append(i)
    return primes

# Aufgabe 3

# Diese Funktion ermittelt die Anzahl der Zerlegungen einer geraden Zahl n als Summe von zwei Primzahlen.
# Goldbachsche Vermutung: Jede gerade Zahl größer als 2 ist die Summe von zwei Primzahlen.
def Zerlegung(n):
    # Überprüfe, ob n eine gerade Zahl ist.
    if n % 2 == 1:
        messagebox.showerror("Fehler", f"{n} ist keine gerade Zahl.") # Fehlermeldung als Pop-Up
        raise ValueError(f"{n} ist keine gerade Zahl.") # Fehlermeldung in der Konsole

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

# Für Aufgabe 1
# Funktion, die beim Klicken des Buttons ausgeführt wird
def button_click():
    # Nutzer-Eingabe
    n = int(entry.get())

    # Überprüfe, ob die eingegebene Zahl eine Primzahl ist.
    if isPrime(n):
        result_label.config(text=f"{n} ist eine Primzahl.")
    else:
        result_label.config(text=f"{n} ist keine Primzahl.")

# Für Aufgabe 2
# Funktion, die beim Klicken des Buttons ausgeführt wird
def button_click2():
    # Nutzer-Eingabe
    n = int(entry2.get())

    # Erstelle eine Liste der Primzahlen kleiner oder gleich n.
    primeList = getPrimes(n)

    # Gib das Ergebnis aus.
    result_label2.config(text=f"Die Primzahlen kleiner oder gleich {n} sind: {primeList}")

# Für Aufgabe 3
# Funktion, die beim Klicken des Buttons ausgeführt wird
def button_click3():
    # Nutzer-Eingabe
    n = int(entry3.get())

    # Ermittle die Anzahl der Zerlegungen von n als Summe von zwei Primzahlen.
    anzahl = Zerlegung(n)

    # Gib das Ergebnis aus.
    result_label3.config(text=f"Die Zahl {n} lässt sich {anzahl}-mal als Summe von zwei Primzahlen darstellen.")

    # Gib alle Zerlegungen von n als Summe von zwei Primzahlen aus.
    for i in range(2, n):
        # Wenn sowohl i als auch n-i Primzahlen sind, gib die Zerlegung aus.
        if isPrime(i):
            if isPrime(n - i):
                # Gib die Zerlegung aus.
                result_label3.config(text=result_label3.cget("text") + f"\n{i} + {n - i}")

# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Primzahl-Checker")
window.geometry("800x600")

# Erstelle ein Label und ein Entry für die Nutzer-Eingabe
label = tk.Label(window, text="Gib eine Zahl ein:") # Erstelle ein Label
label.pack() # Packe das Label in das Fenster
entry = tk.Entry(window) # Erstelle ein Entry
entry.pack() # Packe das Entry in das Fenster

# Erstelle einen Button, der die Funktion button_click ausführt
button = tk.Button(window, text="Überprüfen", command=button_click) # Erstelle einen Button
button.pack() # Packe den Button in das Fenster

# Erstelle ein Label für das Ergebnis
result_label = tk.Label(window, text="") # Erstelle ein Label
result_label.pack() # Packe das Label in das Fenster

# Erstelle ein Label und ein Entry für die Nutzer-Eingabe
label2 = tk.Label(window, text="Geben Sie eine Zahl ein:") # Erstelle ein Label
label2.pack()   # Packe das Label in das Fenster
entry2 = tk.Entry(window) # Erstelle ein Entry
entry2.pack() # Packe das Entry in das Fenster

# Erstelle einen Button, der die Funktion button_click2 ausführt
button2 = tk.Button(window, text="Primzahlen anzeigen", command=button_click2) # Erstelle einen Button
button2.pack() # Packe den Button in das Fenster

# Erstelle ein Label für das Ergebnis
result_label2 = tk.Label(window, text="") # Erstelle ein Label
result_label2.pack() # Packe das Label in das Fenster

# Erstelle ein Label und ein Entry für die Nutzer-Eingabe
label3 = tk.Label(window, text="Geben Sie eine gerade Zahl ein:") # Erstelle ein Label
label3.pack() # Packe das Label in das Fenster
entry3 = tk.Entry(window) # Erstelle ein Entry
entry3.pack() # Packe das Entry in das Fenster

# Erstelle einen Button, der die Funktion button_click3 ausführt
button3 = tk.Button(window, text="Zerlegungen anzeigen", command=button_click3) # Erstelle einen Button
button3.pack() # Packe den Button in das Fenster

# Erstelle ein Label für das Ergebnis
result_label3 = tk.Label(window, text="") # Erstelle ein Label
result_label3.pack() # Packe das Label in das Fenster

# Starte die Hauptloop des Fensters
# Hält das Fenster offen bis es geschlossen wird
window.mainloop()


