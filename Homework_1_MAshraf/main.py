#Muhammad S Ashraf 1763709
from datetime import date

def calculateAge(currentDate,birthDate):
        today = currentDate
        age = today.year - birthDate.year -((today.month, today.day)< (birthDate.month, birthDate.day))

        return age

print("Birthday Calculator")
print('Current day')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))
print('Birthday')
birth_month = int(input('Month: '))
birth_day = int(input('Day: '))
birth_year = int(input('Year: '))
print("You are", calculateAge(date(current_year, current_month, current_day), date(birth_year, birth_month, birth_day)), "years old.")
if current_day == birth_day and current_month == birth_month:
    print("Happy Birthday!")