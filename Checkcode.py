
import Switch


def check_code(code):
    even = []
    odd = []

    for i in range(0, 15, 2):
        odd.append(code[i])

    for i in range(1, 14, 2):
        even.append(code[i])

    toteven = 0
    totodd = 0

    for i in even:
        toteven += Switch.switch_even(str(i))

    for i in odd:
        totodd += Switch.switch_odd(str(i))

    final_value = (toteven + totodd) % 26

    return str(Switch.switch_final_value(final_value))
