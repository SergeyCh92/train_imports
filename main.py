from application.people import get_employees
from application.salary import calculate_salary
import datetime


def formatted_now():
    now = datetime.datetime.now()
    formatted_data = now.strftime('%H:%M %d.%m.%Y')
    print(f'Сейчас {formatted_data}.')


formatted_now()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
