
def surname(surname):
    output = ""

    surname = surname.replace(" ", "")
    surname = surname.replace("'", "")

    for i in surname:
        if i not in "aeiou":
            output += i
            if len(output) >= 3:
                break

    if len(output) < 3:
        for i in surname:
            if i in "aeiou":
                output += i
                if len(output) >= 3:
                    break

    while len(output) < 3:
        output += "x"

    return output.upper()


def name(name):
    output = ""

    name = name.replace(" ", "")
    name = name.replace("'", "")

    for i in name:
        if i not in "aeiou":
            output += i

    if len(output) > 3:
        output = output[0] + output[2] + output[3]

    if len(output) < 3:
        for i in name:
            if i in "aeiou":
                output += i
                if len(output) >= 3:
                    break

    while len(output) < 3:
        output += "x"

    return output.upper()


def year(year):
    return year[2:]


def month(month):
    letters = ["A", "B", "C", "D", "E", "H", "L", "M", "P", "R", "S", "T"]

    return letters[month - 1]


def day_sex(day, sex):
    output = day

    if sex == "f":
        output += 40

    if output < 10:
        return "0" + str(output)

    return str(output)


def place(place):
    try:
        with open("Comuni.txt") as file:

            for line in file:
                semiline = line.split(";")

                if semiline[0].lower() == place:
                    return semiline[1][0:4]

    except FileNotFoundError:
        print("File dei comuni non trovato!")

    return -1
