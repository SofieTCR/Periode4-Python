def get_Faculty(arg):
    countbefore = range(1,arg+1)
    result = 1
    for num in countbefore:
        result *= num
    return result

getal = int(input("Wat is het getal?"))
resultaat = "De faculty van {} is {}"
print(resultaat.format(getal, get_Faculty(getal)))