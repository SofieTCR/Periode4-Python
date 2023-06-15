import datetime

userYear = input("Welk jaar gaat het om?")
userMonth = input("Welke maand?")
userDay = input("En welke dag?")

timestamp = datetime.datetime(int(userYear), int(userMonth), int(userDay))
now = datetime.datetime.now()

difference = timestamp - now

print(difference.days)