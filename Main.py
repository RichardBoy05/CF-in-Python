
import User
import Code

print("\nCalcolatore del codice fiscale in Python!!!\n\n")

surname = User.getsurname()
name = User.getname()
day = User.getday()
month = User.getmonth()
year = str(User.getyear())
sex = User.getsex()
place = User.getplace()

code = Code.getcode(surname, name, day, month, year, sex, place)

if code != - 1:
    print("\nIl tuo codice fiscale è: " + code)
else:
    print("\nIl comune che hai inserito non esiste!")