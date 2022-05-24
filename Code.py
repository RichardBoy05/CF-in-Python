
import Checkcode
import Elements


def getcode(surname, name, day, month, year, sex, place):

    place_check = Elements.place(place)

    if place_check != - 1:
        code = Elements.surname(surname) + Elements.name(name) + Elements.year(year) + Elements.month(month) + \
               Elements.day_sex(day, sex) + place_check
        check = Checkcode.check_code(code)

        return code + check

    return -1
