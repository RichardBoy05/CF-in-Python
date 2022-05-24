
def getsurname():
    surname = input("Inserisci il tuo cognome: ")

    return surname.lower()


def getname():
    name = input("Inserisci il tuo nome: ")

    return name.lower()


def getday():
    day = int(input("Inserisci il tuo giorno di nascita: "))

    while day < 1 or day > 31:
        day = int(input("Inserisci un giorno valido: "))

    return day


def getmonth():
    month = int(input("Inserisci il tuo mese di nascita (1 - 12): "))

    while month < 1 or month > 12:
        day = int(input("Inserisci un mese valido: "))

    return month


def getyear():
    year = int(input("Inserisci il tuo anno di nascita: "))

    while len(str(year)) != 4:
        year = int(input("L'anno deve essere espresso con 4 cifre: "))

    return year


def getsex():
    sex = input("Inserisci il tuo sesso (m/f): ")

    while sex.lower() != "m" and sex.lower() != "f":
        sex = input("Inserisci un valore valido (m/f): ")

    return sex.lower()


def getplace():
    place = input("Inserisci il tuo comune di nascita: ")

    return place.lower()
