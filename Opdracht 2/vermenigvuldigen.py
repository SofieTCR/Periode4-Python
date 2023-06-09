def get_Product(arg1, arg2):
    return int(arg1) * int(arg2)

getal1 = input("Wat is het eerste getal?")
getal2 = input("En wat is het tweede getal?")
resultaat = "Het resultaat is: {}"

print(resultaat.format(get_Product(getal1, getal2)))