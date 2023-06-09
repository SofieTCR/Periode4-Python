inputtext = ""
Dominique = 0
Zacharia = 0

while inputtext != "UITSLAG":
    inputtext = input("Op wie wilt u stemmen?")
    if inputtext == "Dominique":
        Dominique = Dominique + 1
    elif inputtext == "Zacharia":
        Zacharia = Zacharia + 1
    else:
        print("Onjuiste invoer, stem AUB opniew")

if Dominique > Zacharia:
    print("Dominique is de nieuwe president")
elif Zacharia > Dominique:
    print("Zacharia is de nieuwe president")
else:
    print("De score is gelijk")