speler1score = input("Wat heeft speler 1 gescoord?")
speler2score = input("En wat heeft speler 2 gescoord?")

if speler1score > speler2score:
    print("Speler 1 heeft het spel gewonnen!")
elif speler2score > speler1score:
    print("Speler 2 heeft het spel gewonnen!")
else:
    print("Er is gelijk gespeeld!")